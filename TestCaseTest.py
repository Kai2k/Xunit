from TestCase import TestCase
from TestResult import TestResult
from TestSuite import TestSuite
from WasNotRun import WasNotRun
from WasRun import WasRun


class TestCaseTest(TestCase):

    def setup(self):
        super().setup()
        self.result = TestResult()

    def test_template_method(self):
        test = WasRun("test_method")
        test.run(self.result)
        assert ("setUp testMethod tearDown " == test.log)

    def test_result(self):
        test = WasRun("test_method")
        test.run(self.result)
        assert ("1 run, 0 failed, 0 failed setups" == self.result.summary())

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        test.run(self.result)
        assert ("1 run, 1 failed, 0 failed setups" == self.result.summary())

    def test_failed_result_formatted(self):
        self.result.test_started()
        self.result.test_failed()
        assert ("1 run, 1 failed, 0 failed setups" == self.result.summary())

    def test_failed_setup_reported(self):
        test = WasNotRun("name")
        test.run(self.result)
        assert ("1 run, 0 failed, 1 failed setups" == self.result.summary())

    def test_teardown_called_given_failed_test(self):
        test = WasRun("test_broken_method")
        test.run(self.result)
        assert ("setUp tearDown " == test.log)

    def test_suite(self):
        testee = TestSuite()
        testee.add(WasRun("test_method"))
        testee.add(WasRun("test_broken_method"))
        testee.run(self.result)
        assert ("2 run, 1 failed, 0 failed setups" == self.result.summary())


suite = TestSuite()
suite.add(TestCaseTest("test_template_method"))
suite.add(TestCaseTest("test_result"))
suite.add(TestCaseTest("test_failed_result"))
suite.add(TestCaseTest("test_failed_result_formatted"))
suite.add(TestCaseTest("test_failed_setup_reported"))
suite.add(TestCaseTest("test_teardown_called_given_failed_test"))
suite.add(TestCaseTest("test_suite"))
result = TestResult()
suite.run(result)
print(result.summary())
