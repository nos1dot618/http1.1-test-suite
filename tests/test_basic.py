from utils import curl, asserts


def testGetRoot(url):
    response = curl.request(url)

    asserts.equals(
        b"HTTP/1.1",
        response.version,
        "Expected version 'HTTP/1.1'",
        response
    )

    asserts.equals(
        200,
        response.code,
        "Expected 200 OK",
        response
    )

    asserts.contains(
        b"\r\n\r\n",
        response.raw,
        "Missing header-body seperator",
        response
    )


def testNotFound(url):
    url += "/let/there/be/light"
    response = curl.request(url)

    asserts.equals(
        404,
        response.code,
        "Expected 404 Not Found",
        response
    )
