class MeltanoPluginEnricher < Jekyll::Generator
  safe true

  def generate(site)
    enrich_plugins(site, "extractors", "tap")
    enrich_plugins(site, "loaders", "target")
  end

  def enrich_plugins(site, collection, logo_type)
    site.data['meltano'][collection].each do |plugin_name, plugin|
      plugin['logo_url'] = "/assets/logos/#{logo_type}s/#{plugin_name}.png"
      plugin['url'] = "/#{collection}/#{plugin_name}"
    end
  end
end
