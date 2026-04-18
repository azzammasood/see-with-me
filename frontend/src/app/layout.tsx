import type { Metadata } from 'next';
import './globals.css';
import { Eye, Bell, Moon, Home, User, LogOut } from 'lucide-react';

export const metadata: Metadata = {
  title: 'See With Me',
  description: 'A voice-native mobility assistant.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="flex flex-col h-screen overflow-hidden">
        {/* Top Navbar */}
        <header className="flex justify-between items-center p-6 w-full absolute top-0 z-10">
          <div className="flex items-center gap-3">
            <div className="p-2 rounded-full border border-[var(--primary)] text-[var(--primary)] hover:bg-[var(--primary)] hover:text-white transition-colors cursor-pointer">
              <Eye size={20} />
            </div>
            <h1 className="text-xl font-bold tracking-wide">SeeWithMe</h1>
          </div>
          
          <div className="flex items-center gap-5 border-l border-[var(--btn-border)] pl-5">
            <Bell size={18} className="text-gray-400 hover:text-white cursor-pointer transition-colors" />
            <Moon size={18} className="text-gray-400 hover:text-white cursor-pointer transition-colors" />
            <div className="flex items-center gap-3 ml-2">
              <div className="bg-[var(--primary)] w-8 h-8 rounded-full flex items-center justify-center text-black font-semibold text-sm">
                AU
              </div>
              <span className="text-sm font-medium text-gray-300">Ahmad Uzzam</span>
            </div>
          </div>
        </header>

        {/* Main Content Area */}
        <main className="flex-1 w-full flex items-center justify-center px-8 relative pt-20 pb-16">
          {children}
        </main>

        {/* Bottom Navbar (Optional, matches image structure vaguely) */}
        <footer className="absolute bottom-6 w-full flex justify-center gap-8 text-gray-500">
          <Home size={22} className="hover:text-[var(--primary)] cursor-pointer transition-colors" />
          <User size={22} className="hover:text-[var(--primary)] cursor-pointer transition-colors" />
          <LogOut size={22} className="hover:text-[var(--primary)] cursor-pointer transition-colors" />
        </footer>
      </body>
    </html>
  );
}
