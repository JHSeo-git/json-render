import { defineConfig } from "tsup";

export default defineConfig({
  entry: ["scripts/generate-prompt.ts"],
  format: ["esm"],
  dts: false,
  clean: true,
  outDir: "dist",
});
