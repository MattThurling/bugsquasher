import csv
from datetime import datetime


def _format(list):
    str = ''
    for item in list:
        str += item[0] + ','
    return str[:-1]


class Report:

    def __init__(self, report_name):
        self.report_file_path = 'reports/' + report_name + ' ' + datetime.now().strftime('%d-%m-%y %H%M%S') + '.csv'

    def _write(self, mode, row):
        with open(self.report_file_path, mode, newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(row)

    def create(self):
        self._write('w', ['TEST NAME', 'RESULT', 'TIME', 'TAGS', 'PLANS'])

    def append(self, name, result, duration, tags='', plans=''):
        self._write('a', [name, result, round(duration, 4), _format(tags), _format(plans)])

    def meta(self, options, total, passed, failed, skipped, duration):
        for row in [
                ['<end of tests>'],
                [''],
                ['META'],
                ['Options', options],
                ['Total tests', total],
                ['Tests passed', passed],
                ['Tests failed', failed],
                ['Tests skipped', skipped],
                ['Total time', round(duration, 4)]
                ]:
            self._write('a', row)
