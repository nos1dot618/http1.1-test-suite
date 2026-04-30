from utils import curl, asserts


def testContentType(url):
    response = curl.request(url)

    asserts.contains(
        b"content-type",
        response.headers,
        "Missing content-type header",
        response
    )


def testKeepAlive(url):
    response = curl.request(url, headers={"connection": "keep-alive"})

    asserts.contains(
        b"connection",
        response.headers,
        "Missing connection header",
        response
    )

    asserts.equals(
        b"keep-alive",
        response.headers[b"connection"],
        "Expected 'connection: keep-alive'",
        response
    )
