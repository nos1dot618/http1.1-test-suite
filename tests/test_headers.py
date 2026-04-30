from utils import asserts, curl


def test_missing_host_header(url, document):
    response = curl.request(
        f"{url}{document}",
        headers={}
    )

    asserts.equals(
        400,
        response.code,
        "Expected '404 Bad Request'; due to missing the header 'host'",
        response
    )


def test_empty_host_header_value(url, document):
    response = curl.request(
        f"{url}{document}",
        headers={"host": ""}
    )

    asserts.equals(
        400,
        response.code,
        "Expected '404 Bad Request'; due to empty value for the header 'host'",
        response
    )


def test_content_type_header_presence(url, document):
    response = curl.request(
        f"{url}{document}",
        headers={"host": "9th.fun"}
    )

    asserts.contains(
        b"content-type",
        response.headers,
        "Missing header 'content-type'",
        response
    )


def test_content_length_header_presence(url, document):
    # TODO: HTTP/1.1 standard says that either 'content-length' or
    #       'transfer-encoding' must be present, but not both.
    # Reference: <https://www.rfc-editor.org/rfc/rfc9110.html#section-8.6-9>
    response = curl.request(
        f"{url}{document}",
        headers={"host": "9th.fun"}
    )

    asserts.contains(
        b"content-length",
        response.headers,
        "Missing header 'content-length'",
        response
    )


# TODO: Relook.
def test_connection_keep_alive(url, document):
    response = curl.request(
        f"{url}{document}",
        headers={"host": "9th.fun", "connection": "keep-alive"}
    )

    asserts.contains(
        b"connection",
        response.headers,
        "Missing header 'connection'",
        response
    )

    asserts.equals(
        b"keep-alive",
        response.headers[b"connection"].lower(),
        "Expected 'connection: keep-alive'",
        response
    )


def test_connection_close(url, document):
    response = curl.request(
        f"{url}{document}",
        headers={"host": "9th.fun", "connection": "close"}
    )

    asserts.contains(
        b"connection",
        response.headers,
        "Missing header 'connection'",
        response
    )

    asserts.equals(
        b"close",
        response.headers[b"connection"].lower(),
        "Expected 'connection: close'",
        response
    )
