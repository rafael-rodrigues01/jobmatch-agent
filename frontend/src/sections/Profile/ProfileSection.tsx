import React, { useEffect, useState } from 'react';
import { CandidateProfile, WorkMode } from '@/types/profile';
import { getProfile, saveProfile } from '@/services/profileService';
import { Button } from '@/components/ui/Button';
import { Input } from '@/components/ui/Input';
import { Card } from '@/components/ui/Card';
import { Badge } from '@/components/ui/Badge';

const defaultEmptyProfile: CandidateProfile = {
  full_name: '',
  headline: '',
  summary: '',
  email: '',
  phone: '',
  location: '',
  linkedin_url: '',
  github_url: '',
  portfolio_url: '',
  target_roles: [],
  work_modes: ['REMOTE'],
  base_resume_raw: '',
  experiences: [],
  educations: [],
  skills: [],
};

export const ProfileSection: React.FC = () => {
  const [profile, setProfile] = useState<CandidateProfile>(defaultEmptyProfile);
  const [loading, setLoading] = useState<boolean>(true);
  const [saving, setSaving] = useState<boolean>(false);
  const [statusMessage, setStatusMessage] = useState<{
    type: 'success' | 'error';
    text: string;
  } | null>(null);

  useEffect(() => {
    async function loadData() {
      try {
        setLoading(true);
        const data = await getProfile();
        if (data) {
          setProfile(data);
        }
      } catch (err) {
        setStatusMessage({
          type: 'error',
          text: 'Não foi possível carregar os dados do perfil.',
        });
      } finally {
        setLoading(false);
      }
    }
    loadData();
  }, []);

  const handleChange = (
    field: keyof CandidateProfile,
    value: string | WorkMode[] | string[]
  ) => {
    setProfile((prev) => ({ ...prev, [field]: value }));
  };

  const handleSave = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      setSaving(true);
      setStatusMessage(null);
      const saved = await saveProfile(profile);
      setProfile(saved);
      setStatusMessage({
        type: 'success',
        text: 'Perfil salvo com sucesso!',
      });
    } catch (err) {
      setStatusMessage({
        type: 'error',
        text: 'Erro ao salvar perfil. Tente novamente.',
      });
    } finally {
      setSaving(false);
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center p-12 text-[#A7B1C2]">
        <span className="text-sm">Carregando perfil do candidato...</span>
      </div>
    );
  }

  return (
    <form onSubmit={handleSave} className="space-y-6 max-w-4xl mx-auto p-4">
      <div className="flex items-center justify-between pb-4 border-b border-[#303947]">
        <div>
          <h1 className="text-2xl font-bold text-[#F2F5F9]">Perfil do Candidato</h1>
          <p className="text-sm text-[#A7B1C2] mt-1">
            Fonte da verdade para busca de vagas e geração de materiais.
          </p>
        </div>
        <Button type="submit" isLoading={saving}>
          Salvar alterações
        </Button>
      </div>

      {statusMessage && (
        <div
          role="alert"
          className={`p-3.5 rounded-[10px] text-sm border ${
            statusMessage.type === 'success'
              ? 'bg-[#46C99A]/10 border-[#46C99A]/30 text-[#46C99A]'
              : 'bg-[#FF727F]/10 border-[#FF727F]/30 text-[#FF727F]'
          }`}
        >
          {statusMessage.text}
        </div>
      )}

      {/* Dados Básicos */}
      <Card title="Dados Pessoais & Contato" subtitle="Informações primárias do candidato">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <Input
            label="Nome Completo"
            value={profile.full_name}
            onChange={(e) => handleChange('full_name', e.target.value)}
            required
            placeholder="Ex: Carlos Silva"
          />
          <Input
            label="Título Profissional (Headline)"
            value={profile.headline || ''}
            onChange={(e) => handleChange('headline', e.target.value)}
            placeholder="Ex: Desenvolvedor Backend Sênior"
          />
          <Input
            label="E-mail"
            type="email"
            value={profile.email || ''}
            onChange={(e) => handleChange('email', e.target.value)}
            placeholder="dev@example.com"
          />
          <Input
            label="Telefone / WhatsApp"
            value={profile.phone || ''}
            onChange={(e) => handleChange('phone', e.target.value)}
            placeholder="+55 11 99999-9999"
          />
        </div>
      </Card>

      {/* Resumo Profissional */}
      <Card title="Resumo Profissional" subtitle="Apresentação sintetizada da carreira">
        <div className="flex flex-col gap-1.5">
          <label htmlFor="summary" className="text-sm font-medium text-[#F2F5F9]">
            Resumo
          </label>
          <textarea
            id="summary"
            rows={4}
            value={profile.summary || ''}
            onChange={(e) => handleChange('summary', e.target.value)}
            className="w-full px-3.5 py-2 bg-[#181D25] border border-[#303947] rounded-[10px] text-[#F2F5F9] placeholder-[#7E899B] text-sm focus:outline-none focus:border-[#6C8CFF] focus:ring-1 focus:ring-[#6C8CFF]"
            placeholder="Descreva suas conquistas, principais competências e momento de carreira..."
          />
        </div>
      </Card>

      {/* Experiências Cadastradas */}
      <Card
        title="Experiências Profissionais"
        subtitle="Histórico com evidências e competências comprovadas"
      >
        {profile.experiences.length === 0 ? (
          <p className="text-xs text-[#7E899B] italic">Nenhuma experiência cadastrada ainda.</p>
        ) : (
          <div className="space-y-3">
            {profile.experiences.map((exp, index) => (
              <div
                key={index}
                className="p-3.5 bg-[#202733] border border-[#303947]/70 rounded-[10px] space-y-1.5"
              >
                <div className="flex items-center justify-between">
                  <h4 className="text-sm font-semibold text-[#F2F5F9]">
                    {exp.role} <span className="text-[#A7B1C2] font-normal">na</span> {exp.company}
                  </h4>
                  {exp.is_current && <Badge variant="brand">Atual</Badge>}
                </div>
                {exp.description && (
                  <p className="text-xs text-[#A7B1C2]">{exp.description}</p>
                )}
                <div className="flex flex-wrap gap-1.5 pt-1">
                  {exp.skills_used.map((skill, sIdx) => (
                    <Badge key={sIdx} variant="neutral">
                      {skill}
                    </Badge>
                  ))}
                </div>
              </div>
            ))}
          </div>
        )}
      </Card>

      {/* Competências */}
      <Card title="Competências" subtitle="Habilidades técnicas e comportamentais validadas">
        {profile.skills.length === 0 ? (
          <p className="text-xs text-[#7E899B] italic">Nenhuma competência cadastrada ainda.</p>
        ) : (
          <div className="flex flex-wrap gap-2">
            {profile.skills.map((skill, index) => (
              <Badge key={index} variant="brand">
                {skill.name} {skill.proficiency_level ? `(${skill.proficiency_level})` : ''}
              </Badge>
            ))}
          </div>
        )}
      </Card>

      {/* Currículo-Base Bruto (RF-02) */}
      <Card
        title="Currículo-Base Bruto (Markdown / Texto)"
        subtitle="Documento de referência preservado integralmente"
      >
        <div className="flex flex-col gap-1.5">
          <label htmlFor="base_resume_raw" className="text-sm font-medium text-[#F2F5F9]">
            Conteúdo Original
          </label>
          <textarea
            id="base_resume_raw"
            rows={8}
            value={profile.base_resume_raw || ''}
            onChange={(e) => handleChange('base_resume_raw', e.target.value)}
            className="w-full font-mono text-xs px-3.5 py-2.5 bg-[#181D25] border border-[#303947] rounded-[10px] text-[#F2F5F9] placeholder-[#7E899B] focus:outline-none focus:border-[#6C8CFF] focus:ring-1 focus:ring-[#6C8CFF]"
            placeholder="Cole seu currículo em formato texto ou Markdown aqui..."
          />
        </div>
      </Card>
    </form>
  );
};
