"""Bridge to TypeScript json-render via subprocess."""

import subprocess
from pathlib import Path

# Directory structure:
#   json-render-py/
#   ├── dist/generate-prompt.js
#   └── src/json_render/bridge.py  <- this file
_PACKAGE_ROOT = Path(__file__).parent.parent.parent  # json-render-py/
_PROJECT_ROOT = _PACKAGE_ROOT.parent  # <project-root>/

_SCRIPT_PATH = _PACKAGE_ROOT / "dist" / "generate-prompt.js"


def generate_catalog_prompt(
    catalog_path: str,
    export_name: str = "catalog",
) -> str:
    """
    Generate a catalog prompt by calling the TypeScript generateCatalogPrompt.

    Args:
        catalog_path: Absolute path to the TypeScript catalog file.
        export_name: The export name of the catalog in the file (default: "catalog").

    Returns:
        The generated prompt string.

    Raises:
        FileNotFoundError: If the catalog file or script doesn't exist.
        RuntimeError: If node is not available or the script fails.
    """
    if not _SCRIPT_PATH.exists():
        raise FileNotFoundError(
            f"Script not found: {_SCRIPT_PATH}. "
            "Please run 'pnpm build' in the json-render-py directory first."
        )

    catalog_file = Path(catalog_path)
    if not catalog_file.exists():
        raise FileNotFoundError(f"Catalog file not found: {catalog_file}")

    try:
        result = subprocess.run(
            ["node", str(_SCRIPT_PATH), str(catalog_file), export_name],
            capture_output=True,
            text=True,
            check=True,
            # Run from project root where node_modules is available
            cwd=str(_PROJECT_ROOT),
        )
    except FileNotFoundError:
        raise RuntimeError(
            "node is not available. Please install Node.js: https://nodejs.org"
        ) from None
    except subprocess.CalledProcessError as e:
        error_message = e.stderr.strip() if e.stderr else str(e)
        raise RuntimeError(f"Failed to generate prompt: {error_message}") from e

    return result.stdout.strip()
