import { CandidateProfile } from '@/types/profile';

const API_BASE_URL = 'http://localhost:8000/api/v1';

export async function getProfile(): Promise<CandidateProfile | null> {
  const response = await fetch(`${API_BASE_URL}/profile`);
  if (response.status === 404) {
    return null;
  }
  if (!response.ok) {
    throw new Error(`Erro ao buscar perfil: ${response.statusText}`);
  }
  return response.json();
}

export async function saveProfile(
  profile: CandidateProfile
): Promise<CandidateProfile> {
  const response = await fetch(`${API_BASE_URL}/profile`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(profile),
  });

  if (!response.ok) {
    throw new Error(`Erro ao salvar perfil: ${response.statusText}`);
  }
  return response.json();
}

export async function deleteProfile(): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/profile`, {
    method: 'DELETE',
  });
  if (!response.ok && response.status !== 204) {
    throw new Error(`Erro ao excluir perfil: ${response.statusText}`);
  }
}
