import db


def get(name=''):
    query = 'SELECT * from tags'
    clause = ''
    params = ()
    if name:
        clause = ' WHERE name = ?'
        params = (name,)
    return db.run_statement(query + clause, params)