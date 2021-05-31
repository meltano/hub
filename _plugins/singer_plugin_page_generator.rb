class SingerPluginPageGenerator < Jekyll::Generator
  safe true
  priority :high

  def generate(site)
    generate_pages(site, 'taps', 'extractors')
    generate_pages(site, 'targets', 'loaders')
  end

  def generate_pages(site, collection, meltano_collection)
    site.data[collection].each do |plugin_name, plugin|
      plugin['logo_url'] = "/assets/logos/#{plugin['type']}s/#{plugin_name}.png"

      meltano_plugin = site.data['meltano'][meltano_collection][plugin_name]
      if meltano_plugin
        plugin['meltano_url'] = meltano_plugin['url']
      end

      plugin['variants'].each do |variant|
        repo_url = variant['repo']
        repo_path_match = repo_url.match(%r{\Ahttps?://(?:www\.)?git(?:hub|lab)\.com/([^/]+/[^/.]+)}i)
        if repo_path_match
          repo_path = repo_path_match[1]
          variant['metrics'] = site.data['metrics'][repo_path]
        else
          puts("Unknown Git repo URL #{repo_url}")
        end

        if variant['default']
          page = PluginVariantPage.new(site, plugin_name, plugin, variant, variant_specific: false)
          site.pages << page
          plugin['url'] = page.url
        end

        page = PluginVariantPage.new(site, plugin_name, plugin, variant)
        site.pages << page
        variant['url'] = page.url
      end
    end

    site.data["sorted_#{collection}"] = site.data[collection].values.sort_by { |p| p['label'].downcase }
  end

  class PluginVariantPage < Jekyll::Page
    def initialize(site, plugin_name, plugin, variant, variant_specific: true)
      @site = site
      @base = site.source
      @dir  = "#{plugin['type']}s"

      basename = plugin_name
      title = "#{plugin['label']} Singer #{plugin['type']}"
      if variant_specific
        basename += "--#{variant['name']}"
        title += " (#{variant['name']} variant)"
      end

      description =
        if plugin['type'] == 'tap'
          "The open source #{plugin['label']} Singer tap pulls data from the #{plugin['domain']['name']} that can then be sent to a destination using a Singer target."
        else
          "The open source #{plugin['label']} Singer target sends data into #{plugin['domain']['name']} after it was pulled from a source using a Singer tap."
        end

      @basename = basename
      @ext      = '.html'
      @name     = @basename + @ext

      @data = {
        'title' => title,
        'description' => description,
        'image_url' => plugin['logo_url'],
        'variant_specific' => variant_specific,
        'plugin' => plugin,
        'variant' => variant,
        'header' => 'singer'
      }

      data.default_proc = proc do |_, key|
        site.frontmatter_defaults.find(relative_path, :plugins, key)
      end
    end
  end
end
