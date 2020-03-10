import db

def get(name=''):
    query = 'SELECT * from plans'
    clause = ''
    params = ()
    if (name):
        clause = ' WHERE name = ?'
        params = name

    return db.run_statement(query + clause, params)