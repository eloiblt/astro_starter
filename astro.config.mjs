// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

// https://astro.build/config
export default defineConfig({
  integrations: [
    starlight({
      title: "Notes",
      social: {
        github: "https://github.com/eloiblt/astro/",
      },
      pagination: false,
      editLink: {
        baseUrl: "https://github.com/eloiblt/astro/edit/master/",
      },
      customCss: [
        './src/styles/custom.css',
      ],
      sidebar: [
        {
          label: "01 - IT",
          collapsed: true,
          autogenerate: { directory: "01 - IT" },
        },
      ],
    }),
  ],
});
