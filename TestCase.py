from MyException import MyException
from MySetupException import MySetupException
from TestResult import TestResult


class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        result = TestResult()
        result.testStarted()
        try:
            self.setUp()
        except MySetupException:
            result.setupFailed()
            return result
        try:
            method = getattr(self, self.name)
            method()
        except MyException:
            result.testFailed()
        self.tearDown()
        return result
