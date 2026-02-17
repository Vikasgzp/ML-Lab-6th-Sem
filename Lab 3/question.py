import pandas as pd
import numpy as np

def create_dataset():
    np.random.seed(42)

    num_students = 40
    student_data = []

    for i in range(1, num_students + 1):
        dept_code = np.random.choice(['CS', 'EC', 'ME', 'CE'], p=[0.4, 0.3, 0.2, 0.1])
        roll_no = f"23{dept_code}{str(i).zfill(3)}"
        name = f"Student_{chr(65 + (i % 26))}{i}"
        lab_batch = np.random.choice([f'A{j}' for j in range(1,5)] + [f'B{j}' for j in range(1,5)])
        cgpa = np.random.normal(loc=7.5, scale=1.2)
        cgpa = max(0, min(10, round(cgpa, 2)))
        attendance = np.random.randint(70, 101)

        course_options = {
            'CS': ['CS301', 'CS302', 'CS303'],
            'EC': ['EC401', 'EC402'],
            'ME': ['ME501', 'ME502'],
            'CE': ['CE601', 'CE602']
        }
        course = np.random.choice(course_options[dept_code])

        project_marks = np.random.randint(18, 31)
        hackathons = np.random.poisson(lam=1.5)

        student_data.append({
            'Roll_No': roll_no,
            'Name': name,
            'Department': dept_code,
            'Lab_Batch': lab_batch,
            'CGPA': cgpa,
            'Attendance': attendance,
            'Course': course,
            'Project_Marks': project_marks,
            'Hackathons': hackathons,
            'Hosteller': np.random.choice([0, 1], p=[0.4, 0.6])
        })

    df = pd.DataFrame(student_data)

    def calculate_score(row):
        score = row['CGPA'] * 10
        score += row['Hackathons'] * 2
        if row['Attendance'] > 85:
            score += 1
        if row['Hosteller'] == 1:
            score += 1.5
        if row['Course'].startswith('CS'):
            score *= 1.05
        return round(score, 2)

    df['Total_Score'] = df.apply(calculate_score, axis=1)

    return df
