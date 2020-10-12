from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.log = ""

    def testMethod(self):
        self.log = self.log + "testMethod "

    def testBrokenMethod(self):
        raise Exception

    def setUp(self):
        self.log = "setUp "

    def tearDown(self):
        self.log = self.log + "tearDown "
