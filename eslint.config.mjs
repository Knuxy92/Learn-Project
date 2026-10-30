import js from "@eslint/js";
import globals from "globals";
import tseslint from "typescript-eslint";
import { defineConfig } from "eslint/config";

export default defineConfig([
  {
    files: ["**/*.{js,mjs,cjs,ts,mts,cts}"],
    plugins: { js },
    extends: ["js/recommended"],
    languageOptions: {
      globals: { ...globals.browser, ...globals.node },
    },
    rules: {
      eqeqeq: ["warn", "always"],
      "no-unused-vars": ["error", { caughtErrors: "none" }],
    },
  },

  {
    files: ["curriculum/**/*.{js,ts}", "exercises/**/*.{js,ts}"],
    rules: {
      "no-useless-assignment": "off",
    },
  },

  tseslint.configs.recommended,

  {
    files: ["curriculum/**/*.{js,ts}", "exercises/**/*.{js,ts}"],
    rules: {
      "@typescript-eslint/no-unused-vars": [
        "error",
        { caughtErrors: "none" },
      ],
    },
  },
]);
