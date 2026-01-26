#!/bin/bash
# Script to switch from Gridsome to Astro setup
# This renames directories and updates imports

set -e

cd "$(dirname "$0")/.."

echo "Switching to Astro setup..."

# Backup Gridsome pages
if [ -d "src/pages" ] && [ ! -d "src/pages-gridsome" ]; then
  echo "Backing up Gridsome pages to src/pages-gridsome..."
  mv src/pages src/pages-gridsome
fi

# Activate Astro pages
if [ -d "src/pages-astro" ]; then
  echo "Activating Astro pages..."
  mv src/pages-astro src/pages
fi

# Backup Gridsome layouts
if [ -d "src/layouts" ] && [ ! -d "src/layouts-gridsome" ]; then
  echo "Backing up Gridsome layouts to src/layouts-gridsome..."
  mv src/layouts src/layouts-gridsome
fi

# Activate Astro layouts
if [ -d "src/layouts-astro" ]; then
  echo "Activating Astro layouts..."
  mv src/layouts-astro src/layouts
fi

# Backup Gridsome components
if [ -d "src/components" ] && [ ! -d "src/components-gridsome" ]; then
  echo "Backing up Gridsome components to src/components-gridsome..."
  mv src/components src/components-gridsome
fi

# Activate Vue 3 components
if [ -d "src/components-vue3" ]; then
  echo "Activating Vue 3 components..."
  mv src/components-vue3 src/components
fi

# Update imports in all files
echo "Updating imports..."

# Fix imports in .astro, .vue, and .ts files
find src/pages src/layouts src/components -type f \( -name "*.astro" -o -name "*.vue" -o -name "*.ts" \) 2>/dev/null | while read file; do
  if [ -f "$file" ]; then
    # Use sed to replace import paths (macOS compatible)
    sed -i '' 's|layouts-astro/|layouts/|g' "$file" 2>/dev/null || true
    sed -i '' 's|components-vue3/|components/|g' "$file" 2>/dev/null || true
    sed -i '' 's|pages-astro/|pages/|g' "$file" 2>/dev/null || true
  fi
done

echo "Done! You can now run 'npm run astro:dev' to start the Astro dev server."
