from utils import curl, asserts


def testContentType(url):
    response = curl.request(url)

    asserts.contains(b"content-type:", response.lower(),
                     "Missing content-type header", response)
