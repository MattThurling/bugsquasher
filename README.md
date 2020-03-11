# Bugsquasher

Test plan framework.

### Prerequisites

Python 3.7

## Installing

Clone the repository and cd into the directory:

```
cd bugsquasher
```

## Running the framework

Run all tests:

```
python3 execute_tests.py
```

Run test plan by name:

```
python3 execute_tests.py -p <test plan name>
```

Run individual test by name:

```
python3 execute_tests.py -T <test name>
```

Run dynamic test plan by tag (or list of tags separated by commas):

```
python3 execute_tests.py -T <tag or tag list>
```

List all tests, test plans or tags:

```
python3 execute_tests.py -l <tag, plan, test>
```
### Tags
The following tags are available:
* short
* long
* endurance
* performance
* critical

Any test tagged critical which fails will abort the current test plan.

## Reporting
CSV reports of all test runs are stored in the reports directory.

## Creating new tests, plans and tags
Create a new test:
```
python3 create.py -T <test name>
```

Create a new plan:
```
python3 create.py -p <test plan name>
```

Create a new tag:
```
python3 create.py -p <tag name>
```

