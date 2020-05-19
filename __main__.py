import psycopg2
from config import getConfig

def __exec__():
    """ Connect to the PostgreSQL database server """
    conn = None

    try:
        databaseParams = getConfig('database')
        fileParms = getConfig('createdFile')
        urlParms = getConfig('url')

        print('Connecting to the database')
        conn = psycopg2.connect(**databaseParams)

        cur = conn.cursor()

        print('Database version: ')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)

        result = None
        cur.execute('query')
        result = cur.fetchall()

        sitemap = open('{0}/{1}' .format(fileParms['path'], fileParms['name']), 'w+')

        for data in result:
            sitemap.write('{0}?{1}={2}\r' .format(urlParms['url'], urlParms['param'], data[0]))

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed')

if __name__ == '__main__':
    __exec__()