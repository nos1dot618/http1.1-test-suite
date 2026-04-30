import subprocess


class Response:
    def __init__(self, raw):
        self.raw = raw

        parts = raw.split(b"\r\n\r\n", 1)
        headerBlock = parts[0]
        self.body = parts[1] if len(parts) > 1 else b""
        lines = headerBlock.split(b"\r\n")

        statusLine = lines[0].split()
        self.version = statusLine[0]
        self.code = int(statusLine[1])
        self.codeString = b" ".join(statusLine[2:])

        self.headers = {}
        for line in lines[1:]:
            key, value = line.split(b":")
            self.headers[key.strip().lower()] = value.strip()

    def text(self):
        return self.raw.decode(errors="replace")

    def __str__(self):
        return f"Version: {self.version.decode(errors='replace')}\n" + \
            f"Code: {self.code} " + \
            self.codeString.decode(errors='replace') + \
            "\nHeaders:\n" + \
            "\n".join(f"* {key.decode(errors='replace')}: " +
                      f"{value.decode(errors='replace')}" for key, value
                      in self.headers.items()) + \
            "\nBody: ... <truncated>"


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
    return Response(result.stdout)
