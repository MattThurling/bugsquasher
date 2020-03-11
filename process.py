import subprocess
from report import Report
import test
from time import time


class Process:
    _passed = 0
    _failed = 0

    def __init__(self, options):
        self._options = options

    def _sub(self, filepath):
        proc = subprocess.Popen(['python', filepath], stdout=subprocess.PIPE)
        while True:
            line = proc.stdout.readline()
            if not line:
                break
            if '1' in line.decode('utf-8'):
                print("🚀 PASS ✅️ ")
                self._passed += 1
                return "PASS"
            else:
                print("🦟 FAIL ❌ ")
                self._failed += 1
                return "FAIL"

    def run(self, tests, report_name):
        batch_start = time()
        report = Report(report_name)
        report.create()

        for t in tests:
            test_start = time()
            test_name = t[1]
            file_name = 'tests/' + test_name + '.py'
            print('---------------------------------')
            print('>>> Running test: ' + test_name + '...')
            tags = test.tags(t[0])
            plans = test.plans(t[0])
            tag_str = ''
            for tag in tags:
                tag_str += '🏷️' + tag[0] + ' '
            if tag_str:
                print(tag_str)
            result = self._sub(file_name)
            duration = time() - test_start
            report.append(test_name, result, duration, tags, plans)
            # Abort the plan if critical tagged test fails
            if ('critical',) in tags and result == "FAIL":
                print('🚨 critical test failed - ABORT 🚨')
                break

        total = len(tests)
        skipped = total - (self._passed + self._failed)
        duration = time() - batch_start
        report.meta(
                    options=self._options,
                    total=total,
                    passed=self._passed,
                    failed=self._failed,
                    skipped=skipped,
                    duration=duration
                     )