import React from 'react';
import { ProfileSection } from '@/sections/Profile/ProfileSection';

export const App: React.FC = () => {
  return (
    <main className="min-h-screen bg-[#101318] text-[#F2F5F9] py-8">
      <ProfileSection />
    </main>
  );
};

export default App;
