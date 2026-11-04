import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { ProfileSection } from '@/sections/Profile/ProfileSection';
import * as profileService from '@/services/profileService';
import { CandidateProfile } from '@/types/profile';

vi.mock('@/services/profileService');

const mockProfile: CandidateProfile = {
  id: 'uuid-123',
  full_name: 'Carlos Desenvolvedor',
  headline: 'Backend Engineer',
  summary: 'Especialista em microsserviços',
  email: 'carlos@example.com',
  target_roles: ['Backend Engineer'],
  work_modes: ['REMOTE'],
  base_resume_raw: '# Carlos\n\nResumo profissional...',
  experiences: [
    {
      company: 'Tech Solutions',
      role: 'Sênior',
      start_date: '2022-01-01',
      is_current: true,
      skills_used: ['Python', 'Docker'],
    },
  ],
  educations: [],
  skills: [
    {
      name: 'Python',
      category: 'TECHNICAL',
      proficiency_level: 'ADVANCED',
    },
  ],
};

describe('ProfileSection Component', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('loads and renders existing profile data', async () => {
    vi.mocked(profileService.getProfile).mockResolvedValue(mockProfile);

    render(<ProfileSection />);

    expect(screen.getByText(/carregando perfil/i)).toBeInTheDocument();

    await waitFor(() => {
      expect(screen.getByDisplayValue('Carlos Desenvolvedor')).toBeInTheDocument();
      expect(screen.getByDisplayValue('Backend Engineer')).toBeInTheDocument();
      expect(screen.getByText(/Tech Solutions/)).toBeInTheDocument();
      expect(screen.getByText(/Python \(ADVANCED\)/)).toBeInTheDocument();
    });
  });

  it('submits updated profile when saving', async () => {
    vi.mocked(profileService.getProfile).mockResolvedValue(mockProfile);
    vi.mocked(profileService.saveProfile).mockResolvedValue({
      ...mockProfile,
      full_name: 'Carlos Silva',
    });

    render(<ProfileSection />);

    await waitFor(() => {
      expect(screen.getByDisplayValue('Carlos Desenvolvedor')).toBeInTheDocument();
    });

    const nameInput = screen.getByLabelText(/nome completo/i);
    await userEvent.clear(nameInput);
    await userEvent.type(nameInput, 'Carlos Silva');

    const saveButton = screen.getByRole('button', { name: /salvar alterações/i });
    await userEvent.click(saveButton);

    await waitFor(() => {
      expect(profileService.saveProfile).toHaveBeenCalledWith(
        expect.objectContaining({
          full_name: 'Carlos Silva',
        })
      );
      expect(screen.getByText(/perfil salvo com sucesso/i)).toBeInTheDocument();
    });
  });

  it('shows error notice when profile update fails', async () => {
    vi.mocked(profileService.getProfile).mockResolvedValue(mockProfile);
    vi.mocked(profileService.saveProfile).mockRejectedValue(new Error('Falha na API'));

    render(<ProfileSection />);

    await waitFor(() => {
      expect(screen.getByDisplayValue('Carlos Desenvolvedor')).toBeInTheDocument();
    });

    const saveButton = screen.getByRole('button', { name: /salvar alterações/i });
    await userEvent.click(saveButton);

    await waitFor(() => {
      expect(screen.getByText(/erro ao salvar perfil/i)).toBeInTheDocument();
    });
  });
});
