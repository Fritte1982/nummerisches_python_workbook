from pathlib import Path

modulskript_path = Path(__file__).parent
project_dir = modulskript_path.parent
OUTPUT_DIR = project_dir / "output"



def main():
    print(project_dir)

if __name__ == '__main__':
    main()

