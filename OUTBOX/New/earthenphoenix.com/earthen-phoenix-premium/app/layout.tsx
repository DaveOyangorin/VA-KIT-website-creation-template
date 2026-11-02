import type { Metadata, Viewport } from 'next';
import './globals.css';
import Header from '@/components/layout/Header';
import Footer from '@/components/layout/Footer';
import SmoothScroll from '@/components/layout/SmoothScroll';
import Animator from '@/components/layout/Animator';
import PageCurtain from '@/components/layout/PageCurtain';
import Flourish from '@/components/layout/Flourish';
import { SITE_URL, asset } from '@/lib/site';

// Google Fonts (not self-hosted) so the type also loads inside sandboxed preview frames.
const FONTS = 'https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..700;1,6..96,400..700&family=Manrope:wght@400;500;600;700&display=swap';

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  icons: { icon: asset('img/ep-mark.png') },
};

export const viewport: Viewport = { themeColor: '#f6f3ee', width: 'device-width', initialScale: 1 };

// Turns on the hidden starting states for scroll motion before first paint, unless motion is reduced.
const ANIM = `try{if(!matchMedia('(prefers-reduced-motion: reduce)').matches)document.documentElement.classList.add('anim')}catch(e){}`;

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en-US" suppressHydrationWarning>
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        {/* eslint-disable-next-line @next/next/no-page-custom-font */}
        <link rel="stylesheet" href={FONTS} />
        <script dangerouslySetInnerHTML={{ __html: ANIM }} />
        <noscript><style>{`[data-reveal]{opacity:1!important;visibility:visible!important}[data-mask]{clip-path:none!important}.sw>span{transform:none!important}`}</style></noscript>
      </head>
      <body>
        <a className="skip" href="#main">Skip to content</a>
        <Header />
        <main id="main">{children}</main>
        <Footer />
        <SmoothScroll />
        <Animator />
        <PageCurtain />
        <Flourish />
      </body>
    </html>
  );
}
