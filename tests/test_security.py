from utils import asserts, curl


def test_path_traversal(url, document):
    response = curl.request(
        f"{url}/../../etc/passwd",
        headers={"host": "9th.fun"},
        flags=["--path-as-is"]
    )

    asserts.equalsAny(
        [403, 404],
        response.code,
        "Expected either '403 Forbidden' or '404 Not Found'; " +
        "path traversal not blocked",
        response
    )


def test_encoded_path_traversal(url, document):
    response = curl.request(
        f"{url}/%2e%2e/%2e%2e/etc/passwd",
        headers={"host": "9th.fun"},
        flags=["--path-as-is"]
    )

    asserts.equalsAny(
        [403, 404],
        response.code,
        "Expected either '403 Forbidden' or '404 Not Found'; " +
        "encoded path traversal not blocked",
        response
    )
