# pg_simple.py
import psycopg2

# ТОЛЬКО ЭТО МЕНЯЕМ - свой пароль!
PASSWORD = "091152"

# Подключаемся
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password=PASSWORD,
    database="postgres"
)

cursor = conn.cursor()

# Создаем таблицу
cursor.execute("""
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        age INTEGER
    )
""")

conn.commit()
print("✅ Таблица users создана!")

# Добавляем данные
cursor.execute("INSERT INTO users (name, age) VALUES ('Иван', 25)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Мария', 30)")
conn.commit()
print("✅ Данные добавлены!")

# Проверяем
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Имя: {row[1]}, Возраст: {row[2]}")

cursor.close()
conn.close()