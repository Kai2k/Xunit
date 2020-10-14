from MyException import MyException
from MySetupException import MySetupException


class TestCase:
    def __init__(self, name):
        self.name = name

    def setup(self):
        pass

    def teardown(self):
        pass

    def run(self, result):
        result.test_started()
        if self.try_run_setup_method(result) == 1:
            return
        self.try_run_test_method(result)
        self.teardown()

    def try_run_setup_method(self, result):
        try:
            self.setup()
        except MySetupException:
            result.setup_failed()
            return 1
        return 0

    def try_run_test_method(self, result):
        try:
            method = getattr(self, self.name)
            method()
        except MyException:
            result.test_failed()
