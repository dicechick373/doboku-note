import React from "react";
import { DocsThemeConfig } from "nextra-theme-docs";
import { useRouter } from 'next/router'

const config: DocsThemeConfig = {
  head: (
    <>
      <meta name="google-adsense-account" content="ca-pub-7995274743017484" />
    </>
  ),
  useNextSeoProps() {
    const { asPath } = useRouter()
    if (asPath !== '/') {
      return {
        titleTemplate: '%s – 土木ノート'
      }
    }
  },
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
