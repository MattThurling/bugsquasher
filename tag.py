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


def attach(test_name, tag_name):
    """
    Attaches an existing tag to an existing test
    :param test_name:
    :param tag_name:
    :return:
    """
    query = ("INSERT INTO test_tag (test_id, tag_id)"
             "VALUES ((SELECT id FROM tests WHERE name=?), (SELECT id FROM tags where name=?))")
    params = (test_name, tag_name)
    db.run_statement(query, params, mode='write')