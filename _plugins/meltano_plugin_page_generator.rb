class MeltanoPluginPageGenerator < Jekyll::Generator
  safe true
  priority :high

  def generate(site)
    generate_pages(site, 'extractor')
    generate_pages(site, 'loader')
    generate_pages(site, 'file')
    generate_pages(site, 'utilitie')
    generate_pages(site, 'transformer')
    generate_pages(site, 'orchestrator')
  end

  def generate_pages(site, plugin_type)
    defaults = site.data['default_variants']["#{plugin_type}s"]
    site.data['meltano']["#{plugin_type}s"].each do |plugin_name, variants|
      variants.each do |variant_name, variant_definition|
        if variant_name = defaults[plugin_name]
          page = PluginVariantPage.new(site, plugin_type, plugin_name, variant_definition, variant_specific: false)
          unless site.pages.map(&:path).include?(page.path.sub(".html", ".md"))
            site.pages << page
          end
          variant_definition['url'] = page.url
        end

        page = PluginVariantPage.new(site, plugin_type, plugin_name, variant_definition)
        unless site.pages.map(&:path).include?(page.path.sub(".html", ".md"))
          site.pages << page
        end
      end
    end
  end


  class PluginVariantPage < Jekyll::Page
    def initialize(site, plugin_type, plugin_name, variant_definition, variant_specific: true)
      @site = site
      @base = site.source
      @dir  = "#{plugin_type}s"

      basename = plugin_name
      title = "#{variant_definition['label']} Meltano #{plugin_type}"
      if variant_specific
        basename += "--#{variant_definition['variant']}"
        title += " (#{variant_definition['variant']} variant)"
      end

      description =
        if plugin_type == 'extractor'
          "The open source Meltano extractor pulls data from #{variant_definition['label']} that can then be sent to a destination using a loader."
        else
          "The open source Meltano loader sends data into #{variant_definition['label']} after it was pulled from a source using an extractor."
        end

      @basename = basename
      @ext      = '.html'
      @name     = @basename + @ext

      @data = {
        'title' => title,
        'description' => description,
        'image_url' => variant_definition['logo_url'],
        'variant_specific' => variant_specific,
        'plugin_type' => plugin_type,
        'plugin' => variant_definition
      }

      data.default_proc = proc do |_, key|
        site.frontmatter_defaults.find(relative_path, :meltano_plugins, key)
      end
    end
  end
end
