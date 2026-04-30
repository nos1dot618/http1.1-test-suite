from utils import curl, asserts


def testPathTraversal(url):
    if not url.endswith("/"):
        url += "/"
    url += "../../etc/passwd"
    response = curl.request(url, flags=["--path-as-is"])

    # TODO: Make it more stricter by testing the response code. This test
    #       should fail: if the request was successful, however the response
    #       body contains the 403 response code, leading to the test to pass.
    asserts.contains(b"403", response, "Path traversal not blocked", response)
