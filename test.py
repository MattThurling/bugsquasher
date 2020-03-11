import db


def get(plan='', name='', tag=''):
    """
    Gets a list of tests according to user's specified options
    :param plan: name of a test plan
    :param name: name of an individual test
    :param tag: single tag or list of tags
    :return: list of tuples
    """
    query = "SELECT tests.id, tests.name from tests"
    clause = ""
    params = ()
    if plan:
        clause = " JOIN test_plan ON tests.id = test_id JOIN plans ON plans.id = plan_id WHERE plans.name=?"
        params = (plan,)
    elif name:
        clause = " WHERE name=?"
        params = (name,)
    elif tag:
        # There may be a more elegant way of handling lists of tags!
        tlist = tag.split(',')
        tstring = "("
        for t in tlist:
            tstring += "'" + t + "',"
        tstring = tstring[:-1] + ")"

        query = ("SELECT s.id, s.name FROM "
                 "(SELECT * FROM tests JOIN test_tag on tests.id = test_id "
                 "JOIN tags on tags.id = tag_id WHERE tags.name IN ")

        query = query + tstring + ") as s GROUP BY s.name HAVING COUNT(s.name)=?"

        params = (len(tlist),)
    return db.run_statement(query + clause, params)


def store(name):
    """
    Creates a new test
    :param name: str
    """
    query = "INSERT INTO tests (name) VALUES (?)"
    params = (name,)
    db.run_statement(query, params, mode='write')


def tags(test_id):
    """
    Returns the tags associated with a particular test
    :param test_id: int id of the test
    :return: list of tuples
    """
    query = "SELECT tags.name from tags"
    clause = " JOIN test_tag ON tags.id = tag_id JOIN tests ON tests.id = test_id WHERE tests.id=?"
    params = (test_id,)

    return db.run_statement(query + clause, params)


def plans(test_id):
    """
    Returns the plans associated with a particular test
    :param test_id: int id of the test
    :return: list of tuples
    """
    query = "SELECT plans.name from plans"
    clause = " JOIN test_plan ON plans.id = plan_id JOIN tests ON tests.id = test_id WHERE tests.id=?"
    params = (test_id,)

    return db.run_statement(query + clause, params)