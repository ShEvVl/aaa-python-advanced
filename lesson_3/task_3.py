from typing import Any, Callable, TypeVar
import sys


F = TypeVar("F", bound=Callable[..., Any])


def redirect_output(filepath: str) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            original_stdout = sys.stdout
            with open(filepath, "w") as f:
                sys.stdout = f
                try:
                    result = func(*args, **kwargs)
                finally:
                    sys.stdout = original_stdout
            return result

        return wrapper  # type: ignore

    return decorator


@redirect_output("./lesson_3/function_output.txt")
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num**power, end=" ")
        print()


if __name__ == "__main__":
    calculate()
