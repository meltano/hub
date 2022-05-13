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
      'utilities'
    ]
    # Deep copy site data for API purposes
    meltano_data = Marshal.load(Marshal.dump(site.data["meltano"]))
    taps_data = Marshal.load(Marshal.dump(site.data["taps"]))
    targets_data = Marshal.load(Marshal.dump(site.data["targets"]))
    plugins_list = _compile_plugins_list(meltano_data, taps_data, targets_data)

    plugin_index = generate_json_index(site, plugin_types, plugins_list)
    plugin_types.each do |plugin_type|
      generate_json(site, plugin_type, plugins_list)
      generate_file(site, "/meltano/api/v1/plugins/#{plugin_type}", "index", JSON.generate(plugin_index[plugin_type]))
    end
  end

  def _clean_top(plugin_variant_def)
    accepted_list = [
      "name",
      "pip_url",
      "variant",
      "namespace",
      "label",
      "description",
      "executable",
      "settings",
      "docs",
      "repo",
      "logo_url",
      "hidden",
      "settings_group_validation",
      "commands",
      "capabilities",
      "metadata",
      "schema",
      "select",
      "update",
      "dialect",
      "target_schema",
      "mappings"
    ]
    plugin_variant_def.each do |key, value|
      if !accepted_list.include? key
        plugin_variant_def.delete(key)
      end
    end
    return plugin_variant_def
  end

  def _clean_variant(variant)
    accepted_list = [
      "name",
      "pip_url",
      "variant",
      "namespace",
      "label",
      "description",
      "executable",
      "settings",
      "docs",
      "repo",
      "logo_url",
      "hidden",
      "settings_group_validation",
      "commands",
      "capabilities",
      "metadata",
      "schema",
      "select",
      "update",
      "dialect",
      "target_schema",
      "mappings"
    ]
    variant.each do |key, value|
      if !accepted_list.include? key
        variant.delete(key)
      end
    end
    return variant
  end

  def _definition_from_multi_variant(plugin, variant)
    plugin_variant_def = _clean_top(plugin.clone)
    plugin_variant_def["logo_url"] = _get_logo_url(plugin)
    variant = _clean_variant(variant)
    variant.each_key do |key|
      if key == "name"
        plugin_variant_def["variant"] = variant["name"]
      else
        plugin_variant_def[key] = variant[key]
      end
    end
    return plugin_variant_def
  end

  def _definition_from_single_variant(plugin)
    clean_plugin = _clean_top(plugin.clone)
    clean_plugin["logo_url"] = _get_logo_url(plugin)
    return clean_plugin
  end

  def _get_multi_variant_default(variants)
    default = ""
    variants.each do |variant|
      if default.empty? || variant["default"] 
        default = variant["name"]
      end
    end
    return default
  end

  def _build_multi_variant_details(plugin_def, plugin_type, plugin_name)
    variants_detail = {}
    plugin_def["variants"].each do |variant|
      variants_detail[variant["name"]] = {
        "ref": "#{@url}/meltano/api/v1/plugins/#{plugin_type}/#{plugin_name}--#{variant["name"]}"
      }
    end
    return variants_detail
  end

  def _get_logo_url(plugin_def)
    if plugin_def["logo_url"]
      return "#{@url}#{plugin_def["logo_url"]}"
    end
  end

  def _build_plugin_type_index(plugin_type, plugin_defs)
    plugin_type_index = {}
    plugin_defs.each do |plugin, plugin_def|
      plugin_index = {}
      plugin_name = plugin_def["name"]
      plugin_index["logo_url"] = _get_logo_url(plugin_def)
      plugin_index["default_variant"] = plugin_def["variant"]

      if plugin_def.key?("variants")
        plugin_index["variants"] = _build_multi_variant_details(plugin_def, plugin_type, plugin_name)
        plugin_index["default_variant"] = _get_multi_variant_default(plugin_def["variants"])
        plugin_index["logo_url"] = _get_logo_url(plugin_def)
      elsif plugin_def.key?("variant")
        variant_name = plugin_def["variant"]
        plugin_index["variants"] = {
          "#{variant_name}": {
            "ref": "#{@url}/meltano/api/v1/plugins/#{plugin_type}/#{plugin_name}--#{variant_name}"
          }
        }
      else
        plugin_index["logo_url"] = _get_logo_url(plugin_def)
        plugin_index["variants"] = {}
      end

      plugin_type_index[plugin_name] = plugin_index
    end
    return plugin_type_index
  end

  def _build_index(plugins, plugin_types)
    index = {}
    plugins.each do |plugin_type, plugin_defs|
      if plugin_types.include? plugin_type
        index[plugin_type] = _build_plugin_type_index(plugin_type, plugin_defs)
      end
    end
    return index
  end

  def _add_custom_to_list(plugins_list, plugin_data, plugin_type)
    # TODO: when an extractor/loader exists we skip the custom variants
    plugin_data.each do |tap_name, definition|
      if !plugins_list[plugin_type].key?(tap_name)
        singer_name = definition["singer_name"].clone()
        singer_name.gsub! '-', '_'
        definition["namespace"] = singer_name
        definition["name"] = definition["singer_name"]
        plugins_list[plugin_type][definition["singer_name"]] = definition
      end
    end
  end

  def _compile_plugins_list(plugins_list, taps_data, targets_data)
    _add_custom_to_list(plugins_list, taps_data, "extractors")
    _add_custom_to_list(plugins_list, targets_data, "loaders")
    
    return plugins_list
  end

  def generate_json(site, collection, plugins_list)
    plugins = plugins_list[collection].values

    plugins.each do |plugin|
      if plugin.key?("variants")        
        plugin["variants"].each do |variant|
          plugin_variant_def = _definition_from_multi_variant(plugin, variant)
          generate_file(site, "/meltano/api/v1/plugins/#{collection}", "#{plugin['name']}--#{variant['name']}", JSON.generate(plugin_variant_def))
        end
      else
        plugin_variant_def = _definition_from_single_variant(plugin)
        generate_file(site, "/meltano/api/v1/plugins/#{collection}", "#{plugin['name']}--#{plugin['variant']}", JSON.generate(plugin_variant_def))
      end
    end

  end

  def generate_json_index(site, plugin_types, plugins_list)
    index = _build_index(plugins_list, plugin_types)

    generate_file(site, "/meltano/api/v1/plugins", "index", JSON.generate(index))
    return index
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
