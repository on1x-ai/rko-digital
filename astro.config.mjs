// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

import sitemap from '@astrojs/sitemap';
import robots from 'astro-robots-txt';

// https://astro.build/config
export default defineConfig({
  site: 'https://rko.digital',
  output: 'static',

  vite: {
    plugins: [tailwindcss()]
  },

  integrations: [
    sitemap(),
    robots()
  ]
});