class SingerJsonGenerator < Jekyll::Generator
  safe true

  def generate(site)
    generate_json(site, 'taps')
    generate_json(site, 'targets')
  end

  def generate_json(site, collection)
    plugins = site.data[collection].values

    plugins.sort_by! { |p| p['label'] }

    plugins.each do |plugin|
      plugin['variants'].each do |variant|
        variant['maintainer'] ||= site.data['maintainers'][variant['name']]
      end
    end

    # singer/<taps/targets>.json #TODO Point this to latest version
    generate_file(site, "/singer", "#{collection}.json", JSON.generate(plugins))

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
