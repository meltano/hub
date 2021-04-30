class PluginPageGenerator < Jekyll::Generator
  safe true

  def generate(site)
    generate_pages(site, 'taps')
    generate_pages(site, 'targets')
  end

  def generate_pages(site, collection)
    site.data[collection].each do |plugin_name, plugin|
      plugin['variants'].each do |variant|
        if variant['primary_variant']
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
      title = plugin['name']
      if variant_specific
        basename += "--#{variant['name']}"
        title += " (#{variant['name']} variant)"
      end

      @basename = basename
      @ext      = '.html'
      @name     = @basename + @ext

      @data = {
        'title' => title,
        'excerpt' => plugin['description'],
        'variant_specific' => variant_specific,
        'plugin' => plugin,
        'variant' => variant
      }

      data.default_proc = proc do |_, key|
        site.frontmatter_defaults.find(relative_path, :plugins, key)
      end
    end
  end
end
