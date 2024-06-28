/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    // Add paths to other apps if necessary
  ],
  theme: {
    colors: {
      primary: "#124E66",
      secondary: "#748D92",
      accent: "#D3d9d4",
      shadow: "#D3D9D4",
      background: "d3d9d4",
      text: "#333333",
      gray: "#2E3944",
      black: "#000000",
      blackLike: "#212A31",
      white: "#FFFFFF",
      whiteLike: "#f4f4f5",
      // Add dark theme colors here
      darkPrimary: "#007bff",
      darkSecondary: "#2d89ef",
      darkBackground: "#212121",
      darkText: "#ffffff",
      darkAccent: "#9e9e9e",
    },
    fontFamily: {
      brand: ["Merriweather", "sans-serif"],
      subHeading: ["Playfair", "sans-serif"],
      title: ["Open Sans", "sans-serif"],
      body: ["Lora", "sans-serif"],
    },
    extend: {},
  },
  plugins: [],
};