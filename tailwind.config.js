/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/components/**/*.{js,vue,ts}",
    "./src/layouts/**/*.vue",
    "./src/pages/**/*.vue",
    "./src/templates/**/*.vue",
  ],
  // Safelist is a brute force method to get tailwind to work with `gridsome develop`
  // https://tailwindcss.com/docs/content-configuration#safelisting-classes
  // Only enable during local dev
  // safelist: [{ pattern: /.*/ }],
  theme: {
    extend: {},
  },
  plugins: [],
};
