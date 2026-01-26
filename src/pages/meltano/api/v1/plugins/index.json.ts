import type { APIRoute } from 'astro';
import { getPluginsApiIndex } from '../../../../../lib/data';

export const GET: APIRoute = async () => {
  const index = getPluginsApiIndex();

  return new Response(JSON.stringify(index, null, 2), {
    headers: {
      'Content-Type': 'application/json',
    },
  });
};
