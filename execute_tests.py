import options
from process import Process
import art
import list

if __name__ == '__main__':

    art.header()

    option = options.get()

    tests = option[0]
    resources = option[2]

    if tests:
        process = Process()
        process.run(tests, option[1])

    if resources:
        list.simple(option[3], resources)

