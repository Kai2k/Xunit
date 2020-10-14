from MySetupException import MySetupException
from TestCase import TestCase


class WasNotRun(TestCase):

    def setUp(self):
        raise MySetupException
