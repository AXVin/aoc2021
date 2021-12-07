import time

def test(solution=None):
    def wrapper(func):
        def inner(data):
            if solution is not None:
                with open("test_input.txt", "r") as file:
                    test_data = file.read()
                test_result = func(test_data)
                if test_result != solution:
                    raise ValueError(f"{func.__name__} fails test. Output {test_result} doesn't match solution {solution}!")
            start = time.time()
            ret = func(data)
            end = time.time()
            print("\u001b[38;5;244m", f"[{func.__name__} took {round(end-start, 5)}s]", "\u001b[0m")
            return ret
        return inner
    return wrapper
