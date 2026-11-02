import type { Metadata, Viewport } from 'next';
import { Fraunces, Hanken_Grotesk } from 'next/font/google';
import './globals.css';
import Header from '@/components/layout/Header';
import Footer from '@/components/layout/Footer';
import SmoothScroll from '@/components/layout/SmoothScroll';
import Animator from '@/components/layout/Animator';
import PageCurtain from '@/components/layout/PageCurtain';
import { SITE_URL, asset } from '@/lib/site';

const fraunces = Fraunces({ subsets: ['latin'], axes: ['SOFT', 'opsz'], style: ['normal', 'italic'], variable: '--font-fraunces', display: 'swap' });
const hanken = Hanken_Grotesk({ subsets: ['latin'], weight: ['400', '500', '600'], variable: '--font-hanken', display: 'swap' });

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  icons: { icon: asset('img/ep-mark.png') },
};

export const viewport: Viewport = { themeColor: '#0d1410', width: 'device-width', initialScale: 1 };

// Turns on the hidden starting states for scroll motion before first paint, unless motion is reduced.
const ANIM = `try{if(!matchMedia('(prefers-reduced-motion: reduce)').matches)document.documentElement.classList.add('anim')}catch(e){}`;

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en-US" className={`${fraunces.variable} ${hanken.variable}`} suppressHydrationWarning>
      <head>
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
      </body>
    </html>
  );
}
