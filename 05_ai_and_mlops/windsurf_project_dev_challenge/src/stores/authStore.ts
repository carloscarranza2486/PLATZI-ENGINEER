import { create } from 'zustand'
import { User } from '../types'
import { supabase } from '../lib/supabase'

interface AuthState {
  user: User | null
  loading: boolean
  signIn: (email: string, password: string) => Promise<{ error: any }>
  signUp: (email: string, password: string, fullName?: string) => Promise<{ error: any }>
  signOut: () => Promise<void>
  initializeAuth: () => Promise<void>
  updateProfile: (updates: Partial<User>) => Promise<{ error: any }>
}

export const useAuthStore = create<AuthState>((set, get) => ({
  user: null,
  loading: true,

  signIn: async (email: string, password: string) => {
    try {
      const { error } = await supabase.auth.signInWithPassword({
        email,
        password
      })
      
      if (!error) {
        await get().initializeAuth()
      }
      
      return { error }
    } catch (error) {
      return { error }
    }
  },

  signUp: async (email: string, password: string, fullName?: string) => {
    try {
      const { error } = await supabase.auth.signUp({
        email,
        password,
        options: {
          data: {
            full_name: fullName
          }
        }
      })
      
      return { error }
    } catch (error) {
      return { error }
    }
  },

  signOut: async () => {
    await supabase.auth.signOut()
    set({ user: null })
  },

  initializeAuth: async () => {
    try {
      const { data: { session } } = await supabase.auth.getSession()
      
      if (session?.user) {
        const { data: profile } = await supabase
          .from('profiles')
          .select('*')
          .eq('id', session.user.id)
          .single()
        
        set({ 
          user: profile ? {
            id: profile.id,
            email: session.user.email,
            full_name: profile.full_name,
            avatar_url: profile.avatar_url
          } : null
        })
      }
    } catch (error) {
      console.error('Error initializing auth:', error)
    } finally {
      set({ loading: false })
    }
  },

  updateProfile: async (updates: Partial<User>) => {
    try {
      const { user } = get()
      if (!user) return { error: 'No user logged in' }

      const { error } = await supabase
        .from('profiles')
        .update(updates)
        .eq('id', user.id)

      if (!error) {
        set({ user: { ...user, ...updates } })
      }

      return { error }
    } catch (error) {
      return { error }
    }
  }
}))

// Listener para cambios de autenticación
supabase.auth.onAuthStateChange(async (event, session) => {
  if (event === 'SIGNED_IN' && session?.user) {
    const { data: profile } = await supabase
      .from('profiles')
      .select('*')
      .eq('id', session.user.id)
      .single()
    
    useAuthStore.setState({ 
      user: profile ? {
        id: profile.id,
        email: session.user.email,
        full_name: profile.full_name,
        avatar_url: profile.avatar_url
      } : null,
      loading: false
    })
  } else if (event === 'SIGNED_OUT') {
    useAuthStore.setState({ user: null, loading: false })
  }
})
