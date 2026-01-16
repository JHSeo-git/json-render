#!/usr/bin/env node
import { program } from "commander";
import { generateCatalogPrompt } from "@json-render/core";
import { resolve } from "path";

program
  .name("generate-prompt")
  .description("Generate prompt from JSON-Render catalog")
  .argument("<catalog-path>", "Path to catalog file(absolute path)")
  .argument("[export-name]", "Export name", "catalog")
  .action(async (catalogPath: string, exportName: string) => {
    const absolutePath = resolve(process.cwd(), catalogPath);
    const module = await import(absolutePath);
    const catalog = module[exportName];

    if (!catalog) {
      console.error(`Export "${exportName}" not found in ${catalogPath}`);
      process.exit(1);
    }

    console.log(generateCatalogPrompt(catalog));
  });

program.parse();
