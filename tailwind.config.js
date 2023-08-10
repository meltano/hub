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
    extend: {
      borderRadius: {
        none: "0",
        full: "9999px",
      },
      colors: {
        white: {
          DEFAULT: "#ffffff",
        },
        grey: {
          medium: "#B5B4BA",
        },
        green: {
          DEFAULT: "#99CE55",
        },
        transparent: {
          DEFAULT: "transparent",
        },
        blue: {
          DEFAULT: "#3A64FA",
          light: "#18C3FA",
          300: "#B1D5F8",
        },
        pink: {
          DEFAULT: "#F963BC",
        },
        purple: {
          DEFAULT: "#311772",
          10: "#E2DBFE",
          25: "#EEEBF7",
          50: "#E9E5FB",
          lila: "#DAD1FE",
          hub: "#E9E5FB",
          300: "#9A82F7",
          200: "#C5B6FF",
          100: "#E7E2FA",
        },
        black: {
          DEFAULT: "#080216",
        },
        smoke: {
          DEFAULT: "#F6F4FE",
        },
      },
      keyframes: {
        fly: {
          "0%, 100%": { transform: "translateY(0px)" },
          "25%": { transform: "translateY(30px)" },
          "40%": { transform: "translateY(20px)" },
          "75%": { transform: "translateY(40px)" },
        },
        flyx: {
          "0%, 100%": { transform: "translateX(0px)" },

          "50%": { transform: "translateX(50px)" },
          "55%": { transform: "translateX(50px)" },
        },
      },
      animation: {
        fly: "fly 8s ease-in-out infinite",
        flyx: "flyx 15s ease infinite",
      },
      opacity: {
        15: ".15",
      },
      screens: {
        "2xl": { min: "1536px" },
        xl: { min: "1280px" },
        lg: { min: "1024px" },
        md: { min: "768px" },
        sm: { min: "640px" },
      },
    },
    // safelist: [{ pattern: /.*/, variants: ["lg", "md", "sm", "hover"] }],
  },
  // eslint-disable-next-line global-require
  plugins: [require("@tailwindcss/typography")],
};
