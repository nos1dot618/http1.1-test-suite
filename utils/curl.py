import subprocess


def request(url,
            method="GET",
            headers=None,
            data=None,
            insecure=True,
            flags=None):

    if headers is None:
        headers = {}
    if flags is None:
        flags = []

    cmd = ["curl", "-i", "-s"]
    if insecure:
        cmd.append("-k")

    cmd += flags
    cmd += ["-X", method]

    for key, value in headers.items():
        cmd += ["-H", f"{key}: {value}"]
    if data:
        cmd += ["--data", data]

    cmd.append(url)

    result = subprocess.run(cmd, capture_output=True)
    return result.stdout
