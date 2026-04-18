"use client";

import { Mic, Navigation, BookOpen, Search, User as UserIcon, LogOut } from 'lucide-react';

export default function Home() {
  return (
    <div className="w-full max-w-[1400px] h-full flex items-start justify-between mt-10">
      
      {/* Left Sidebar - Activities */}
      <div className="w-64 space-y-4">
        <h2 className="text-lg font-bold text-white mb-6">Activities</h2>
        
        <div className="flex flex-col gap-3">
          <ActivityCard label="Went for walking" time="SUN, 12:00 AM" />
          <ActivityCard label="Read text" time="SAT, 3:00 PM" />
          <ActivityCard label="Found water bottle" time="FRI, 5:00 PM" />
        </div>
      </div>

      {/* Center - Interactive Orb & Buttons */}
      <div className="flex flex-col items-center flex-1 mt-10">
        <div className="w-48 h-48 rounded-full animate-orb shadow-2xl shadow-[var(--primary)]/20 mb-8 flex items-center justify-center border border-[var(--primary)]/20 cursor-pointer">
          <div className="orb-wave-lines"></div>
        </div>

        <h2 className="text-xl font-bold mb-6">How can I help you?</h2>
        
        <Mic size={24} className="text-[var(--primary)] mb-8" />

        <div className="flex flex-col gap-4 w-64">
          <ActionButton label="Let's Walk" icon={<Navigation size={18} className="text-orange-400" />} />
          <ActionButton label="Read me this" icon={<BookOpen size={18} className="text-blue-300" />} />
          <ActionButton label="Find me" icon={<Search size={18} className="text-purple-400" />} />
        </div>
      </div>

      {/* Right Sidebar - Settings */}
      <div className="w-48 space-y-4 text-center right-sidebar">
        <h2 className="text-lg font-bold text-white mb-6 text-left">Settings</h2>
        
        <div className="bg-[var(--card-bg)] border border-[var(--card-border)] rounded-2xl p-6 flex flex-col items-center gap-3 hover:bg-[var(--btn-bg)] transition-colors cursor-pointer">
          <UserIcon size={24} className="text-gray-300" />
          <span className="text-sm font-semibold tracking-wide text-gray-300 uppercase">User Profile</span>
        </div>

        <div className="bg-[var(--card-bg)] border border-[var(--card-border)] rounded-2xl p-6 flex flex-col items-center gap-3 hover:bg-[var(--btn-bg)] transition-colors cursor-pointer">
          <LogOut size={24} className="text-gray-300" />
          <span className="text-sm font-semibold tracking-wide text-gray-300 uppercase">Logout</span>
        </div>
      </div>

    </div>
  );
}

function ActivityCard({ label, time }: { label: string; time: string }) {
  return (
    <div className="flex items-center justify-between text-sm py-3 px-4 bg-[var(--btn-bg)] border border-[var(--btn-border)] rounded-xl hover:border-[var(--primary)]/50 transition-colors cursor-pointer">
      <span className="font-semibold text-gray-200">{label}</span>
      <span className="text-[10px] text-gray-500 whitespace-nowrap ml-4">{time}</span>
    </div>
  );
}

function ActionButton({ label, icon }: { label: string; icon: React.ReactNode }) {
  return (
    <button className="flex items-center justify-center gap-3 w-full py-4 rounded-xl bg-[var(--card-bg)] border border-[var(--card-border)] hover:bg-[var(--btn-bg)] hover:border-[var(--primary)]/40 transition-all active:scale-95 text-sm font-bold text-gray-200 shadow-lg">
      {icon}
      {label}
    </button>
  );
}
