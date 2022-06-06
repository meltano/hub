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
        if variant_name == defaults[plugin_name]
          page = register_pages(site, plugin_type, plugin_name, variant_definition, false)
          variant_definition['url'] = page.url
        end

        page = register_pages(site, plugin_type, plugin_name, variant_definition, true)
      end
    end
  end

  def register_pages(site, plugin_type, plugin_name, variant_definition, variant_specific)
    if plugin_type == 'extractor'
      page = PluginVariantPage.new(site, 'tap', plugin_name.delete_prefix('tap-'), variant_definition, variant_specific)
      unless site.pages.map(&:path).include?(page.path.sub(".html", ".md"))
        site.pages << page
      end
      page = PluginVariantPage.new(site, plugin_type, plugin_name.delete_prefix('tap-'), variant_definition, variant_specific)
      unless site.pages.map(&:path).include?(page.path.sub(".html", ".md"))
        site.pages << page
      end
    elsif plugin_type == 'loader'
      page = PluginVariantPage.new(site, 'target', plugin_name.delete_prefix('target-'), variant_definition, variant_specific)
      unless site.pages.map(&:path).include?(page.path.sub(".html", ".md"))
        site.pages << page
      end
      page = PluginVariantPage.new(site, plugin_type, plugin_name.delete_prefix('target-'), variant_definition, variant_specific)
      unless site.pages.map(&:path).include?(page.path.sub(".html", ".md"))
        site.pages << page
      end
    else
      page = PluginVariantPage.new(site, plugin_type, plugin_name, variant_definition, variant_specific)
      unless site.pages.map(&:path).include?(page.path.sub(".html", ".md"))
        site.pages << page
      end
    end


    return page
  end

  class PluginVariantPage < Jekyll::Page
    def initialize(site, plugin_type, plugin_name, variant_definition, variant_specific)
      @site = site
      @base = site.source
      if plugin_type == 'tap'
        singular_plugin_type = plugin_type
        plural_plugin_type = "taps"
        @dir  = plural_plugin_type
        variant_definition = Marshal.load(Marshal.dump(variant_definition))
        variant_definition['url'] = "/taps/#{plugin_name}"
        title = "#{variant_definition['label']} Singer #{plugin_type}"
        is_singer = true
        meltano_type = "extractors"
      elsif plugin_type == 'target'
        singular_plugin_type = plugin_type
        plural_plugin_type   = "targets"
        @dir  = plural_plugin_type
        variant_definition = Marshal.load(Marshal.dump(variant_definition))
        variant_definition['url'] = "/targets/#{plugin_name}"
        title = "#{variant_definition['label']} Singer #{plugin_type}"
        is_singer = true
        meltano_type = "loaders"
      else
        singular_plugin_type = plugin_type

        plural_plugin_type = "#{plugin_type}s"
        @dir  = plural_plugin_type
        title = "#{variant_definition['label']} Meltano #{plugin_type}"
        if plugin_type == "utilitie"
          singular_plugin_type = "utility"
          title = "#{variant_definition['label']} Meltano #{singular_plugin_type}"
        end
        is_singer = false
        meltano_type = plural_plugin_type
      end

      basename = plugin_name
      if variant_specific
        basename += "--#{variant_definition['variant']}"
        title += " (#{variant_definition['variant']} variant)"
      end

      if plugin_type == 'extractor'
        page_topic = "The `#{variant_definition['name']}` [Meltano extractor](https://docs.meltano.com/concepts/plugins#extractors) pulls data from [#{variant_definition['label']}](#{variant_definition['domain_url']}) that can then be sent to a destination using a [loader](/loaders)."
        next_steps = """Follow the remaining steps of the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Select entities and attributes to extract](https://docs.meltano.com/getting-started.html#select-entities-and-attributes-to-extract)
2. [Add a loader to send data to a destination](https://docs.meltano.com/getting-started.html#add-a-loader-to-send-data-to-a-destination)
3. [Run a data integration (EL) pipeline](https://docs.meltano.com/getting-started.html#run-a-data-integration-el-pipeline)

If you run into any issues, [learn how to get help](#looking-for-help)."""
      elsif plugin_type == 'loader'
        page_topic = "The `#{variant_definition['name']}` [Meltano loader](https://docs.meltano.com/concepts/plugins#loaders) sends data into [#{variant_definition['label']}](#{variant_definition['domain_url']}) after it was pulled from a source using an [extractor](/extractors)."
        next_steps = """Follow the remaining steps of the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Run a data integration (EL) pipeline](https://docs.meltano.com/getting-started.html#run-a-data-integration-el-pipeline)

If you run into any issues, [learn how to get help](#looking-for-help)."""
      elsif plugin_type == 'tap'
        page_topic = "The `#{variant_definition['name']}` [Singer tap](/singer/taps) pulls data from [#{variant_definition['label']}](#{variant_definition['domain_url']}) that can then be sent to a destination using a [Singer target](/singer/targets)."
      elsif plugin_type == 'target'
        page_topic = "The `#{variant_definition['name']}` [Singer target](/singer/targets) sends data into [#{variant_definition['label']}](#{variant_definition['domain_url']}) after it was pulled from a source using a [Singer tap](/singer/taps)."
      elsif plugin_type == 'transformer'
        page_topic = "The `#{variant_definition['name']}` [transformer](https://docs.meltano.com/guide/transformation) uses SQL to transform data stored in your warehouse."
        next_steps = """Follow the remaining steps of the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Transform loaded data for analysis](https://docs.meltano.com/getting-started.html#transform-loaded-data-for-analysis)

If you run into any issues, [learn how to get help](#looking-for-help)."""
      elsif plugin_type == 'orchestrator'
        page_topic = "The `#{variant_definition['name']}` [orchestrator](https://docs.meltano.com/concepts/plugins#orchestrators) allows for workflows to be programmatically authored, scheduled, and monitored."
        next_steps = """1. Use the [meltano schedule](https://docs.meltano.com/reference/command-line-interface#schedule) command to create pipeline schedules in your project, to be run by Airflow.
2. Start Scheduler and Webserver or execute Airflow commands directly using the instructions in [the Meltano docs](https://docs.meltano.com/guide/orchestration#starting-the-airflow-scheduler).

If you run into any issues, [learn how to get help](#looking-for-help).
"""
      elsif plugin_type == 'file'
        page_topic = "The `#{variant_definition['name']}` [file bundle](https://docs.meltano.com/concepts/plugins#file-bundles) #{variant_definition['definition']}"
        next_steps = "#{variant_definition['next_steps']}"
      elsif plugin_type == 'utilitie'
        page_topic = "The `#{variant_definition['name']}` [utility](https://docs.meltano.com/concepts/plugins#utilities) #{variant_definition['definition']}"
        next_steps = "#{variant_definition['next_steps']}"
      else
        page_topic = "This is the default text."
      end

      @basename = basename
      @ext      = '.html'
      @name     = @basename + @ext

      @data = {
        'title' => title,
        'page_topic' => page_topic,
        'image_url' => variant_definition['logo_url'],
        'variant_specific' => variant_specific,
        'plugin_type' => plugin_type,
        'singular_plugin_type' => singular_plugin_type,
        'plural_plugin_type' => plural_plugin_type,
        'plugin' => variant_definition,
        'plugin_name_no_prefix' => plugin_name,
        'is_singer' => is_singer,
        'meltano_type' => meltano_type,
        'next_steps' => next_steps
      }

      data.default_proc = proc do |_, key|
        site.frontmatter_defaults.find(relative_path, :meltano_plugins, key)
      end
    end
  end
end
