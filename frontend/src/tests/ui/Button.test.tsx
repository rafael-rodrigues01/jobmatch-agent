import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect, vi } from 'vitest';
import { Button } from '@/components/ui/Button';

describe('Button Component', () => {
  it('renders children correctly', () => {
    render(<Button>Salvar Perfil</Button>);
    expect(screen.getByRole('button', { name: /salvar perfil/i })).toBeInTheDocument();
  });

  it('handles click events', async () => {
    const handleClick = vi.fn();
    render(<Button onClick={handleClick}>Clique</Button>);
    await userEvent.click(screen.getByRole('button', { name: /clique/i }));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('renders disabled state and does not trigger clicks', async () => {
    const handleClick = vi.fn();
    render(<Button disabled onClick={handleClick}>Desabilitado</Button>);
    const button = screen.getByRole('button', { name: /desabilitado/i });
    expect(button).toBeDisabled();
    await userEvent.click(button);
    expect(handleClick).not.toHaveBeenCalled();
  });

  it('shows loading indicator when isLoading is true', () => {
    render(<Button isLoading>Processando</Button>);
    const button = screen.getByRole('button');
    expect(button).toBeDisabled();
    expect(button).toHaveAttribute('aria-busy', 'true');
  });
});
