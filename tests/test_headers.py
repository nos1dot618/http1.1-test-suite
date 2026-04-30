from utils import curl, asserts


def testContentType(url):
    response = curl.request(url)

    asserts.contains(
        b"content-type",
        response.headers,
        "Missing content-type header",
        response
    )
