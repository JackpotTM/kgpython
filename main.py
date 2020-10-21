import sys
import re

__version__ = "1.1.0"

GRAMMARS = {"асинк функция": "async def",
            "функция": "def",
            "эвейт": "await",
            "жазуу": "print",
            "импорт": "import",
            "фром": "from",
            "фор": "for",
            "пока": "while",
            "ин": "in",
            "кантип": "as",
            "стр": "str",
            "саны": "int",
            "Чын": "True",
            "Калп": "False"
            }

def get_file_name() -> str:
    try:
        name = sys.argv[1]
        return name
    except IndexError:
        raise ValueError("Bad file name")

def get_mode() -> str:
    # run - try run KGPYTHON code
    # compile - compile python to kgpython.
    try:
        mode = sys.argv[2]
    except IndexError:
        mode = "run"

    if mode not in ["compile", "run"]:
        raise ValueError("Bad mode")

    return mode

def translate(file_name: str, grammars: dict) -> str:
    with open(file_name, "r") as f:
        text = f.read()
        for k, v in grammars.items():
            text = re.sub(k, v, text)
    return text

def compile(code: str):  # noqa
    with open(f"ru{file}", "w") as f:
        pre = f"""
# TRANSLATED BY KGPYTHON {__version__}
"""
        f.write(pre + code)


if __name__ == '__main__':

    file = get_file_name()
    mode = get_mode()
    if mode == "run":
        grammars = GRAMMARS
    else:
        grammars = {v: k for k, v in GRAMMARS.items()}
    code = translate(file, grammars)

    if mode == "run":
        exec(code)
    elif mode == "compile":
        compile(code)