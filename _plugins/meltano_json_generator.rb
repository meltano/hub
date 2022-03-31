class MeltanoJsonGenerator < Jekyll::Generator
  safe true

  def generate(site)
    @site = site
    generate_json_index(site)
    plugin_types = [
      'extractors',
      'files',
      'loaders',
      'mappers',
      'orchestrators',
      'transformers',
      'utilities'
    ]
    plugin_types.each do |plugin_type|
      generate_json(site, plugin_type)
    end
  end

  def _remove_extras(plugin_variant_def)
    plugin_variant_def.delete("variants")
    plugin_variant_def.delete("singer_plugin")
    plugin_variant_def.delete("url")
    return plugin_variant_def
  end

  def _definition_from_multi_variant(plugin, variant)
    plugin_variant_def = _remove_extras(plugin.clone)
    plugin_variant_def["variant"] = variant["name"]
    plugin_variant_def["docs"] = variant["docs"]
    plugin_variant_def["pip_url"] = variant["pip_url"]
    plugin_variant_def["repo"] = variant["repo"]
    plugin_variant_def["capabilities"] = variant["capabilities"]
    plugin_variant_def["settings_group_validation"] = variant["settings_group_validation"]
    plugin_variant_def["settings"] = variant["settings"]
    return plugin_variant_def
  end

  def _definition_from_single_variant(plugin)
    return _remove_extras(plugin.clone)
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
        "ref": "#{@site.config["url"]}/meltano/api/v1/#{plugin_type}/#{plugin_name}--#{variant["name"]}.json"
      }
    end
    return variants_detail
  end

  def _get_logo_url(plugin_def)
    if plugin_def["logo_url"]
      return "#{@site.config["url"]}#{plugin_def["logo_url"]}"
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
          variant_name: {
            "ref": "#{@site.config["url"]}/meltano/api/v1/#{plugin_type}/#{plugin_name}--#{variant_name}.json"
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

  def _build_index(plugins)
    index = {}
    plugins.each do |plugin_type, plugin_defs|
      if plugin_type.start_with?("sorted_")
        next
      end

      index[plugin_type] = _build_plugin_type_index(plugin_type, plugin_defs)
    end
    return index
  end

  def generate_json(site, collection)
    plugins = site.data["meltano"][collection].values

    plugins.each do |plugin|
      if plugin.key?("variants")        
        plugin["variants"].each do |variant|
          plugin_variant_def = _definition_from_multi_variant(plugin, variant)
          generate_file(site, "/meltano/api/v1/#{collection}", "#{plugin['name']}--#{variant['name']}.json", JSON.generate(plugin_variant_def))
        end
      else
        plugin_variant_def = _definition_from_single_variant(plugin)
        generate_file(site, "/meltano/api/v1/#{collection}", "#{plugin['name']}--#{plugin['variant']}.json", JSON.generate(plugin_variant_def))
      end
    end

  end

  def generate_json_index(site)
    plugins = site.data["meltano"]

    index = _build_index(plugins)

    generate_file(site, "/meltano/api/v1", "plugin_index.json", JSON.generate(index))
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
