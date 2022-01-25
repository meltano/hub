[![Build Status](https://gitlab.com/meltano/hub/badges/main/pipeline.svg)](https://gitlab.com/meltano/hub/-/pipelines?ref=main)

---

## MeltanoHub

Source of MeltanoHub <https://hub.meltano.com/>.

## Development

To work locally with this project, you'll have to follow the steps below:

1. Fork this project
2. Download dependencies: `bundle install`
3. Build and preview: `bundle exec jekyll serve --livereload`
4. Add content
5. Push the commit(s) you made
6. Make an MR

Step 3 may fail if you are running Ruby 3.0.0 or above. It is best to set the local version of Ruby to 2.7.5 via `rbenv` to avoid this.

The above commands should be executed from the root directory of this project.

Read more at Jekyll's [documentation][].

[documentation]: https://jekyllrb.com/docs/home/
