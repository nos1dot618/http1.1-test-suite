class TestFailure(AssertionError):
    def __init__(self, message, response=None):
        self.response = response
        super().__init__(message)


def contains(needle, haystack, message, response=None):
    if needle not in haystack:
        raise TestFailure(message, response=response)
