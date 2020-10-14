class TestResult:
    def __init__(self):
        self.runCount = 0
        self.setUpFailCount = 0
        self.errorCount = 0

    def testStarted(self):
        self.runCount = self.runCount + 1

    def setupFailed(self):
        self.setUpFailCount = self.setUpFailCount + 1

    def testFailed(self):
        self.errorCount = self.errorCount + 1

    def summary(self):
        return "%d run, %d failed, %d failed setups" % (self.runCount, self.errorCount, self.setUpFailCount)
