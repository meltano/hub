import type { APIRoute, GetStaticPaths } from 'astro';
import { getPluginsByType, allPluginTypes, type PluginTypePlural } from '../../../../../../lib/data';

const baseUrl = process.env.HUB_SITE_URL || 'https://hub.meltano.com';

export const getStaticPaths: GetStaticPaths = async () => {
  return allPluginTypes.map((type) => ({
    params: { type },
  }));
};

export const GET: APIRoute = async ({ params }) => {
  const pluginType = params.type as PluginTypePlural;
  const plugins = getPluginsByType(pluginType);

  const typeIndex: Record<string, {
    variants: Record<string, { ref: string }>;
    default_variant?: string;
    logo_url?: string | null;
  }> = {};

  for (const plugin of plugins) {
    const indexEntry = typeIndex[plugin.name] || { variants: {} };
    indexEntry.variants[plugin.variant] = {
      ref: `${baseUrl}/meltano/api/v1/plugins/${pluginType}/${plugin.name}--${plugin.variant}`,
    };
    if (plugin.isDefault) {
      indexEntry.default_variant = plugin.variant;
      indexEntry.logo_url = plugin.logo_url
        ? (plugin.logo_url.startsWith('http') ? plugin.logo_url : `${baseUrl}${plugin.logo_url}`)
        : null;
    }
    typeIndex[plugin.name] = indexEntry;
  }

  return new Response(JSON.stringify(typeIndex), {
    headers: {
      'Content-Type': 'application/json',
    },
  });
};
