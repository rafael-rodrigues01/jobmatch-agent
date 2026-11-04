import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect } from 'vitest';
import { Input } from '@/components/ui/Input';

describe('Input Component', () => {
  it('renders with label and helper text', () => {
    render(
      <Input
        label="Nome Completo"
        helperText="Digite seu nome conforme documentos"
        placeholder="Seu nome"
      />
    );
    expect(screen.getByLabelText(/nome completo/i)).toBeInTheDocument();
    expect(screen.getByText(/digite seu nome conforme documentos/i)).toBeInTheDocument();
  });

  it('allows user typing', async () => {
    render(<Input label="E-mail" placeholder="dev@example.com" />);
    const input = screen.getByLabelText(/e-mail/i);
    await userEvent.type(input, 'teste@dev.com');
    expect(input).toHaveValue('teste@dev.com');
  });

  it('renders error state and error message with aria-invalid', () => {
    render(
      <Input
        label="Telefone"
        error="Campo obrigatório"
      />
    );
    const input = screen.getByLabelText(/telefone/i);
    expect(input).toHaveAttribute('aria-invalid', 'true');
    expect(screen.getByText(/campo obrigatório/i)).toBeInTheDocument();
  });
});
