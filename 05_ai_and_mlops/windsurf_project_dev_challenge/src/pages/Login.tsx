import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'
import { Button, Input, Card, CardHeader, CardTitle, CardContent } from '../components/ui'
import { useAuthStore } from '../stores/authStore'
import toast from 'react-hot-toast'

const loginSchema = z.object({
  email: z.string().email('Email inválido'),
  password: z.string().min(6, 'La contraseña debe tener al menos 6 caracteres')
})

const signupSchema = loginSchema.extend({
  fullName: z.string().min(2, 'El nombre debe tener al menos 2 caracteres')
})

type LoginFormData = z.infer<typeof loginSchema>
type SignupFormData = z.infer<typeof signupSchema>

export const Login: React.FC = () => {
  const [isSignUp, setIsSignUp] = useState(false)
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()
  const { signIn, signUp } = useAuthStore()

  const loginForm = useForm<LoginFormData>({
    resolver: zodResolver(loginSchema)
  })

  const signupForm = useForm<SignupFormData>({
    resolver: zodResolver(signupSchema)
  })

  const handleLogin = async (data: LoginFormData) => {
    setLoading(true)
    try {
      const { error } = await signIn(data.email, data.password)
      if (error) {
        toast.error(error.message)
      } else {
        toast.success('¡Bienvenido de vuelta!')
        navigate('/dashboard')
      }
    } catch (error) {
      toast.error('Error al iniciar sesión')
    } finally {
      setLoading(false)
    }
  }

  const handleSignUp = async (data: SignupFormData) => {
    setLoading(true)
    try {
      const { error } = await signUp(data.email, data.password, data.fullName)
      if (error) {
        toast.error(error.message)
      } else {
        toast.success('¡Cuenta creada! Revisa tu email para confirmar.')
        setIsSignUp(false)
      }
    } catch (error) {
      toast.error('Error al crear cuenta')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-background flex items-center justify-center px-4">
      <Card className="w-full max-w-md">
        <CardHeader>
          <CardTitle className="text-center">
            {isSignUp ? 'Crear Cuenta' : 'Iniciar Sesión'}
          </CardTitle>
        </CardHeader>
        <CardContent>
          {!isSignUp ? (
            <form onSubmit={loginForm.handleSubmit(handleLogin)} className="space-y-4">
              <Input
                label="Email"
                type="email"
                {...loginForm.register('email')}
                error={loginForm.formState.errors.email?.message}
              />
              <Input
                label="Contraseña"
                type="password"
                {...loginForm.register('password')}
                error={loginForm.formState.errors.password?.message}
              />
              <Button
                type="submit"
                className="w-full"
                disabled={loading}
              >
                {loading ? 'Iniciando...' : 'Iniciar Sesión'}
              </Button>
            </form>
          ) : (
            <form onSubmit={signupForm.handleSubmit(handleSignUp)} className="space-y-4">
              <Input
                label="Nombre completo"
                {...signupForm.register('fullName')}
                error={signupForm.formState.errors.fullName?.message}
              />
              <Input
                label="Email"
                type="email"
                {...signupForm.register('email')}
                error={signupForm.formState.errors.email?.message}
              />
              <Input
                label="Contraseña"
                type="password"
                {...signupForm.register('password')}
                error={signupForm.formState.errors.password?.message}
              />
              <Button
                type="submit"
                className="w-full"
                disabled={loading}
              >
                {loading ? 'Creando cuenta...' : 'Crear Cuenta'}
              </Button>
            </form>
          )}
          
          <div className="mt-6 text-center">
            <button
              type="button"
              onClick={() => setIsSignUp(!isSignUp)}
              className="text-accent hover:text-blue-600 text-sm font-medium"
            >
              {isSignUp 
                ? '¿Ya tienes cuenta? Inicia sesión' 
                : '¿No tienes cuenta? Crea una'
              }
            </button>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
