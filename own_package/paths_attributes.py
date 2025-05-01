from pathlib import Path

modulskript_path = Path(__file__).parent
PROJECT_DIR = modulskript_path.parent
OUTPUT_DIR = PROJECT_DIR / "output"
SOURCE_DIR = PROJECT_DIR / "data"


def main():
    print(PROJECT_DIR)
    if SOURCE_DIR.exists() and SOURCE_DIR.is_dir():
        print(SOURCE_DIR, "Existiert")

if __name__ == '__main__':
    main()

