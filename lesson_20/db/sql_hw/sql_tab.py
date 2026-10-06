import psycopg2 as ps
from faker import Faker

faker = Faker()

connector = ps.connect(
    host="localhost",
    port="5432",
    dbname="mydb",
    user="kate",
    password="kate",
)

cursor = connector.cursor()

q = '''CREATE TABLE IF NOT EXISTS public.products (
	id int4 GENERATED ALWAYS AS IDENTITY NOT NULL,
    name varchar NOT NULL,
    description varchar NULL,
    price numeric(10,2) NOT NULL,
    category_id int4 NULL,
    CONSTRAINT products_pk PRIMARY KEY (id),
    CONSTRAINT products_category_fk 
    
    FOREIGN KEY (category_id)
    
    REFERENCES public.categories (id)
);
'''

cursor.execute(q)


categories = [
    ("Animal feed", "Food for dogs, cats and other pets"),
    ("Health and treatment", "Vitamins, medicines and care products for animals"),
    ("Clothing for animals", "Coats, collars and harnesses"),
    ("Toys", "Toys and games for pets"),
]

for name, description in categories:
    execute_categories_q = f"""
        INSERT INTO public.categories (name, description)
        VALUES ('{name}','{description}')
        ON CONFLICT (name) DO NOTHING;
        """
    cursor.execute(execute_categories_q)


products_name_and_description = [
    ("Dog food Premium", "Dry food for adult dogs", 1),
    ("Cat food Premium", "Dry food for adult cats", 1),
    ("Puppy food", "Dry food for puppies", 1),
    ("Cat vitamins", "Vitamin complex for cats", 2),
    ("Dog vitamins", "Vitamin complex for dogs", 2),
    ("Flea shampoo", "Shampoo for protection against fleas", 2),
    ("Animal eye drops", "Eye care drops for dogs and cats", 2),
    ("Dog coat", "Warm coat for dogs in cold weather", 3),
    ("Cat collar", "Comfortable collar for cats", 3),
    ("Dog harness", "Adjustable harness for dogs", 3),
    ("Rubber ball", "Durable rubber ball for dogs", 4),
    ("Cat mouse toy", "Interactive toy for cats", 4),
    ("Rope toy", "Rope toy for dogs", 4),
    ("Interactive toy", "Interactive toy for cats and dogs", 4),
]


for product_name, product_description, category_id in products_name_and_description:

    product_price = round(faker.random.uniform(10, 1000), 2)

    execute_products_q = f'''
    INSERT INTO public.products
    (name, description, price, category_id)
    VALUES (
        '{product_name}',
        '{product_description}',
        {product_price},
        {category_id}
    )
    '''

    cursor.execute(execute_products_q)

connector.commit()
cursor.close()
connector.close()