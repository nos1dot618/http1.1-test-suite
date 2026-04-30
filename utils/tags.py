TAG_STRICT = "strict"


def tag(*tags):
    def decorator(func):
        existing = getattr(func, "_tags", set())
        func._tags = existing.union(tags)
        return func
    return decorator
