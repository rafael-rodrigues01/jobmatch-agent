import { describe, it, expect, vi, beforeEach } from 'vitest';
import { getProfile, saveProfile, ApiConnectionError } from '@/services/profileService';

describe('profileService connection & error handling', () => {
  beforeEach(() => {
    vi.restoreAllMocks();
  });

  it('throws ApiConnectionError when network request fails (Failed to fetch)', async () => {
    global.fetch = vi.fn().mockRejectedValue(new TypeError('Failed to fetch'));

    await expect(getProfile()).rejects.toThrow(ApiConnectionError);
    await expect(getProfile()).rejects.toThrow(/Serviço local indisponível/);
  });

  it('returns null when profile returns 404 (not created yet)', async () => {
    global.fetch = vi.fn().mockResolvedValue({
      status: 404,
      ok: false,
    } as Response);

    const result = await getProfile();
    expect(result).toBeNull();
  });

  it('throws ApiConnectionError on save when server is offline', async () => {
    global.fetch = vi.fn().mockRejectedValue(new TypeError('Failed to fetch'));

    await expect(
      saveProfile({
        full_name: 'Dev Test',
        target_roles: [],
        work_modes: ['REMOTE'],
        experiences: [],
        educations: [],
        skills: [],
      })
    ).rejects.toThrow(ApiConnectionError);
  });
});

