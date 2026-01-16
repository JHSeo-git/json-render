# json-render-py

Python bridge to [json-render](https://github.com/vercel-labs/json-render) for AI prompt generation.

## Installation

```bash
pip install json-render
```

## Usage

This package provides a Python binding to call the TypeScript `@json-render/core` library.

```python
from json_render import generate_catalog_prompt

# Generate AI prompt from a TypeScript catalog file(absolute path)
prompt = generate_catalog_prompt("/absolute/path/to/catalog.ts")
print(prompt)

# With custom export name
prompt = generate_catalog_prompt("/absolute/path/to/catalog.ts", export_name="myCatalog")
```

### LangChain Integration

```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from json_render import generate_catalog_prompt

prompt = generate_catalog_prompt("/absolute/path/to/catalog.ts")

llm = ChatOpenAI(model="gpt-4o")
messages = [
    SystemMessage(content=f"Generate UI as JSON:\n{prompt}"),
    HumanMessage(content="Create a dashboard"),
]
response = llm.invoke(messages)
```

## Development

```bash
# Install dependencies
uv sync --dev

# Run tests
uv run pytest

# Lint, fix & sort imports
uv run ruff check --fix .

# Format code
uv run ruff format .
```

## License

MIT
