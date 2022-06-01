class MeltanoJsonGenerator < Jekyll::Generator
  safe true

  def generate(site)
    @url = site.config["url"]
    plugin_types = [
      'extractors',
      'files',
      'loaders',
      'mappers',
      'orchestrators',
      'transformers',
      'utilities',
      'transforms'
    ]

    # Write plugin files
    plugin_types.each do |plugin_type|
      if not site.data['meltano_original'].key?(plugin_type)
        next
      end
      site.data['meltano_original'][plugin_type].each do |plugin_name, variants|
        variants.each do |variant_name, variant_definition|
          definition = transform_definition(variant_definition)
          generate_file(site, "/meltano/api/v1/plugins/#{plugin_type}", "#{variant_definition['name']}--#{variant_name}", JSON.generate(definition))
        end
      end
    end

    # Indexes: top level and plugin type level
    top_level_index = {}
    defaults = site.data['default_variants']
    plugin_types.each do |plugin_type|
      if not site.data['meltano_original'].key?(plugin_type)
        next
      end
      plugin_type_index = {}
      site.data['meltano_original'][plugin_type].each do |plugin_name, variants|
        variant_refs = {}
        logo_url = nil
        variants.each do |variant_name, variant_definition|
          variant_refs[variant_name] = {
            "ref": "#{@url}/meltano/api/v1/plugins/#{plugin_type}/#{plugin_name}--#{variant_name}"
          }
          if defaults[plugin_type][plugin_name] == variant_name
            logo_url = _get_logo_url(variant_definition)
          end
        end
        plugin_type_index[plugin_name] = {
          "logo_url" => logo_url,
          "default_variant" => defaults[plugin_type][plugin_name],
          "variants" => variant_refs
        }
        generate_file(site, "/meltano/api/v1/plugins/#{plugin_type}", "index", JSON.generate(plugin_type_index))
      end
      top_level_index[plugin_type] = plugin_type_index
    end
    generate_file(site, "/meltano/api/v1/plugins", "index", JSON.generate(top_level_index))
  end

  def _get_logo_url(plugin_def)
    if plugin_def["logo_url"]
      return "#{@url}#{plugin_def["logo_url"]}"
    end
  end

  def transform_definition(variant_definition)
    to_delete_list = ['keywords', 'maintenance_status', 'domain_url']
    clean_copy = Marshal.load(Marshal.dump(variant_definition))
    to_delete_list.each do |attrb|
      clean_copy.delete(attrb)
    end
    clean_copy['logo_url'] = _get_logo_url(variant_definition)

    return clean_copy
  end

  def generate_file(site, dir, name, content)
    base = site.source

    file = Jekyll::StaticFile.new(site, base, dir, name)

    FileUtils.mkdir_p(File.dirname(file.path))

    File.open(file.path, "w") do |f|
      f.write(content)
    end

    unless site.static_files.map(&:path).include?(file.path)
      site.static_files << file
    end
  end
end
