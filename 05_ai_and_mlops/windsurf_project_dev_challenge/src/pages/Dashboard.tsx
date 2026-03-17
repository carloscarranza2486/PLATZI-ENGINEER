import React from 'react'
import { Card, CardHeader, CardTitle, CardContent, Badge, ProgressBar, Button } from '../components/ui'
import { DollarSign, Activity, Utensils, BookOpen, CheckCircle, Plus } from 'lucide-react'

const mockStats = {
  totalItems: 24,
  completedItems: 18,
  activeHabits: 5,
  currentStreak: 12
}

const mockCategories = [
  { name: 'Finanzas', icon: DollarSign, color: 'text-green-500', count: 8 },
  { name: 'Ejercicio', icon: Activity, color: 'text-yellow-500', count: 6 },
  { name: 'Alimentación', icon: Utensils, color: 'text-red-500', count: 4 },
  { name: 'Educación', icon: BookOpen, color: 'text-blue-500', count: 3 },
  { name: 'Hábitos', icon: CheckCircle, color: 'text-purple-500', count: 3 }
]

const mockRecentItems = [
  { id: 1, title: 'Correr 5km', category: 'Ejercicio', completed: true, date: 'Hoy' },
  { id: 2, title: 'Leer 30 minutos', category: 'Educación', completed: true, date: 'Hoy' },
  { id: 3, title: 'Presupuesto mensual', category: 'Finanzas', completed: false, date: 'Ayer' },
  { id: 4, title: 'Meditar 10 min', category: 'Hábitos', completed: true, date: 'Ayer' }
]

const mockHabits = [
  { id: 1, title: 'Ejercicio diario', currentStreak: 12, targetStreak: 30 },
  { id: 2, title: 'Lectura', currentStreak: 8, targetStreak: 30 },
  { id: 3, title: 'Meditación', currentStreak: 15, targetStreak: 30 }
]

export const Dashboard: React.FC = () => {
  return (
    <div className="min-h-screen bg-background p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-3xl font-bold text-text">Dashboard</h1>
            <p className="text-text-secondary mt-1">Gestiona tus áreas de vida</p>
          </div>
          <Button className="flex items-center gap-2">
            <Plus className="w-4 h-4" />
            Nuevo Registro
          </Button>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <Card>
            <CardContent className="pt-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm text-text-secondary">Total Items</p>
                  <p className="text-2xl font-bold text-text">{mockStats.totalItems}</p>
                </div>
                <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
                  <CheckCircle className="w-6 h-6 text-blue-600" />
                </div>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="pt-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm text-text-secondary">Completados</p>
                  <p className="text-2xl font-bold text-text">{mockStats.completedItems}</p>
                </div>
                <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
                  <CheckCircle className="w-6 h-6 text-green-600" />
                </div>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="pt-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm text-text-secondary">Hábitos Activos</p>
                  <p className="text-2xl font-bold text-text">{mockStats.activeHabits}</p>
                </div>
                <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
                  <CheckCircle className="w-6 h-6 text-purple-600" />
                </div>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="pt-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm text-text-secondary">Racha Actual</p>
                  <p className="text-2xl font-bold text-text">{mockStats.currentStreak} días</p>
                </div>
                <div className="w-12 h-12 bg-yellow-100 rounded-lg flex items-center justify-center">
                  <Activity className="w-6 h-6 text-yellow-600" />
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Categories */}
          <Card>
            <CardHeader>
              <CardTitle>Categorías</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {mockCategories.map((category) => {
                  const Icon = category.icon
                  return (
                    <div key={category.name} className="flex items-center justify-between">
                      <div className="flex items-center gap-3">
                        <div className={`w-10 h-10 rounded-lg bg-gray-100 flex items-center justify-center ${category.color}`}>
                          <Icon className="w-5 h-5" />
                        </div>
                        <span className="font-medium text-text">{category.name}</span>
                      </div>
                      <Badge variant="secondary">{category.count}</Badge>
                    </div>
                  )
                })}
              </div>
            </CardContent>
          </Card>

          {/* Recent Items */}
          <Card>
            <CardHeader>
              <CardTitle>Actividad Reciente</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-3">
                {mockRecentItems.map((item) => (
                  <div key={item.id} className="flex items-center justify-between py-2 border-b border-gray-100 last:border-0">
                    <div className="flex-1">
                      <p className="font-medium text-text text-sm">{item.title}</p>
                      <p className="text-xs text-text-secondary">{item.category} • {item.date}</p>
                    </div>
                    <Badge 
                      variant={item.completed ? 'success' : 'secondary'}
                      size="sm"
                    >
                      {item.completed ? 'Completado' : 'Pendiente'}
                    </Badge>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>

          {/* Habits Progress */}
          <Card>
            <CardHeader>
              <CardTitle>Progreso de Hábitos</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {mockHabits.map((habit) => (
                  <div key={habit.id} className="space-y-2">
                    <div className="flex justify-between items-center">
                      <span className="font-medium text-text text-sm">{habit.title}</span>
                      <span className="text-xs text-text-secondary">
                        {habit.currentStreak}/{habit.targetStreak} días
                      </span>
                    </div>
                    <ProgressBar 
                      value={habit.currentStreak} 
                      max={habit.targetStreak}
                      size="sm"
                      color="primary"
                    />
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  )
}
