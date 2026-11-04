import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import { Badge } from '@/components/ui/Badge';
import { Card } from '@/components/ui/Card';

describe('Badge Component', () => {
  it('renders label with appropriate styling', () => {
    render(<Badge variant="success">Atendido</Badge>);
    const badge = screen.getByText(/atendido/i);
    expect(badge).toBeInTheDocument();
  });
});

describe('Card Component', () => {
  it('renders title, subtitle and children', () => {
    render(
      <Card title="Experiências" subtitle="Histórico profissional">
        <p>Conteúdo do card</p>
      </Card>
    );
    expect(screen.getByText(/experiências/i)).toBeInTheDocument();
    expect(screen.getByText(/histórico profissional/i)).toBeInTheDocument();
    expect(screen.getByText(/conteúdo do card/i)).toBeInTheDocument();
  });
});
