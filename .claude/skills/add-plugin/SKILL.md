---
name: add-plugin
description: Add one or more new plugins (taps/targets) to the Hub from their GitHub repos using hub-utils. Use when asked to add, onboard, or register missing plugins.
---

# Add plugins to the Hub

1. **Find candidates.** List the repos to add (e.g. `gh repo list <owner> --limit 200 --no-archived --json name,description,isFork`). Keep only `tap-*` / `target-*` repos that aren't forks.
2. **Find what is missing.** A plugin is missing if `_data/meltano/<extractors|loaders>/<name>/<variant>.yml` doesn't exist for that owner's variant. Also check existing variants whose `repo:` points at a renamed or transferred repo (`gh api repos/<owner>/<name> -q .full_name` shows the current location); those need a rename, not a new plugin.
3. **Create a branch** if on the default branch.
4. **Try one first:**
   ```bash
   uv run hub-utils add --repo-url https://github.com/<owner>/<name> --auto-accept
   ```
   Confirm it writes the variant file and updates `_data/default_variants.yml`.
5. **Run the rest** in a loop, logging each to a file and reporting failures. It installs each plugin, so it is slow; run it in the background.
   ```bash
   for n in <names>; do uv run hub-utils add --repo-url https://github.com/<owner>/$n --auto-accept > "$TMPDIR/$n.log" 2>&1 && echo "ok $n" || echo "FAIL $n"; done
   ```
6. **Clean up and check:** run `uv run hub-utils yamllint lint`, and review `git status`.
7. **Report** what was added, what was skipped and why, and that `--auto-accept` leaves the maintainer unset and the logo as a placeholder, so those need follow-up. Don't commit unless asked.
