// @ts-check
import { defineConfig } from "astro/config";
import rehypeStripFirstH1 from "./src/plugins/rehype-strip-first-h1.mjs";
import remarkCodePairs from "./src/plugins/remark-code-pairs.mjs";
import rehypeSections from "./src/plugins/rehype-sections.mjs";

/* Shiki ธีมสีเดียวตาม Design.md — ทุกสีอ้าง token ผ่าน CSS vars (gate 48)
   kw/ตัวเลข = accent · string = ink-2 · comment = ink-3 · พื้นโปร่ง (figure จัดการเอง) */
const midnightAccent = {
  name: "midnight-accent",
  type: "dark",
  colorReplacements: {},
  colors: {
    "editor.background": "#00000000",
    "editor.foreground": "var(--color-ink)",
  },
  settings: [
    { settings: { foreground: "var(--color-ink)" } },
    {
      scope: ["keyword", "storage", "keyword.operator.expression", "constant.numeric"],
      settings: { foreground: "var(--color-accent)" },
    },
    { scope: ["string", "string.template", "constant.character"], settings: { foreground: "var(--color-ink-2)" } },
    { scope: ["comment", "punctuation.definition.comment"], settings: { foreground: "var(--color-ink-3)" } },
    { scope: ["entity.name.function", "support.function"], settings: { foreground: "var(--color-ink)" } },
  ],
};

// static output เท่านั้น — self-host / Vercel
export default defineConfig({
  output: "static",
  build: {
    assets: "assets",
  },
  markdown: {
    syntaxHighlight: "shiki",
    shikiConfig: {
      theme: midnightAccent,
    },
    remarkPlugins: [remarkCodePairs],
    rehypePlugins: [rehypeStripFirstH1, rehypeSections],
  },
});
