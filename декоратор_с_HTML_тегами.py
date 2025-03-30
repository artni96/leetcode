from functools import wraps


def add_tag(tag):
    def wrapper(func):
        def actual_wrapper(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
        return actual_wrapper
    return wrapper


def add_div(func):
    def wrapper(*args, **kwargs):
        return f"<div>{func(*args, **kwargs)}</div>"
    return wrapper


@add_div
@add_tag("h1")
def greeting(name: str) -> str:
    return f"Hello, {name}!"


print(greeting("Artem"))
