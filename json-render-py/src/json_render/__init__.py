"""json-render: Python binding for TypeScript json-render catalog prompt generation."""

from .bridge import generate_catalog_prompt

__version__ = "0.1.0"

__all__ = [
    "generate_catalog_prompt",
]
