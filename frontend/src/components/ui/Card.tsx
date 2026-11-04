import React, { HTMLAttributes, ReactNode } from 'react';

export interface CardProps extends HTMLAttributes<HTMLDivElement> {
  title?: string;
  subtitle?: string;
  actions?: ReactNode;
}

export const Card: React.FC<CardProps> = ({
  title,
  subtitle,
  actions,
  children,
  className = '',
  ...props
}) => {
  return (
    <div
      className={`bg-[#181D25] border border-[#303947] rounded-[14px] p-5 shadow-sm ${className}`}
      {...props}
    >
      {(title || actions) && (
        <div className="flex items-start justify-between gap-4 mb-4 pb-3 border-b border-[#303947]/50">
          <div>
            {title && (
              <h3 className="text-base font-semibold text-[#F2F5F9]">{title}</h3>
            )}
            {subtitle && (
              <p className="text-xs text-[#7E899B] mt-0.5">{subtitle}</p>
            )}
          </div>
          {actions && <div className="flex items-center gap-2">{actions}</div>}
        </div>
      )}
      <div>{children}</div>
    </div>
  );
};
