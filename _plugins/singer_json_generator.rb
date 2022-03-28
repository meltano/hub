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
      if plugin.key?("variants")
        plugin["variants"].each do |variant|
          generate_file(site, "/meltano/api/v1/#{collection}", "#{plugin['name']}--#{variant['name']}.json", JSON.generate(plugin))
        end
      else
        generate_file(site, "/meltano/api/v1/#{collection}", "#{plugin['name']}-#{plugin['variant']}.json", JSON.generate(plugin))
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
        variants_list = []
        plugin_index = {}
        if plugin_def.key?("variants")
          plugin_def["variants"].each_with_index do |variant, index|
            if index == 0
              plugin_index["default"] = variant["name"]
            end
            variants_list.append(variant["name"])

          end
        elsif plugin_def.key?("variant")
          plugin_index["default"] = plugin_def["variant"]
          variants_list = [plugin_def["variant"]]
        else
          variants_list = []
        end
        plugin_index["variants"] = variants_list
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
