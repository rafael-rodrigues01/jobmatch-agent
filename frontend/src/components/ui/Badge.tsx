import React, { HTMLAttributes } from 'react';

export type BadgeVariant = 'neutral' | 'brand' | 'success' | 'warning' | 'danger' | 'info';

export interface BadgeProps extends HTMLAttributes<HTMLSpanElement> {
  variant?: BadgeVariant;
}

const variantStyles: Record<BadgeVariant, string> = {
  neutral: 'bg-[#202733] text-[#A7B1C2] border border-[#303947]',
  brand: 'bg-[#6C8CFF]/15 text-[#6C8CFF] border border-[#6C8CFF]/30',
  success: 'bg-[#46C99A]/15 text-[#46C99A] border border-[#46C99A]/30',
  warning: 'bg-[#F2B85B]/15 text-[#F2B85B] border border-[#F2B85B]/30',
  danger: 'bg-[#FF727F]/15 text-[#FF727F] border border-[#FF727F]/30',
  info: 'bg-[#63B8F5]/15 text-[#63B8F5] border border-[#63B8F5]/30',
};

export const Badge: React.FC<BadgeProps> = ({
  children,
  variant = 'neutral',
  className = '',
  ...props
}) => {
  return (
    <span
      className={`inline-flex items-center px-2.5 py-0.5 rounded-[6px] text-xs font-medium tracking-wide ${variantStyles[variant]} ${className}`}
      {...props}
    >
      {children}
    </span>
  );
};
