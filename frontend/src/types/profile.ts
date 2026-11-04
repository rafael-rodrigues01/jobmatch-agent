export type WorkMode = 'REMOTE' | 'HYBRID' | 'ON_SITE';

export type SkillCategory = 'TECHNICAL' | 'SOFT_SKILL' | 'LANGUAGE';

export interface Skill {
  name: string;
  category: SkillCategory;
  proficiency_level?: string;
  evidence?: string;
}

export interface Education {
  institution: string;
  degree: string;
  field_of_study: string;
  start_date?: string;
  end_date?: string;
  order_index?: number;
}

export interface Experience {
  company: string;
  role: string;
  location?: string;
  start_date: string;
  end_date?: string;
  is_current: boolean;
  description?: string;
  skills_used: string[];
  order_index?: number;
}

export interface CandidateProfile {
  id?: string;
  full_name: string;
  headline?: string;
  summary?: string;
  email?: string;
  phone?: string;
  location?: string;
  linkedin_url?: string;
  github_url?: string;
  portfolio_url?: string;
  target_roles: string[];
  work_modes: WorkMode[];
  base_resume_raw?: string;
  experiences: Experience[];
  educations: Education[];
  skills: Skill[];
  created_at?: string;
  updated_at?: string;
}
