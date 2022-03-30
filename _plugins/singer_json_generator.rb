class SingerJsonGenerator < Jekyll::Generator
  safe true

  def generate(site)
    generate_json(site, 'taps')
    generate_json(site, 'targets')
    generate_json_plugin_index(site)
    plugin_types = [
      'dashboards',
      'extractors',
      'files',
      'loaders',
      'mappers',
      'models',
      'orchestrators',
      'transformers',
      'utilities'
    ]
    plugin_types.each do |plugin_type|
      generate_json_discovery(site, plugin_type)
    end
  end

  def generate_json_discovery(site, collection)
    plugins = site.data["meltano"][collection].values

    plugins.each do |plugin|
      plugin_variant_def = plugin.clone
      plugin_variant_def.delete("variants")
      plugin_variant_def.delete("singer_plugin")
      plugin_variant_def.delete("url")

      if plugin.key?("variants")        
        plugin["variants"].each do |variant|
          plugin_variant_def["variant"] = variant["name"]
          plugin_variant_def["docs"] = variant["docs"]
          plugin_variant_def["pip_url"] = variant["pip_url"]
          plugin_variant_def["repo"] = variant["repo"]
          plugin_variant_def["capabilities"] = variant["capabilities"]
          plugin_variant_def["settings_group_validation"] = variant["settings_group_validation"]
          plugin_variant_def["settings"] = variant["settings"]

          generate_file(site, "/meltano/api/v1/#{collection}", "#{plugin['name']}--#{variant['name']}.json", JSON.generate(plugin_variant_def))
        end
      else
        generate_file(site, "/meltano/api/v1/#{collection}", "#{plugin['name']}--#{plugin['variant']}.json", JSON.generate(plugin_variant_def))
      end
    end

  end

  def generate_json_plugin_index(site)
    plugins = site.data["meltano"]

    index = {}
    plugins.each do |plugin_type, plugin_defs|
      if plugin_type.start_with?("sorted_")
        next
      end
      plugin_type_index = {}
      plugin_defs.each do |plugin, plugin_def|
        variants_detail = {}
        plugin_index = {}
        if plugin_def.key?("variants")
          plugin_def["variants"].each do |variant|
            if variant["default"]
              plugin_index["default_variant"] = variant["name"]
              if plugin_def["logo_url"]
                plugin_index["logo_url"] = "#{site.config["url"]}#{plugin_def["logo_url"]}"
              end
            end
            variants_detail[variant["name"]] = {
              "ref": "#{site.config["url"]}/meltano/api/v1/#{plugin_type}/#{plugin_def["name"]}--#{variant["name"]}.json"
            }

          end
        elsif plugin_def.key?("variant")
          plugin_index["default_variant"] = plugin_def["variant"]
          if plugin_def["logo_url"]
            plugin_index["logo_url"] = "#{site.config["url"]}#{plugin_def["logo_url"]}"
          end
          variants_detail[plugin_def["variant"]] = {
            "ref": "#{site.config["url"]}/meltano/api/v1/#{plugin_type}/#{plugin_def["name"]}--#{plugin_def["variant"]}.json"
          }
        else
          variants_detail = {}
        end
        plugin_index["variants"] = variants_detail
        plugin_type_index[plugin_def["name"]] = plugin_index
      end
      index[plugin_type] = plugin_type_index
    end

    generate_file(site, "/meltano/api/v1", "plugin_index.json", JSON.generate(index))
  end

  def generate_json(site, collection)
    plugins = site.data[collection].values

    plugins.sort_by! { |p| p['label'].downcase }

    # singer/<taps/targets>.json
    generate_file(site, "/singer/", "#{collection}.json", JSON.generate(plugins))

    # singer/api/v1/<taps/targets>.json
    generate_file(site, "/singer/api/v1", "#{collection}.json", JSON.generate(plugins))

    plugins.each do |plugin|
      # singer/targets/bigquery.json
      generate_file(site, "/singer/#{collection}", "#{plugin['name']}.json", JSON.generate(plugin))
    end
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
