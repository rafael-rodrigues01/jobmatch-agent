import React, { InputHTMLAttributes, useId } from 'react';

export interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
  helperText?: string;
}

export const Input: React.FC<InputProps> = ({
  label,
  error,
  helperText,
  id,
  className = '',
  ...props
}) => {
  const generatedId = useId();
  const inputId = id || generatedId;
  const errorId = `${inputId}-error`;
  const helperId = `${inputId}-helper`;

  return (
    <div className="flex flex-col gap-1.5 w-full">
      {label && (
        <label
          htmlFor={inputId}
          className="text-sm font-medium text-[#F2F5F9]"
        >
          {label}
        </label>
      )}
      <input
        id={inputId}
        aria-invalid={Boolean(error)}
        aria-describedby={
          error ? errorId : helperText ? helperId : undefined
        }
        className={`w-full px-3.5 py-2 bg-[#181D25] border ${
          error ? 'border-[#FF727F]' : 'border-[#303947]'
        } rounded-[10px] text-[#F2F5F9] placeholder-[#7E899B] text-sm focus:outline-none focus:border-[#6C8CFF] focus:ring-1 focus:ring-[#6C8CFF] transition-colors disabled:opacity-50 disabled:cursor-not-allowed ${className}`}
        {...props}
      />
      {error && (
        <span id={errorId} className="text-xs text-[#FF727F]">
          {error}
        </span>
      )}
      {helperText && !error && (
        <span id={helperId} className="text-xs text-[#7E899B]">
          {helperText}
        </span>
      )}
    </div>
  );
};
