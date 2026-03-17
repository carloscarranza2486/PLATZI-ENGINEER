-- Perfiles de usuario (extendido de auth.users)
CREATE TABLE profiles (
  id UUID REFERENCES auth.users PRIMARY KEY,
  full_name TEXT,
  avatar_url TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Categorías de áreas de vida
CREATE TABLE categories (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name TEXT NOT NULL,
  icon TEXT NOT NULL,
  color TEXT NOT NULL,
  user_id UUID REFERENCES profiles(id) ON DELETE CASCADE
);

-- Items/registros por área
CREATE TABLE life_items (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  category_id UUID REFERENCES categories(id) ON DELETE CASCADE,
  title TEXT NOT NULL,
  description TEXT,
  amount DECIMAL(10,2), -- para finanzas
  unit TEXT, -- para ejercicio/alimentación
  target_value DECIMAL(10,2), -- metas
  current_value DECIMAL(10,2), -- progreso
  date DATE,
  completed BOOLEAN DEFAULT FALSE,
  user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Hábitos con seguimiento
CREATE TABLE habits (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  title TEXT NOT NULL,
  description TEXT,
  frequency TEXT NOT NULL CHECK (frequency IN ('daily', 'weekly', 'monthly')),
  target_streak INTEGER NOT NULL DEFAULT 30,
  current_streak INTEGER DEFAULT 0,
  user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Registro de completación de hábitos
CREATE TABLE habit_tracking (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  habit_id UUID REFERENCES habits(id) ON DELETE CASCADE,
  completed_at DATE DEFAULT CURRENT_DATE,
  user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
  UNIQUE(habit_id, completed_at, user_id)
);

-- RLS (Row Level Security)
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE categories ENABLE ROW LEVEL SECURITY;
ALTER TABLE life_items ENABLE ROW LEVEL SECURITY;
ALTER TABLE habits ENABLE ROW LEVEL SECURITY;
ALTER TABLE habit_tracking ENABLE ROW LEVEL SECURITY;

-- Políticas de RLS
CREATE POLICY "Users can view own profile" ON profiles FOR SELECT USING (auth.uid() = id);
CREATE POLICY "Users can update own profile" ON profiles FOR UPDATE USING (auth.uid() = id);

CREATE POLICY "Users can view own categories" ON categories FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own categories" ON categories FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Users can update own categories" ON categories FOR UPDATE USING (auth.uid() = user_id);
CREATE POLICY "Users can delete own categories" ON categories FOR DELETE USING (auth.uid() = user_id);

CREATE POLICY "Users can view own life items" ON life_items FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own life items" ON life_items FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Users can update own life items" ON life_items FOR UPDATE USING (auth.uid() = user_id);
CREATE POLICY "Users can delete own life items" ON life_items FOR DELETE USING (auth.uid() = user_id);

CREATE POLICY "Users can view own habits" ON habits FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own habits" ON habits FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Users can update own habits" ON habits FOR UPDATE USING (auth.uid() = user_id);
CREATE POLICY "Users can delete own habits" ON habits FOR DELETE USING (auth.uid() = user_id);

CREATE POLICY "Users can view own habit tracking" ON habit_tracking FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own habit tracking" ON habit_tracking FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Users can update own habit tracking" ON habit_tracking FOR UPDATE USING (auth.uid() = user_id);
CREATE POLICY "Users can delete own habit tracking" ON habit_tracking FOR DELETE USING (auth.uid() = user_id);

-- Trigger para actualizar updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_life_items_updated_at BEFORE UPDATE ON life_items FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Trigger para actualizar streaks de hábitos
CREATE OR REPLACE FUNCTION update_habit_streak()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        UPDATE habits 
        SET current_streak = (
            SELECT COUNT(*) 
            FROM habit_tracking 
            WHERE habit_id = NEW.habit_id 
            AND user_id = NEW.user_id
            AND completed_at >= CURRENT_DATE - INTERVAL '1 day' * (
                SELECT COUNT(*) + 1
                FROM habit_tracking ht2
                WHERE ht2.habit_id = NEW.habit_id
                AND ht2.user_id = NEW.user_id
                AND ht2.completed_at >= CURRENT_DATE - INTERVAL '1 day'
            )
        )
        WHERE id = NEW.habit_id;
        RETURN NEW;
    END IF;
    RETURN NULL;
END;
$$ language 'plpgsql';

CREATE TRIGGER habit_streak_trigger AFTER INSERT ON habit_tracking FOR EACH ROW EXECUTE FUNCTION update_habit_streak();

-- Función para crear perfil automáticamente
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO public.profiles (id, full_name, avatar_url)
    VALUES (new.id, new.raw_user_meta_data->>'full_name', new.raw_user_meta_data->>'avatar_url');
    RETURN new;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER on_auth_user_created
    AFTER INSERT ON auth.users
    FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();

-- Categorías por defecto
CREATE OR REPLACE FUNCTION create_default_categories(user_uuid UUID)
RETURNS VOID AS $$
BEGIN
    INSERT INTO categories (name, icon, color, user_id) VALUES
    ('Finanzas', 'dollar-sign', '#10B981', user_uuid),
    ('Ejercicio', 'activity', '#F59E0B', user_uuid),
    ('Alimentación', 'utensils', '#EF4444', user_uuid),
    ('Educación', 'book-open', '#3B82F6', user_uuid),
    ('Hábitos', 'check-circle', '#8B5CF6', user_uuid);
END;
$$ LANGUAGE plpgsql;
