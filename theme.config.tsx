import React from "react";
import { DocsThemeConfig } from "nextra-theme-docs";

const config: DocsThemeConfig = {
  head: (
    <>
      <meta name="google-adsense-account" content="ca-pub-7995274743017484" />
    </>
  ),
  logo: <span>doboku-note</span>,
  darkMode: false,
  // project: {
  //   link: "https://github.com/shuding/nextra-docs-template",
  // },
  // chat: {
  //   link: "https://discord.com",
  // },
  // docsRepositoryBase: "https://github.com/shuding/nextra-docs-template",
  footer: {
    text: "doboku-note.com",
  },
};

export default config;
