from utils import asserts, curl


def test_version(url, document):
    response = curl.request(
        f"{url}{document}",
        headers={"host": "9th.fun"}
    )

    asserts.equals(
        b"HTTP/1.1",
        response.version,
        "Expected version 'HTTP/1.1'",
        response
    )


def test_header_body_seperator_presence(url, document):
    response = curl.request(
        f"{url}{document}",
        headers={"host": "9th.fun"}
    )

    asserts.contains(
        b"\r\n\r\n",
        response.raw,
        "Missing header-body seperator '\\r\\n\\r\\n'",
        response
    )
