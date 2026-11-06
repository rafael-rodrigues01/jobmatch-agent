import { CandidateProfile } from '@/types/profile';

const API_BASE_URL = 'http://localhost:8000/api/v1';

export class ApiConnectionError extends Error {
  constructor(message = 'Serviço local indisponível. Verifique se o backend está em execução na porta 8000.') {
    super(message);
    this.name = 'ApiConnectionError';
  }
}

export async function getProfile(): Promise<CandidateProfile | null> {
  try {
    const response = await fetch(`${API_BASE_URL}/profile`);
    if (response.status === 404) {
      return null;
    }
    if (!response.ok) {
      throw new Error(`Erro ao buscar perfil: ${response.statusText}`);
    }
    return response.json();
  } catch (err: unknown) {
    if (err instanceof TypeError || (err instanceof Error && err.message.includes('fetch'))) {
      throw new ApiConnectionError();
    }
    throw err;
  }
}

export async function saveProfile(
  profile: CandidateProfile
): Promise<CandidateProfile> {
  try {
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
  } catch (err: unknown) {
    if (err instanceof TypeError || (err instanceof Error && err.message.includes('fetch'))) {
      throw new ApiConnectionError();
    }
    throw err;
  }
}

export async function deleteProfile(): Promise<void> {
  try {
    const response = await fetch(`${API_BASE_URL}/profile`, {
      method: 'DELETE',
    });
    if (!response.ok && response.status !== 204) {
      throw new Error(`Erro ao excluir perfil: ${response.statusText}`);
    }
  } catch (err: unknown) {
    if (err instanceof TypeError || (err instanceof Error && err.message.includes('fetch'))) {
      throw new ApiConnectionError();
    }
    throw err;
  }
}
