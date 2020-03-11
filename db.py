import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def run_statement(sql, params=(), mode='read'):
    """ get a database connection and execute a query
    :param sql: a prepared sql statement
    :param params: a tuple of parameters
    :return: results, list of tuples
    """
    try:
        conn = create_connection('data.db')
        c = conn.cursor()
        c.execute(sql, params)
        if mode == 'read':
            results = c.fetchall()
        if mode == 'write':
            conn.commit()
            results = params[0] + ' saved'
            print(results)
    except sqlite3.Error as e:
        print(e)

    return results




