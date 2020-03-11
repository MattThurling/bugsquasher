import argparse

import plan
import tag
import test


def arguments():
    """
    Adds custom arguments for the script and parses the user input
    :return: arguments object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--plan", help="specify a test plan by name")
    parser.add_argument("-T", "--test", help="specify an individual test")
    parser.add_argument("-t", "--tag", help="tag or list of tags")
    parser.add_argument("-l", "--list", help="list tests, plans or tags")

    return parser.parse_args()


def get():
    """
    Processes the user inputs and returns tests or lists to process
    :return:
    """
    args = arguments()
    tests = []
    resources = []
    report_name = ''

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

    return [tests, report_name, resources, args.list]