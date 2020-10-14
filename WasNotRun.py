from MySetupException import MySetupException
from TestCase import TestCase


class WasNotRun(TestCase):

    def setup(self):
        raise MySetupException
