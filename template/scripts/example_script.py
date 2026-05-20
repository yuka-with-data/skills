"""
Example utility script for a Skill template repository.

Purpose:
- Demonstrates how small helper scripts may be organized.
- Provides a simple reusable normalization example.
- Intended as a placeholder/template example only.
"""


def normalize_input(user_input: str) -> str:
    """
    Normalize basic user input formatting.
    """

    normalized = user_input.strip().lower()

    replacements = {
        "st.": "station",
        "dept": "department",
    }

    for old, new in replacements.items():
        normalized = normalized.replace(old, new)

    return normalized


def main():
    examples = [
        "  Tokyo St.  ",
        "Sales Dept",
        "Example Input",
    ]

    print("Normalized Examples:\n")

    for item in examples:
        print(f"Original:   {item}")
        print(f"Normalized: {normalize_input(item)}")
        print("-" * 30)


if __name__ == "__main__":
    main()