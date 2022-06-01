class PluginEnricher < Jekyll::Generator
  safe true
  priority :highest

  def generate(site)
    site.data['meltano_original'] = Marshal.load(Marshal.dump(site.data['meltano']))
    enrich_plugins(site, "extractor")
    enrich_plugins(site, "loader")
    enrich_plugins(site, "file")
    enrich_plugins(site, "utilitie")
    enrich_plugins(site, "transformer")
    enrich_plugins(site, "orchestrator")
  end

  def enrich_plugins(site, type_of_plugin)

    meltano_type_plural = "#{type_of_plugin}s"

    defaults = site.data['default_variants']["#{type_of_plugin}s"]
    unsorted_hash = {}
    site.data['meltano'][meltano_type_plural].each do |plugin_name, variants|
      default_variant = defaults[plugin_name]
      enrich_variants(site, variants, default_variant, meltano_type_plural)
      unsorted_hash[plugin_name] = variants[default_variant]

    end
    site.data["meltano"]["sorted_#{meltano_type_plural}"] = unsorted_hash.values.sort_by { |p| p.fetch('label', p.fetch('name')).downcase }

  end

  def add_alt_variants(variants, alt_variants)
    variants.each do |variant_name, variant_definition|
      variant_definition['alt_variants'] = alt_variants
    end
  end

  def enrich_variants(site, variants, default_variant, meltano_type_plural)
    alt_variants = []
    variants.each do |variant_name, variant_definition|
      image_name = variant_definition["name"].dup
      image_name.sub! "tap-", ""
      image_name.sub! "target-", ""

      if not variant_definition.key?("logo_url")
        variant_definition['logo_url'] = "/assets/logos/#{meltano_type_plural}/#{variant_definition["name"]}.png"
      end

      url_suffix = "#{variant_definition["name"]}--#{variant_name}"
      if variant_definition['variant'] == default_variant
        variant_definition['default'] = true
        url_suffix = "#{variant_definition["name"]}"
      end

      if meltano_type_plural == "extractors"
        url_suffix = url_suffix.delete_prefix('tap-')
        variant_definition['singer_url'] = "/taps/#{url_suffix}"
      elsif meltano_type_plural == "loaders"
        url_suffix = url_suffix.delete_prefix('target-')
        variant_definition['singer_url'] = "/targets/#{url_suffix}"
      end
      variant_definition['url'] = "/#{meltano_type_plural}/#{url_suffix}"

      variant_definition['maintainer'] ||= site.data['maintainers'][variant_definition['variant'].downcase]
    
      if variant_definition.key?("repo")
        repo_url = variant_definition['repo']
        repo_path_match = repo_url.match(%r{\Ahttps?://(?:www\.)?git(?:hub|lab)\.com/([^/]+/[^/.]+)}i)
        if repo_path_match
          repo_path = repo_path_match[1]
          variant_definition['metrics'] = site.data['metrics']['metrics'][repo_path]
        else
          puts("Unknown Git repo URL #{repo_url}")
        end
      end

      alt_variants.append(
        {
          "name" => variant_name,
          "url" => variant_definition['url'],
          "variant" => variant_definition['variant'],
          "default" => variant_definition['default']
        }
      )
    end
    add_alt_variants(variants, alt_variants)

  end
end
