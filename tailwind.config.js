/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/components/**/*.{js,vue,ts}",
    "./src/layouts/**/*.vue",
    "./src/pages/**/*.vue",
    "./src/templates/**/*.vue",
    "./gridsome.config.js",
  ],
  // Safelist is a brute force method to get tailwind to work with `gridsome develop`
  // https://tailwindcss.com/docs/content-configuration#safelisting-classes
  // Only enable during local dev
  // safelist: [{ pattern: /.*/ }],
  theme: {
    fontSize: {
      xs: ".75rem",
      sm: ".875rem",
      base: "1rem",
      md: "1.025rem",
      lg: "1.125rem",
      xl: "1.25rem",
      "2xl": "1.5rem",
      "3xl": "1.875rem",
      "4xl": "2.25rem",
      "5xl": "3rem",
      "6xl": "4rem",
      "7xl": "5rem",
    },
    extend: {},
    // safelist: [{ pattern: /.*/, variants: ["lg", "md", "sm", "hover"] }],
  },
  // eslint-disable-next-line global-require
  plugins: [require("@tailwindcss/typography")],
};
