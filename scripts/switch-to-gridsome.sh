#!/bin/bash
# Script to switch back to Gridsome setup
# This restores the original Gridsome directories and updates imports

set -e

cd "$(dirname "$0")/.."

echo "Switching back to Gridsome setup..."

# Restore Astro pages to backup
if [ -d "src/pages" ] && [ ! -d "src/pages-astro" ]; then
  echo "Backing up Astro pages to src/pages-astro..."
  mv src/pages src/pages-astro
fi

# Restore Gridsome pages
if [ -d "src/pages-gridsome" ]; then
  echo "Restoring Gridsome pages..."
  mv src/pages-gridsome src/pages
fi

# Restore Astro layouts to backup
if [ -d "src/layouts" ] && [ ! -d "src/layouts-astro" ]; then
  echo "Backing up Astro layouts to src/layouts-astro..."
  mv src/layouts src/layouts-astro
fi

# Restore Gridsome layouts
if [ -d "src/layouts-gridsome" ]; then
  echo "Restoring Gridsome layouts..."
  mv src/layouts-gridsome src/layouts
fi

# Restore Vue 3 components to backup
if [ -d "src/components" ] && [ ! -d "src/components-vue3" ]; then
  echo "Backing up Vue 3 components to src/components-vue3..."
  mv src/components src/components-vue3
fi

# Restore Gridsome components
if [ -d "src/components-gridsome" ]; then
  echo "Restoring Gridsome components..."
  mv src/components-gridsome src/components
fi

# Update imports back to -astro/-vue3 suffixes in the Astro files
echo "Updating imports in Astro backup files..."

find src/pages-astro src/layouts-astro src/components-vue3 -type f \( -name "*.astro" -o -name "*.vue" -o -name "*.ts" \) 2>/dev/null | while read file; do
  if [ -f "$file" ]; then
    # Use sed to restore import paths (macOS compatible)
    sed -i '' 's|/layouts/|/layouts-astro/|g' "$file" 2>/dev/null || true
    sed -i '' 's|/components/|/components-vue3/|g' "$file" 2>/dev/null || true
  fi
done

echo "Done! You can now run 'npm run develop' to start the Gridsome dev server."
