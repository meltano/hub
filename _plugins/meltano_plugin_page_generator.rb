class MeltanoPluginPageGenerator < Jekyll::Generator
  safe true
  priority :high

  def generate(site)
    generate_pages(site, 'extractor')
    generate_pages(site, 'loader')
  end

  def generate_pages(site, plugin_type)
    site.data['meltano']["#{plugin_type}s"].each do |plugin_name, plugin|
      plugin['variants'].each do |variant|
        if variant['default']
          page = PluginVariantPage.new(site, plugin_type, plugin_name, plugin, variant, variant_specific: false)
          unless site.pages.map(&:path).include?(page.path.sub(".html", ".md"))
            site.pages << page
          end
          plugin['url'] = page.url
        end

        page = PluginVariantPage.new(site, plugin_type, plugin_name, plugin, variant)
        unless site.pages.map(&:path).include?(page.path.sub(".html", ".md"))
          site.pages << page
        end
        variant['url'] = page.url
      end
    end
  end

  class PluginVariantPage < Jekyll::Page
    def initialize(site, plugin_type, plugin_name, plugin, variant, variant_specific: true)
      @site = site
      @base = site.source
      @dir  = "#{plugin_type}s"

      basename = plugin_name
      title = "#{plugin['label']} Meltano #{plugin_type}"
      if variant_specific
        basename += "--#{variant['name']}"
        title += " (#{variant['name']} variant)"
      end

      singer_plugin = plugin['singer_plugin']

      description =
        if plugin_type == 'extractor'
          "The open source Meltano extractor pulls data from #{plugin['label']} that can then be sent to a destination using a loader."
        else
          "The open source Meltano loader sends data into  #{plugin['label']} after it was pulled from a source using an extractor."
        end

      @basename = basename
      @ext      = '.html'
      @name     = @basename + @ext

      @data = {
        'title' => title,
        'description' => description,
        'image_url' => plugin['logo_url'],
        'variant_specific' => variant_specific,
        'plugin_type' => plugin_type,
        'plugin' => plugin,
        'variant' => variant,
      }

      data.default_proc = proc do |_, key|
        site.frontmatter_defaults.find(relative_path, :meltano_plugins, key)
      end
    end
  end
end
