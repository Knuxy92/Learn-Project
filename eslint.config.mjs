import js from '@eslint/js';
import globals from 'globals';
import { defineConfig } from 'eslint/config';

export default defineConfig([
  {
    files: ['**/*.js'],
    plugins: { js },
    extends: ['js/recommended'],
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',
      globals: { ...globals.node },
    },
    rules: {
      eqeqeq: ['warn', 'always'],
      'no-unused-vars': ['error', { caughtErrors: 'none' }],
      'no-useless-assignment': 'off',
    },
  },
  {
    files: ['exercises/**/*.js'],
    rules: {
      'no-unused-vars': 'off',
      'no-empty-function': 'off',
    },
  },
  {
    ignores: ['node_modules/**', '**/storage/**'],
  },
]);
