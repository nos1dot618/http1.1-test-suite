import importlib
import os
from utils.asserts import TestFailure

TEST_DIR = "tests/"
URL = "http://localhost:8080/README.md"


def runTests():
    for file in os.listdir(TEST_DIR):
        if not (file.startswith("test_") and file.endswith(".py")):
            continue

        moduleName = f"tests.{file[:-3]}"
        module = importlib.import_module(moduleName)

        for attr in dir(module):
            if attr.startswith("test"):
                testFunction = getattr(module, attr)
                try:
                    testFunction(URL)
                    print(f"[PASS] {attr}")
                except TestFailure as e:
                    print(f"[FAIL] {attr}: {e}")

                    if e.response:
                        print("#### Response ####")
                        print(e.response.text())
                        print("##################")


if __name__ == "__main__":
    runTests()
