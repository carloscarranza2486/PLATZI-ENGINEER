import React from 'react'
import { Dialog } from '@headlessui/react'
import { X } from 'lucide-react'

interface ModalProps {
  isOpen: boolean
  onClose: () => void
  title?: string
  children: React.ReactNode
  size?: 'sm' | 'md' | 'lg' | 'xl'
}

export const Modal: React.FC<ModalProps> = ({
  isOpen,
  onClose,
  title,
  children,
  size = 'md'
}) => {
  const sizes = {
    sm: 'max-w-md',
    md: 'max-w-lg',
    lg: 'max-w-2xl',
    xl: 'max-w-4xl'
  }

  return (
    <Dialog
      open={isOpen}
      onClose={onClose}
      className="relative z-50"
    >
      <div className="fixed inset-0 bg-black/30" aria-hidden="true" />
      
      <div className="fixed inset-0 flex items-center justify-center p-4">
        <Dialog.Panel className={`mx-auto w-full ${sizes[size]} bg-white rounded-xl shadow-xl`}>
          {(title || typeof onClose === 'function') && (
            <div className="flex items-center justify-between p-6 border-b border-gray-200">
              {title && (
                <Dialog.Title className="text-lg font-semibold text-text">
                  {title}
                </Dialog.Title>
              )}
              {onClose && (
                <button
                  onClick={onClose}
                  className="text-text-secondary hover:text-text transition-colors"
                >
                  <X className="w-5 h-5" />
                </button>
              )}
            </div>
          )}
          
          <div className="p-6">
            {children}
          </div>
        </Dialog.Panel>
      </div>
    </Dialog>
  )
}
