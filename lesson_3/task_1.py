import sys
from datetime import datetime


def my_write(string_text: str) -> None:
    if string_text != "\n":
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]: ")
        modified_text = timestamp + string_text
    else:
        modified_text = string_text
    original_write(modified_text)


if __name__ == "__main__":
    original_write = sys.stdout.write
    print("Change method")
    sys.stdout.write = my_write
    print("1, 2, 3")
    sys.stdout.write = original_write
    print("Change method back")
    print("1, 2, 3")
