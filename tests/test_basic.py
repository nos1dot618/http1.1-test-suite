from utils import curl, asserts


def testGetRoot(url):
    response = curl.request(url)

    asserts.contains(b"HTTP/1.1 200", response, "Expected 200 OK", response)
    asserts.contains(b"\r\n\r\n", response, "Missing header-body seperator",
                     response)
