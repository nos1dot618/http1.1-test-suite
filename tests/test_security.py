from utils import curl, asserts


def testPathTraversal(url):
    if not url.endswith("/"):
        url += "/"

    url += "../../etc/passwd"
    response = curl.request(url, flags=["--path-as-is"])

    asserts.equalsAny(
        [403, 404],
        response.code,
        "Expected either '403 Forbidden' or '404 Not Found'; " +
        "path traversal not blocked",
        response
    )
