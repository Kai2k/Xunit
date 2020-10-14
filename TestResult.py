class TestResult:
    def __init__(self):
        self.runCount = 0
        self.setUpFailCount = 0
        self.errorCount = 0

    def test_started(self):
        self.runCount = self.runCount + 1

    def setup_failed(self):
        self.setUpFailCount = self.setUpFailCount + 1

    def test_failed(self):
        self.errorCount = self.errorCount + 1

    def summary(self):
        return "%d run, %d failed, %d failed setups" % (self.runCount, self.errorCount, self.setUpFailCount)
