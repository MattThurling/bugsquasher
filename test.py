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
        # TODO: this should be AND not OR
        # There may be a more elegant way of handling lists of tags!
        tlist = tag.split(',')
        tstring = "("
        for t in tlist:
            tstring += "'" + t + "',"
        tstring = tstring[:-1] + ")"
        # Caution: doing it this way means that the statement is not called like a prepared statement
        clause = " JOIN test_tag ON tests.id = test_id JOIN tags ON tags.id = tag_id WHERE tags.name IN " + tstring

    return db.run_statement(query + clause, params)


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