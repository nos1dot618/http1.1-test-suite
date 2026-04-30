from utils import curl, asserts


def testPathTraversal(url):
    if not url.endswith("/"):
        url += "/"

    url += "../../etc/passwd"
    response = curl.request(url, flags=["--path-as-is"])

    asserts.equals(
        403,
        response.code,
        "Expected response code '403 Forbidden'; path traversal not blocked",
        response
    )

    asserts.equals(
        b"Forbidden",
        response.codeString,
        "Expected response code '403 Forbidden'; path traversal not blocked",
        response
    )
