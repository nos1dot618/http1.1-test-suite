from utils import asserts, curl


def test_get_root(url, document):
    response = curl.request(
        f"{url}{document}",
        headers={"host": "9th.fun"}
    )

    asserts.equals(
        200,
        response.code,
        "Expected '200 OK'",
        response
    )


def test_file_not_found(url, document):
    response = curl.request(
        f"{url}/let/there/be/light",
        headers={"host": "9th.fun"}
    )

    asserts.equals(
        404,
        response.code,
        "Expected '404 Not Found'",
        response
    )


def test_double_slash(url, document):
    response = curl.request(
        f"{url}/{document}",
        headers={"host": "9th.fun"}
    )

    asserts.equals(
        200,
        response.code,
        "Expected '200 OK'",
        response
    )
