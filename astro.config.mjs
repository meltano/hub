import { defineConfig } from 'astro/config';
import vue from '@astrojs/vue';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: process.env.HUB_SITE_URL || 'https://hub.meltano.com',
  srcDir: './src',
  // Use pages-astro during migration (can change back to pages after migration is complete)
  // Note: To switch to Astro, rename pages-astro to pages and pages to pages-gridsome
  integrations: [
    vue(),
    tailwind({
      configFile: './tailwind.config.js',
    }),
    sitemap(),
  ],
  build: {
    format: 'directory',
  },
  vite: {
    resolve: {
      alias: {
        '@logos': '/static/assets/logos',
      },
    },
  },
});
