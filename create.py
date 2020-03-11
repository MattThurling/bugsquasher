import test
import tag
import plan
import options

if __name__ == '__main__':

    args = options.arguments()

    if args.test and args.plan:
        plan.attach(args.test, args.plan)
    elif args.test and args.tag:
        tag.attach(args.test, args.tag)
    elif args.test:
        test.store(args.test)
    elif args.plan:
        test.store(args.plan)
    elif args.tag:
        test.store(args.tag)
    else:
        print("error: no valid options given")


