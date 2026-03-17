import { createClient } from '@supabase/supabase-js'

const supabaseUrl = process.env.REACT_APP_SUPABASE_URL || ''
const supabaseAnonKey = process.env.REACT_APP_SUPABASE_ANON_KEY || ''

export const supabase = createClient(supabaseUrl, supabaseAnonKey)

export type Database = {
  public: {
    Tables: {
      profiles: {
        Row: {
          id: string
          full_name: string | null
          avatar_url: string | null
          created_at: string
        }
        Insert: {
          id: string
          full_name?: string | null
          avatar_url?: string | null
          created_at?: string
        }
        Update: {
          id?: string
          full_name?: string | null
          avatar_url?: string | null
          created_at?: string
        }
      }
      categories: {
        Row: {
          id: string
          name: string
          icon: string
          color: string
          user_id: string
        }
        Insert: {
          id?: string
          name: string
          icon: string
          color: string
          user_id: string
        }
        Update: {
          id?: string
          name?: string
          icon?: string
          color?: string
          user_id?: string
        }
      }
      life_items: {
        Row: {
          id: string
          category_id: string
          title: string
          description: string | null
          amount: number | null
          unit: string | null
          target_value: number | null
          current_value: number | null
          date: string | null
          completed: boolean
          user_id: string
          created_at: string
          updated_at: string
        }
        Insert: {
          id?: string
          category_id: string
          title: string
          description?: string | null
          amount?: number | null
          unit?: string | null
          target_value?: number | null
          current_value?: number | null
          date?: string | null
          completed?: boolean
          user_id: string
          created_at?: string
          updated_at?: string
        }
        Update: {
          id?: string
          category_id?: string
          title?: string
          description?: string | null
          amount?: number | null
          unit?: string | null
          target_value?: number | null
          current_value?: number | null
          date?: string | null
          completed?: boolean
          user_id?: string
          created_at?: string
          updated_at?: string
        }
      }
      habits: {
        Row: {
          id: string
          title: string
          description: string | null
          frequency: string
          target_streak: number
          current_streak: number
          user_id: string
          created_at: string
        }
        Insert: {
          id?: string
          title: string
          description?: string | null
          frequency: string
          target_streak: number
          current_streak?: number
          user_id: string
          created_at?: string
        }
        Update: {
          id?: string
          title?: string
          description?: string | null
          frequency?: string
          target_streak?: number
          current_streak?: number
          user_id?: string
          created_at?: string
        }
      }
      habit_tracking: {
        Row: {
          id: string
          habit_id: string
          completed_at: string
          user_id: string
        }
        Insert: {
          id?: string
          habit_id: string
          completed_at?: string
          user_id: string
        }
        Update: {
          id?: string
          habit_id?: string
          completed_at?: string
          user_id?: string
        }
      }
    }
  }
}
