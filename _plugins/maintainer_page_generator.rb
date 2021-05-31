class MaintainerPageGenerator < Jekyll::Generator
  safe true

  def generate(site)
    taps = site.data['taps'].values
    targets = site.data['targets'].values
    plugins = taps + targets

    plugins_by_variant_name = Hash.new { |h, k| h[k] = [] }
    plugins.each do |plugin|
      plugin['variants'].each do |variant|
        plugins_by_variant_name[variant['name']] << {
          'url' => variant['url'],
          'logo_url' => plugin['logo_url'],
          'label' => plugin['label']
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
      @dir  = "singer/maintainers"

      basename = variant_name

      @basename = basename
      @ext      = '.html'
      @name     = @basename + @ext

      @data = {
        'title' => "Connectors by #{maintainer['label']}",
        'description' => "Open source Singer taps and targets maintained by #{maintainer['label']}",
        'maintainer' => maintainer,
        'header' => 'singer'
      }

      data.default_proc = proc do |_, key|
        site.frontmatter_defaults.find(relative_path, :maintainers, key)
      end
    end
  end
end
