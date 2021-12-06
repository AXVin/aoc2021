
def test(solution=None):
    def wrapper(func):
        def inner(data):
            if solution is not None:
                with open("test_input.txt", "r") as file:
                    test_data = file.read()
                test_result = func(test_data)
                if test_result != solution:
                    raise ValueError(f"{func.__name__} fails test. Output {test_result} doesn't match solution {solution}!")
            return func(data)
        return inner
    return wrapper
