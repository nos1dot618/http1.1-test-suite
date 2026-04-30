class TestFailure(AssertionError):
    def __init__(self, message, response=None):
        self.response = response
        super().__init__(message)


def contains(needle, haystack, message, response=None):
    if needle not in haystack:
        raise TestFailure(message, response=response)


def equals(expected, actual, message, response=None):
    if actual != expected:
        raise TestFailure(message, response=response)


def equalsAny(expectedValues, actual, message, response=None):
    if all(actual != expected for expected in expectedValues):
        raise TestFailure(message, response=response)
