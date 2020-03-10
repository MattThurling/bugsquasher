import argparse

import plan
import tag
import test
from process import Process
import art
import list


def arguments():
    # TODO: return error when option not specified
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--plan", help="specify a test plan by name")
    parser.add_argument("-T", "--test", help="specify an individual test")
    parser.add_argument("-t", "--tag", help="tag or list of tags")
    parser.add_argument("-l", "--list", help="list tests, plans or tags")

    return parser.parse_args()


if __name__ == '__main__':

    art.header()

    args = arguments()

    tests = []
    resources = []

    if args.plan:
        tests = test.get(plan=args.plan)
        report_name = 'plan ' + args.plan
    elif args.test:
        tests = test.get(name=args.test)
        report_name = 'test ' + args.test
    elif args.tag:
        tests = test.get(tag=args.tag)
        report_name = 'dynamic'
    elif args.list:
        if args.list == 'plan':
            resources = plan.get()
        elif args.list == 'test':
            resources = test.get()
        elif args.list == 'tag':
            resources = tag.get()
    else:
        tests = test.get()
        report_name = 'all'

    if tests:
        process = Process()
        process.run(tests, report_name)

    if resources:
        list.simple(args.list, resources)




