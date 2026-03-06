import React from 'react'
import { clsx } from 'clsx'

interface ProgressBarProps {
  value: number
  max?: number
  size?: 'sm' | 'md' | 'lg'
  color?: 'primary' | 'success' | 'warning' | 'danger'
  showLabel?: boolean
  className?: string
}

export const ProgressBar: React.FC<ProgressBarProps> = ({
  value,
  max = 100,
  size = 'md',
  color = 'primary',
  showLabel = false,
  className
}) => {
  const percentage = Math.min((value / max) * 100, 100)
  
  const sizes = {
    sm: 'h-1',
    md: 'h-2',
    lg: 'h-3'
  }
  
  const colors = {
    primary: 'bg-accent',
    success: 'bg-green-500',
    warning: 'bg-yellow-500',
    danger: 'bg-red-500'
  }

  return (
    <div className={clsx('w-full', className)}>
      {showLabel && (
        <div className="flex justify-between items-center mb-1">
          <span className="text-sm text-text-secondary">Progreso</span>
          <span className="text-sm font-medium text-text">
            {Math.round(percentage)}%
          </span>
        </div>
      )}
      <div
        className={clsx(
          'w-full bg-gray-200 rounded-full overflow-hidden',
          sizes[size]
        )}
      >
        <div
          className={clsx(
            'h-full transition-all duration-300 ease-out',
            colors[color]
          )}
          style={{ width: `${percentage}%` }}
        />
      </div>
    </div>
  )
}
