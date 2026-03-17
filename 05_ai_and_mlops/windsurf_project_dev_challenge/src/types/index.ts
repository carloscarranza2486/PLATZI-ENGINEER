export interface User {
  id: string
  email?: string
  full_name?: string | null
  avatar_url?: string | null
}

export interface Category {
  id: string
  name: string
  icon: string
  color: string
  user_id: string
}

export interface LifeItem {
  id: string
  category_id: string
  title: string
  description?: string | null
  amount?: number | null
  unit?: string | null
  target_value?: number | null
  current_value?: number | null
  date?: string | null
  completed: boolean
  user_id: string
  created_at: string
  updated_at: string
  category?: Category
}

export interface Habit {
  id: string
  title: string
  description?: string | null
  frequency: 'daily' | 'weekly' | 'monthly'
  target_streak: number
  current_streak: number
  user_id: string
  created_at: string
  tracking?: HabitTracking[]
}

export interface HabitTracking {
  id: string
  habit_id: string
  completed_at: string
  user_id: string
}

export interface DashboardStats {
  totalItems: number
  completedItems: number
  activeHabits: number
  currentStreak: number
  recentItems: LifeItem[]
  habitsProgress: Habit[]
}

export type CategoryType = 'finanzas' | 'ejercicio' | 'alimentación' | 'educación' | 'hábitos'

export interface CategoryConfig {
  name: string
  icon: string
  color: string
  fields: {
    amount?: boolean
    unit?: boolean
    target?: boolean
    date?: boolean
  }
}
