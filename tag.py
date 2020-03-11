import db


def get(name=''):
    query = 'SELECT * from tags'
    clause = ''
    params = ()
    if name:
        clause = ' WHERE name = ?'
        params = (name,)
    return db.run_statement(query + clause, params)


def store(name):
    """
    Creates a new tag
    :param name: str
    """
    query = "INSERT INTO tags (name) VALUES (?)"
    params = (name,)
    db.run_statement(query, params, mode='write')