import os

import psycopg2


class DbClient:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname=os.environ['POSTGRES_DB'],
            user=os.environ['POSTGRES_USER'],
            password=os.environ['POSTGRES_PASSWORD'],
            host=os.environ['DB_HOST'],
            port=int(os.getenv('DB_PORT', '5432')),
        )
        self.connection.autocommit = True

    def execute(self, query, params=None):
        with self.connection.cursor() as cur:
            cur.execute(query, params)

    def fetch_one(self, query, params=None):
        with self.connection.cursor() as cur:
            cur.execute(query, params)
            return cur.fetchone()

    def create_products_table(self):
        self.execute("DROP TABLE IF EXISTS products")
        self.execute("CREATE TABLE products (id SERIAL PRIMARY KEY, name TEXT, price NUMERIC)")

    def insert_product(self, name, price):
        self.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (name, price))

    def get_product(self, name):
        return self.fetch_one("SELECT name, price FROM products WHERE name = %s", (name,))

    def update_product_price(self, name, price):
        self.execute("UPDATE products SET price = %s WHERE name = %s", (price, name))

    def delete_product(self, name):
        self.execute("DELETE FROM products WHERE name = %s", (name,))

    def get_all_products(self):
        with self.connection.cursor() as cur:
            cur.execute("SELECT name, price FROM products ORDER BY id")
            return cur.fetchall()

    def count_products(self):
        return self.fetch_one("SELECT count(*) FROM products")[0]

    def close(self):
        self.connection.close()