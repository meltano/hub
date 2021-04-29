class TargetPageGenerator < Jekyll::Generator
  safe true

  def generate(site)
    site.data['targets'].each do |target_name, target|
      target['variants'].each do |variant|
        if variant['primary_variant']
          page = TargetVariantPage.new(site, target_name, target, variant, variant_specific: false)
          site.pages << page
          target['url'] = page.url
        end

        page = TargetVariantPage.new(site, target_name, target, variant)
        site.pages << page
        variant['url'] = page.url
      end
    end
  end

  class TargetVariantPage < Jekyll::Page
    def initialize(site, target_name, target, variant, variant_specific: true)
      @site = site
      @base = site.source
      @dir  = "targets"

      basename = target_name
      title = target['name']
      if variant_specific
        basename += "--#{variant['name']}"
        title += " (#{variant['name']} variant)"
      end

      @basename = basename
      @ext      = '.html'
      @name     = @basename + @ext

      @data = {
        'title' => title,
        'excerpt' => target['description'],
        'variant_specific' => variant_specific,
        'target' => target,
        'variant' => variant
      }

      data.default_proc = proc do |_, key|
        site.frontmatter_defaults.find(relative_path, :targets, key)
      end
    end
  end
end
