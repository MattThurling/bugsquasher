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


def attach(test_name, plan_name):
    """
    Adds an existing test to an existing plan
    :param name: str
    """
    query = ("INSERT INTO test_plan (test_id, plan_id)"
             "VALUES ((SELECT id FROM tests WHERE name=?), (SELECT id FROM plans where name=?))")
    params = (test_name, plan_name)
    db.run_statement(query, params, mode='write')