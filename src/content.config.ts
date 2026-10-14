import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ 
    pattern: '**/*.{md,mdx}', 
    base: './src/content/blog' 
  }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.date(),
    author: z.string().default('Команда RKO.digital'),
    image: z.string().optional(),
    niche: z.enum([
      'it-specialisty',
      'startup', 
      'freelancers',
      'online-school',
      'ecommerce',
      'digital-agency'
    ]).optional(),
    readingTime: z.number().optional(),
  }),
});

export const collections = { blog };