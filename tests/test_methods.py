from utils import asserts, curl, tags


@tags.tag(tags.TAG_STRICT)
def test_invalid_method(url, document):
    """
    The HTTP/1.1 specification allows the TRACE method, but it is commonly
    disabled in production environments due to security risks (e.g., request
    echoing can expose sensitive headers and enable XST attacks).
    Therefore, in strict/secure configurations, the server is expected to
    reject TRACE requests with 405 (Method Not Allowed) or 501
    (Not Implemented).
    """

    response = curl.request(
        f"{url}{document}",
        method="TRACE",
        headers={"host": "9th.fun"}
    )

    asserts.equalsAny(
        [405, 501],
        response.code,
        "Expected TRACE method rejection",
        response
    )
