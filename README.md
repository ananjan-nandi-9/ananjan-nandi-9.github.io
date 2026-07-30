# ananjan-nandi-9.github.io

Personal website of Ananjan Nandi, built with [Jekyll](https://jekyllrb.com/) and the [al-folio](https://github.com/alshedivat/al-folio) theme, hosted on GitHub Pages.

## Local development

```bash
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.

## Updating content

- **Bio / homepage:** `_pages/about.md`
- **Publications:** `_bibliography/papers.bib` (set `topic=` to group on the homepage tabs — structure, safety, human, or agents; `preview=`, `tldr=`, `code=`, `website=` control the extras). Add the new year to `years:` in `_pages/publications.md` each January.
- **News:** add a new `_news/announcement_N.md`
- **Venue badge colors:** `_data/venues.yml`
