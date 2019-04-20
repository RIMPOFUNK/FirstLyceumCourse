def cached(func):
    results = {}

    def decorated_func(*args, **kwargs):
        nonlocal results

        res = func(*args, **kwargs)
        results[args[0]] = res
        if "get" in kwargs and kwargs["get"]:
            return results
        return res

    return decorated_func


@cached
def fib(n, get=None):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
