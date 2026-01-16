from pathlib import Path

from src.json_render import generate_catalog_prompt

# absolute path to the catalog file
CATALOG_PATH = Path(__file__).parent.parent / "web" / "lib" / "catalog-ex1.ts"

# mock llm class
class llm:
    def __init__(self):
        pass

    @classmethod
    def invoke(self, prompt: str) -> str:
        print(
            f"llm.invoke:\n"
            f"{'='*100}\n"
            f"{prompt}\n"
            f"{'='*100}\n"
        )
        return "mock response"

def main():
    prompt = generate_catalog_prompt(CATALOG_PATH)
    response = llm.invoke(prompt)
    print(f"response: {response}")


if __name__ == "__main__":
    main()
