from TestCase import TestCase
from TestResult import TestResult
from WasNotRun import WasNotRun
from WasRun import WasRun


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert ("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert ("1 run, 0 failed, 0 failed setups" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert ("1 run, 1 failed, 0 failed setups" == result.summary())

    def testFailResultFormatted(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert ("1 run, 1 failed, 0 failed setups" == result.summary())

    def testFailedSetUpReported(self):
        test = WasNotRun("name")
        result = test.run()
        assert ("1 run, 0 failed, 1 failed setups" == result.summary())

    def testTeardownCalledGivenFailedTest(self):
        test = WasRun("testBrokenMethod")
        test.run()
        assert ("setUp tearDown " == test.log)


print(TestCaseTest("testTemplateMethod").run().summary())
print(TestCaseTest("testResult").run().summary())
print(TestCaseTest("testFailResultFormatted").run().summary())
print(TestCaseTest("testFailedResult").run().summary())
print(TestCaseTest("testFailedSetUpReported").run().summary())
print(TestCaseTest("testTeardownCalledGivenFailedTest").run().summary())