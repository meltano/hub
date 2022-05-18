class PluginEnricher < Jekyll::Generator
  safe true
  priority :highest

  def generate(site)
    enrich_plugins(site, "extractor", "tap")
    enrich_plugins(site, "loader", "target")
    enrich_plugins(site, "file", nil)
    enrich_plugins(site, "utilitie", nil)
    enrich_plugins(site, "transformer", nil)
    enrich_plugins(site, "orchestrator", nil)
  end

  def enrich_plugins(site, meltano_type, singer_type)
    meltano_type_plural = "#{meltano_type}s"
    singer_type_plural = "#{singer_type}s"

    site.data['meltano'][meltano_type_plural].each do |plugin_name, plugin|
      plugin['logo_url'] = "/assets/logos/#{singer_type_plural}/#{plugin_name}.png"
      plugin['url'] = "/#{meltano_type_plural}/#{plugin_name}"

      if plugin['variants']
        enrich_variants(site, plugin['variants'])
      end
    end

    if site.data[singer_type_plural]
      site.data[singer_type_plural].each do |plugin_name, plugin|
        plugin['logo_url'] = "/assets/logos/#{singer_type_plural}/#{plugin_name}.png"
  
        meltano_plugin = site.data['meltano'][meltano_type_plural][plugin_name]
        if meltano_plugin
          plugin['meltano_url'] = meltano_plugin['url']
          meltano_plugin['singer_plugin'] = plugin
        end
  
        if plugin['variants']
          enrich_variants(site, plugin['variants'])
        end
      end
    end


    if meltano_type_plural === 'extractors' or meltano_type_plural === 'loaders'
      site.data["meltano"]["sorted_#{meltano_type_plural}"] = site.data["meltano"][meltano_type_plural].values.sort_by { |p| p['label'].downcase }
      site.data["sorted_#{singer_type_plural}"] = site.data[singer_type_plural].values.sort_by { |p| p['label'].downcase }
    elsif meltano_type_plural === 'utilities' or meltano_type_plural === 'files'
      site.data['meltano']["sorted_#{meltano_type_plural}"] = site.data['meltano'][meltano_type_plural].values.sort_by { |p| p['name'].downcase }
    end
  end

  def enrich_variants(site, variants)
    variants.each_with_index do |variant, i|
      if variant['default'].nil? && i == 0
        variant['default'] = true
      end

      variant['maintainer'] ||= site.data['maintainers'][variant['name']]

      repo_url = variant['repo']
      repo_path_match = repo_url.match(%r{\Ahttps?://(?:www\.)?git(?:hub|lab)\.com/([^/]+/[^/.]+)}i)
      if repo_path_match
        repo_path = repo_path_match[1]
        variant['metrics'] = site.data['metrics']['metrics'][repo_path]
      else
        puts("Unknown Git repo URL #{repo_url}")
      end
    end
  end
end
