import db


def get(name=''):
    query = 'SELECT * from plans'
    clause = ''
    params = ()
    if (name):
        clause = ' WHERE name = ?'
        params = name

    return db.run_statement(query + clause, params)


def store(name):
    """
    Creates a new test plan
    :param name: str
    """
    query = "INSERT INTO plans (name) VALUES (?)"
    params = (name,)
    db.run_statement(query, params, mode='write')


def attach(test, plan):
    """
    Adds an existing test to an existing plan
    :param name: str
    """
    query = "INSERT INTO test_plan (test_id, plan_id) VALUES (?)"
    params = (name,)
    db.run_statement(query, params, mode='write')