class PluginEnricher < Jekyll::Generator
  safe true
  priority :highest

  def generate(site)
    enrich_plugins(site, "extractor")
    enrich_plugins(site, "loader")
    enrich_plugins(site, "target")
    enrich_plugins(site, "tap")
    enrich_plugins(site, "file")
    enrich_plugins(site, "utilitie")
    enrich_plugins(site, "transformer")
    enrich_plugins(site, "orchestrator")
  end

  def enrich_plugins(site, type_of_plugin)
    if type_of_plugin == 'extractor'
      singer_type = 'tap'
      meltano_type = 'extractor'
    elsif type_of_plugin == 'loader'
      singer_type = 'target'
      meltano_type = 'loader'
    elsif type_of_plugin == 'tap'
      singer_type = 'tap'
      meltano_type = 'extractor'
    elsif type_of_plugin == 'target'
      singer_type = 'target'
      meltano_type = 'loader'
    else     
      singer_type = nil
      meltano_type = type_of_plugin
    end  

    if singer_type != nil
      singer_type_plural = "#{singer_type}s"
    end
    meltano_type_plural = "#{meltano_type}s"

    if type_of_plugin == 'utiiltie'
      type_of_plugin = 'utility'
    end

    site.data['meltano'][meltano_type_plural].each do |plugin_name, plugin|
      p "plugin_name: #{plugin_name}"
      if singer_type == nil
        plugin['logo_url'] = "/assets/logos/#{meltano_type_plural}/#{plugin_name}.png"
      else
        plugin['logo_url'] = "/assets/logos/#{singer_type_plural}/#{plugin_name}.png"
      end

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

    if meltano_type_plural == 'extractors'
      site.data["meltano"]["sorted_#{meltano_type_plural}"] = site.data["meltano"][meltano_type_plural].values.sort_by { |p| p['label'].downcase }
      site.data["sorted_#{singer_type_plural}"] = site.data[singer_type_plural].values.sort_by { |p| p['label'].downcase }
    elsif meltano_type_plural == 'loaders'
        site.data["meltano"]["sorted_#{meltano_type_plural}"] = site.data["meltano"][meltano_type_plural].values.sort_by { |p| p['label'].downcase }
        site.data["sorted_#{singer_type_plural}"] = site.data[singer_type_plural].values.sort_by { |p| p['label'].downcase }
    else
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
