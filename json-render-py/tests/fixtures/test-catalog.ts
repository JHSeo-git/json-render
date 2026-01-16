import { createCatalog } from "@json-render/core";
import { z } from "zod";

export const catalog = createCatalog({
  name: "TestCatalog",
  components: {
    text: {
      props: z.object({
        content: z.string(),
      }),
      description: "Display text content",
    },
    button: {
      props: z.object({
        label: z.string(),
        onClick: z.string().optional(),
      }),
      description: "A clickable button",
    },
  },
  actions: {
    navigate: {
      description: "Navigate to URL",
      params: z.object({
        url: z.string(),
      }),
    },
    alert: {
      description: "Show alert message",
      params: z.object({
        message: z.string(),
      }),
    },
  },
});

// Also export with a different name for testing export_name parameter
export const myCatalog = catalog;
