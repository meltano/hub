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
    plugin_index = generate_json_index(site, plugin_types)
    plugin_types.each do |plugin_type|
      generate_json(site, plugin_type)
      generate_file(site, "/meltano/api/v1/plugins/#{plugin_type}", "index", JSON.generate(plugin_index[plugin_type]))
    end
  end

  def _remove_extras(plugin_variant_def)
    plugin_variant_def.delete("variants")
    plugin_variant_def.delete("singer_plugin")
    plugin_variant_def.delete("url")
    return plugin_variant_def
  end

  def _clean_variant(variant)
    remove_list = [
      "maintainer",
      "hidden",
      "metrics",
      "original",
      "url",
      "default"
    ]
    remove_list.each do |key|
      variant.delete(key)
    end
    return variant
  end

  def _definition_from_multi_variant(plugin, variant)
    plugin_variant_def = _remove_extras(plugin.clone)
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
    clean_plugin = _remove_extras(plugin.clone)
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
          variant_name: {
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

  def generate_json(site, collection)
    plugins = site.data["meltano"][collection].values

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

  def generate_json_index(site, plugin_types)
    plugins = site.data["meltano"]

    index = _build_index(plugins, plugin_types)

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
