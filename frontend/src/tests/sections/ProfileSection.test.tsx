import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { ProfileSection } from '@/sections/Profile/ProfileSection';
import * as profileService from '@/services/profileService';
import { CandidateProfile } from '@/types/profile';

vi.mock('@/services/profileService');

const mockProfile: CandidateProfile = {
  id: '123',
  full_name: 'Maria Engenheira',
  headline: 'Tech Lead',
  summary: 'Resumo da carreira',
  email: 'maria@example.com',
  phone: '11999999999',
  location: 'São Paulo, SP',
  linkedin_url: 'https://linkedin.com/in/maria',
  github_url: 'https://github.com/maria',
  portfolio_url: '',
  target_roles: ['Tech Lead'],
  work_modes: ['REMOTE'],
  base_resume_raw: '# CV Maria',
  experiences: [],
  educations: [],
  skills: [],
};

describe('ProfileSection Component', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('renders loading state initially and then shows profile data', async () => {
    vi.mocked(profileService.getProfile).mockResolvedValue(mockProfile);

    render(<ProfileSection />);

    expect(screen.getByText(/Carregando perfil do candidato.../i)).toBeInTheDocument();

    await waitFor(() => {
      expect(screen.getByDisplayValue('Maria Engenheira')).toBeInTheDocument();
      expect(screen.getByDisplayValue('Tech Lead')).toBeInTheDocument();
    });
  });

  it('submits updated profile when saving', async () => {
    vi.mocked(profileService.getProfile).mockResolvedValue(mockProfile);
    vi.mocked(profileService.saveProfile).mockResolvedValue({
      ...mockProfile,
      headline: 'Principal Engineer',
    });

    render(<ProfileSection />);

    await waitFor(() => {
      expect(screen.getByDisplayValue('Maria Engenheira')).toBeInTheDocument();
    });

    const headlineInput = screen.getByDisplayValue('Tech Lead');
    fireEvent.change(headlineInput, { target: { value: 'Principal Engineer' } });

    const submitBtn = screen.getByRole('button', { name: /Salvar alterações/i });
    fireEvent.click(submitBtn);

    await waitFor(() => {
      expect(profileService.saveProfile).toHaveBeenCalledWith(
        expect.objectContaining({
          headline: 'Principal Engineer',
        })
      );
      expect(screen.getByText(/Perfil salvo com sucesso!/i)).toBeInTheDocument();
    });
  });

  it('shows friendly offline banner with retry button when service is unavailable and recovers on retry', async () => {
    vi.mocked(profileService.getProfile).mockRejectedValueOnce(
      new profileService.ApiConnectionError()
    );

    render(<ProfileSection />);

    await waitFor(() => {
      expect(
        screen.getByText(/Serviço local indisponível. Verifique se o backend está em execução na porta 8000./i)
      ).toBeInTheDocument();
    });

    const retryBtn = screen.getByRole('button', { name: /Tentar novamente/i });
    expect(retryBtn).toBeInTheDocument();

    // Simula recuperação do backend
    vi.mocked(profileService.getProfile).mockResolvedValueOnce(mockProfile);
    fireEvent.click(retryBtn);

    await waitFor(() => {
      expect(screen.getByDisplayValue('Maria Engenheira')).toBeInTheDocument();
      expect(
        screen.queryByText(/Serviço local indisponível/i)
      ).not.toBeInTheDocument();
    });
  });
});
