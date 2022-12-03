import typer
import httpx
import os
from datetime import datetime
from typing import Optional

app = typer.Typer()

TEMPLATE = """
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def load_file():
    with open(os.path.join(BASE_DIR, "input.txt")) as file:
        for line in file.readlines():
            yield line.strip()


def main():
    lines = list(load_file())
    print(lines)


if __name__ == "__main__":
    main()
"""

@app.command()
def generate(template: Optional[str] = "%d_%B_%Y"):
    date = datetime.now()
    dir_name = datetime.strftime(datetime.now(), template)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    with open(f"{dir_name}/input.txt", 'w') as f:
        f.write("")

    with open(f"{dir_name}/main.py", 'w') as f:
        f.write(TEMPLATE)
    
    print(f"Template generated in: ./{dir_name}")
    

if __name__ == "__main__":
    app()