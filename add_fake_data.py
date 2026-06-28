import psycopg2
from faker import Faker 

PASSWORD = "091152"

fake = Faker('ru_RU')

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password=PASSWORD,
    database="postgres",
    port="5432"
)
cursor = conn.cursor() 

for i in range(20):
    name = fake.name()
    age = fake.random_int(18, 70)
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))

conn.commit()
