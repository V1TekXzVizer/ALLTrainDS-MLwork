import psycopg2 
from faker import Faker 
import random 

PASSWORD = "091152"

fake = Faker('ru_RU')

conn = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = PASSWORD,
    database = "it_company",
    port = "5432"
)

cursor = conn.cursor()

positions = [
    'Junior Python Developer', 'Middle Python Developer', 'Senior Python Developer',
    'Junior Frontend Developer', 'Middle Frontend Developer', 'Senior Frontend Developer',
    'QA Engineer', 'DevOps Engineer', 'Data Analyst', 'Data Scientist',
    'UX/UI Designer', 'Product Manager', 'Project Manager', 'Technical Lead'
]

departments = ['Backend', 'Frontend', 'DevOps', 'Data', 'QA', 'Design', 'Management']

skill_list ={
    'Backend': ['Python', 'Django', 'Flask', 'FastAPI', 'SQL', 'PostgreSQL', 'Redis', 'Docker', 'Kubernetes'],
    'Frontend': ['JavaScript', 'TypeScript', 'React', 'Vue', 'Angular', 'HTML', 'CSS', 'SASS', 'Webpack'],
    'DevOps': ['Docker', 'Kubernetes', 'AWS', 'Azure', 'GCP', 'CI/CD', 'Terraform', 'Ansible'],
    'Data': ['Python', 'SQL', 'Pandas', 'NumPy', 'Scikit-learn', 'TensorFlow', 'PyTorch', 'SQL'],
    'QA': ['Selenium', 'Postman', 'JMeter', 'Jenkins', 'Git', 'Docker', 'Kubernetes'],
    'Design': ['Figma', 'Sketch', 'Adobe XD', 'Photoshop', 'Illustrator', 'InVision'],
    'Management': ['Agile', 'Scrum', 'Kanban', 'Jira', 'Confluence', 'Slack', 'Microsoft Teams']
}

for _ in range(50):
    position = random.choice(positions)
    dept = random.choice(departments)
    firts_name = fake.first_name()
    last_name = fake.last_name()
    num_skills = random.randint(3, 6)
    skills = random.sample(skill_list.get(dept, ['Python']), min(num_skills, len(skill_list.get(dept, ['Python']))))
    cursor.execute("""
        INSERT INTO employees (first_name, last_name, position, department, email, phone, salary, experience, city, remote, skills, hired_date, is_active)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (firts_name, last_name, position, dept, fake.email(), fake.phone_number(), random.randint(50000, 150000), random.randint(1, 10), fake.city(), random.choice([True, False]), skills, fake.date_this_decade(), True))

conn.commit()
cursor.close()
conn.close()
