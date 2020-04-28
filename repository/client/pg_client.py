import psycopg2
from psycopg2 import extras
from psycopg2.extras import DictCursor
import os


class PgClient:

    def __init__(self, url):
        self.url = url

    def execute(self, sql, params=()):
        with psycopg2.connect(self.url) as connection:
            with connection.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(sql, params)
                try:
                    return cursor.fetchall()
                except:
                    # create, insert などの時は cursor.fetchall() が例外を投げるため、None を返すようにする
                    return None

    def execute_batch(self, sql, params):
        with psycopg2.connect(self.url) as connection:
            with connection.cursor(cursor_factory=DictCursor) as cursor:
                extras.execute_values(cursor, sql, params)
                try:
                    return cursor.fetchall()
                except:
                    return None


# 環境変数から取ってこれない場合は、local のものを使う
url = os.environ.get('DATABASE_URL') or 'postgresql://postgres:password@localhost:5432/postgres'
pg_client = PgClient(url)
