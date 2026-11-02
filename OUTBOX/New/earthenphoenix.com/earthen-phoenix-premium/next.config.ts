import type { NextConfig } from 'next';
import path from 'node:path';

// EP_PREVIEW=1 builds a flat, relative-path copy for previews (see scripts/build-preview.mjs).
const preview = process.env.EP_PREVIEW === '1';

const config: NextConfig = {
  output: 'export',
  trailingSlash: false,
  images: { unoptimized: true },
  assetPrefix: preview ? '.' : undefined,
  env: { NEXT_PUBLIC_EP_PREVIEW: preview ? '1' : '0' },
  reactStrictMode: true,
  turbopack: { root: path.resolve(__dirname) },
};

export default config;
