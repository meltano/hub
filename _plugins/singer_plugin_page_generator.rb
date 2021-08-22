class SingerPluginPageGenerator < Jekyll::Generator
  safe true
  priority :high

  def generate(site)
    generate_pages(site, 'tap')
    generate_pages(site, 'target')
  end

  def generate_pages(site, plugin_type)
    site.data["#{plugin_type}s"].each do |plugin_name, plugin|
      plugin['variants'].each do |variant|
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
