from faker import Faker
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import random

fake = Faker('ru-RU')

years = [2021, 2022, 2023, 2024, 2025]
forms = ['Очная', 'Заочная', 'Заочно-Очная']
specialties = ['Информационные технологии', 'Кибербезопасность', 'Радиофизика', 'Аэрокосмические технологии', 'Робототехника', 'Машинное обучение'
               'Сетевой волшебник', 'Инженер', 'Компьютерный гном']
subjects = ['Математика', 'Русский язык', 'Физика']

def generate_student(count=10):
    students = []
    for _ in range(count):
        students.append({
            "first_name": fake.first_name(),
            "second_name": fake.last_name(),
            "year_of_admission": fake.date_between(start_date='-5y', end_date='-5m').year,
            "form": random.choice(forms),
            "score": {"Math": random.randint(1, 100), "Russian": random.randint(1, 100), "Physics": random.randint(1, 100)},
            "certificate_score": random.randint(1, 100),
            "overall_score": 0,
            "specialty": random.choice(specialties),
            "address": fake.address(),
            "phone_number": fake.phone_number()
        })

    for __ in range(count):
        total_score = 0
        for _ in students[__]['score']:
            total_score += students[__]['score'][_]
        total_score += students[__]['certificate_score']
        students[__]['overall_score'] = total_score
        
    return students

students = generate_student(100)

subject_avg = defaultdict(lambda: defaultdict(list))

for st in students:
    year = st["year_of_admission"]
    for subj, score in st["score"].items():
        subject_avg[subj][year].append(score)

plt.figure(figsize=(10,5))
for subj in subject_avg:
    years_sorted = sorted(subject_avg[subj].keys())
    avg_scores = [np.mean(subject_avg[subj][y]) for y in years_sorted]
    plt.plot(years_sorted, avg_scores, marker='o', label=subj)

plt.title("Динамика среднего балла по предметам")
plt.xlabel("Год")
plt.ylabel("Средний балл")
plt.legend()
plt.grid(True)
plt.show()

cert_by_year = defaultdict(list)

for st in students:
    cert_by_year[st["year_of_admission"]].append(st["certificate_score"])

plt.figure(figsize=(10,5))
years_sorted = sorted(cert_by_year.keys())
avg_cert = [np.mean(cert_by_year[y]) for y in years_sorted]

plt.plot(years_sorted, avg_cert, marker="o")
plt.title("Динамика среднего балла аттестата")
plt.xlabel("Год")
plt.ylabel("Балл аттестата")
plt.grid(True)
plt.show()


pass_score = defaultdict(list)

for st in students:
    pass_score[st["year_of_admission"]].append(st["overall_score"])

plt.figure(figsize=(10,5))
years_sorted = sorted(pass_score.keys())
min_scores = [min(pass_score[y]) for y in years_sorted]

plt.plot(years_sorted, min_scores, marker='o', color='red')
plt.title("Динамика проходного балла")
plt.xlabel("Год")
plt.ylabel("Проходной балл (минимальный)")
plt.grid(True)
plt.show()


spec_count = defaultdict(int)

for st in students:
    spec_count[st["specialty"]] += 1

plt.figure(figsize=(12,6))
plt.bar(spec_count.keys(), spec_count.values())
plt.title("Количество студентов по специальностям")
plt.xlabel("Специальность")
plt.ylabel("Количество")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()


form_count = defaultdict(int)

for st in students:
    form_count[st["form"]] += 1

plt.figure(figsize=(8,6))
plt.pie(list(form_count.values()), labels=list(form_count.keys()), autopct="%1.1f%%")
plt.title("Статистика по формам обучения")
plt.show()