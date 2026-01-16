"""Tests for the TypeScript bridge module."""

from pathlib import Path

import pytest
from src.json_render import generate_catalog_prompt

# Path to test fixtures
FIXTURES_DIR = Path(__file__).parent / "fixtures"
TEST_CATALOG_PATH = FIXTURES_DIR / "test-catalog.ts"


class TestGenerateCatalogPrompt:
    """Tests for generate_catalog_prompt function."""

    def test_generates_prompt_from_catalog(self):
        """Generates prompt from TypeScript catalog file."""
        prompt = generate_catalog_prompt(str(TEST_CATALOG_PATH))

        # Check that the catalog name is in the prompt
        assert "TestCatalog" in prompt

    def test_includes_component_names(self):
        """Includes component names in the prompt."""
        prompt = generate_catalog_prompt(str(TEST_CATALOG_PATH))

        assert "text" in prompt
        assert "button" in prompt

    def test_includes_component_descriptions(self):
        """Includes component descriptions in the prompt."""
        prompt = generate_catalog_prompt(str(TEST_CATALOG_PATH))

        assert "Display text content" in prompt
        assert "A clickable button" in prompt

    def test_includes_actions(self):
        """Includes action descriptions in the prompt."""
        prompt = generate_catalog_prompt(str(TEST_CATALOG_PATH))

        assert "navigate" in prompt
        assert "Navigate to URL" in prompt
        assert "alert" in prompt
        assert "Show alert message" in prompt

    def test_includes_visibility_section(self):
        """Includes visibility conditions documentation."""
        prompt = generate_catalog_prompt(str(TEST_CATALOG_PATH))

        assert "Visibility" in prompt
        assert "visible" in prompt

    def test_includes_validation_section(self):
        """Includes validation functions documentation."""
        prompt = generate_catalog_prompt(str(TEST_CATALOG_PATH))

        assert "Validation" in prompt
        assert "required" in prompt
        assert "email" in prompt

    def test_uses_custom_export_name(self):
        """Uses custom export name to find catalog."""
        # Both catalog and myCatalog export the same catalog in test-catalog.ts
        prompt = generate_catalog_prompt(
            str(TEST_CATALOG_PATH),
            export_name="myCatalog",
        )

        assert "TestCatalog" in prompt

    def test_raises_error_for_nonexistent_file(self):
        """Raises FileNotFoundError for non-existent catalog file."""
        with pytest.raises(FileNotFoundError):
            generate_catalog_prompt("/nonexistent/path/catalog.ts")

    def test_raises_error_for_missing_export(self):
        """Raises RuntimeError for missing export name."""
        with pytest.raises(RuntimeError) as exc_info:
            generate_catalog_prompt(
                str(TEST_CATALOG_PATH),
                export_name="nonExistentExport",
            )

        assert "not found" in str(exc_info.value)
