from MyException import MyException
from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.log = ""

    def test_method(self):
        self.log = self.log + "testMethod "

    def test_broken_method(self):
        raise MyException

    def setup(self):
        self.log = "setUp "

    def teardown(self):
        self.log = self.log + "tearDown "
