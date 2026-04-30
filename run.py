import importlib
import os
from utils.asserts import TestFailure
from termcolor import colored

TEST_DIR = "tests/"
URL = "http://localhost:8080/README.md"


def log(level, color, message):
    print(f"[{colored(level.upper(), color=color)}] {message}")


def runTests():
    passCount, failCount = 0, 0

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
                    log("PASS", "green", attr)
                    passCount += 1
                except TestFailure as e:
                    log("FAIL", "red", f"{attr}: {e}")
                    if e.response:
                        print(colored(e.response, color="yellow"))
                        failCount += 1

    print("=====================================================")
    log("INFO", "blue", f"Tests Passed : {passCount}")
    log("INFO", "blue", f"Tests Failed : {failCount}")
    log("INFO", "blue", f"Total Tests  : {passCount + failCount}")


if __name__ == "__main__":
    runTests()
