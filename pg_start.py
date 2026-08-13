import psycopg2 

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="091152"
)

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS users CASCADE")
conn.commit()

# Создание таблицы users заново
cursor.execute("""
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        full_name VARCHAR(100),
        age INTEGER,
        city VARCHAR(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

conn.commit()

# Добавление одного пользователя
cursor.execute("""
    INSERT INTO users (username, email, full_name, age, city) 
    VALUES (%s, %s, %s, %s, %s)
""", ("john_doe", "john@gmail.com", "John Doe", 30, "New York"))

conn.commit()
print("✅ Пользователь добавлен")

# Добавление нескольких пользователей
users = [
    ("jane_smith", "jane@gmail.com", "Jane Smith", 25, "London"),
    ("bob_wilson", "bob@gmail.com", "Bob Wilson", 35, "Paris"),
    ("alice_brown", "alice@gmail.com", "Alice Brown", 28, "Berlin")
]

cursor.executemany("""
    INSERT INTO users (username, email, full_name, age, city) 
    VALUES (%s, %s, %s, %s, %s)
""", users)

conn.commit()

# Проверка
cursor.execute("SELECT username, full_name, age, city FROM users")
for row in cursor.fetchall():
    print(f"{row[0]} | {row[1]} | {row[2]} лет | {row[3]}")

cursor.close()
conn.close()