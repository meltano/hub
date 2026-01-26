import type { APIRoute } from 'astro';
import { getSearchIndex } from '../../lib/data';

export const GET: APIRoute = async () => {
  const searchIndex = getSearchIndex();

  return new Response(JSON.stringify(searchIndex), {
    headers: {
      'Content-Type': 'application/json',
    },
  });
};
