class MaintainerPageGenerator < Jekyll::Generator
  safe true

  def generate(site)
    extractors = site.data['meltano']["extractors"].values
    loaders = site.data['meltano']["loaders"].values
    plugins = extractors + loaders

    plugins_by_variant_name = Hash.new { |h, k| h[k] = [] }
    site.data['meltano']["extractors"].each do |plugin_name, variants|
      variants.each do |variant_name, variant_definition|
        plugins_by_variant_name[variant_name] << {
          'url' => variant_definition['url'],
          'logo_url' => variant_definition['logo_url'],
          'label' => variant_definition['label']
        }
      end
    end

    maintainers = site.data['maintainers']
    maintainers.each do |variant_name, maintainer|
      maintainer['plugins'] = plugins_by_variant_name[variant_name].sort_by { |p| p['label'].downcase }

      page = MaintainerPage.new(site, variant_name, maintainer)
      site.pages << page
      maintainer['page_url'] = page.url
    end

    site.data['sorted_maintainers'] = maintainers.values.sort_by { |m| m['label'] }.sort_by { |m| -m['plugins'].length }
  end

  class MaintainerPage < Jekyll::Page
    def initialize(site, variant_name, maintainer)
      @site = site
      @base = site.source
      @dir  = "maintainers"

      basename = variant_name

      @basename = basename
      @ext      = '.html'
      @name     = @basename + @ext

      @data = {
        'title' => "Plugins by #{maintainer['label']}",
        'description' => "Open source plugins maintained by #{maintainer['label']}",
        'maintainer' => maintainer
      }

      data.default_proc = proc do |_, key|
        site.frontmatter_defaults.find(relative_path, :maintainers, key)
      end
    end
  end
end
