import type { APIRoute, GetStaticPaths } from 'astro';
import { loadAllPlugins, allPluginTypes, type Plugin, type PluginTypePlural } from '../../../../../../lib/data';

const baseUrl = process.env.HUB_SITE_URL || 'https://hub.meltano.com';

// Fields to exclude from the API response
const fieldsToDelete = [
  'keywords',
  'maintenance_status',
  'domain_url',
  'definition',
  'definition_rendered',
  'next_steps',
  'next_steps_rendered',
  'settings_preamble',
  'settings_preamble_rendered',
  'usage',
  'usage_rendered',
  'prereq',
  'prereq_rendered',
  'label_lowercase',
  'pluginType',
  'pluginTypePlural',
  'isDefault',
  'path',
  'metrics',
  'maintainer',
  'airbyte_name',
];

export const getStaticPaths: GetStaticPaths = async () => {
  const allPlugins = loadAllPlugins();
  return allPlugins.map((plugin) => ({
    params: {
      type: plugin.pluginTypePlural,
      nameVariant: `${plugin.name}--${plugin.variant}`,
    },
    props: { plugin },
  }));
};

export const GET: APIRoute = async ({ props }) => {
  const plugin = props.plugin as Plugin;

  // Build the API response object
  const apiPlugin: Record<string, unknown> = {};

  // Copy all fields except those to delete
  for (const [key, value] of Object.entries(plugin)) {
    if (!fieldsToDelete.includes(key)) {
      apiPlugin[key] = value;
    }
  }

  // Add logo_url with full URL if relative
  if (plugin.logo_url) {
    apiPlugin.logo_url = plugin.logo_url.startsWith('http')
      ? plugin.logo_url
      : `${baseUrl}${plugin.logo_url}`;
  }

  // Add docs URL
  apiPlugin.docs = `${baseUrl}/${plugin.pluginTypePlural}/${plugin.name}--${plugin.variant}`;

  // Clean up settings (remove rendered descriptions)
  if (apiPlugin.settings && Array.isArray(apiPlugin.settings)) {
    apiPlugin.settings = apiPlugin.settings.map((setting: Record<string, unknown>) => {
      const cleanSetting = { ...setting };
      delete cleanSetting.description_rendered;
      return cleanSetting;
    });
  }

  return new Response(JSON.stringify(apiPlugin), {
    headers: {
      'Content-Type': 'application/json',
    },
  });
};
