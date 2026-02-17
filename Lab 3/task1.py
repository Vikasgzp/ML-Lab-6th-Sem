from question import create_dataset

df = create_dataset()

# Task 1: Categorize students

def categorize_student(row):
    if row['Total_Score'] > 85 and row['Attendance'] > 90:
        return 'Scholarship'
    elif row['Total_Score'] > 75 or (row['Project_Marks'] > 25 and row['Hackathons'] >= 2):
        return 'Placement'
    elif row['Total_Score'] < 60 or row['Attendance'] < 75:
        return 'Needs Help'
    else:
        return 'Regular'

# Create Category column
df['Category'] = df.apply(categorize_student, axis=1)

# Count students in each category
category_counts = df['Category'].value_counts()

print("\nStudent Count by Category:")
print(category_counts)

# Find department with most Scholarship students
scholarship_dept = (
    df[df['Category'] == 'Scholarship']['Department']
    .value_counts()
    .idxmax()
)

print("\nDepartment with most Scholarship students:")
print(scholarship_dept)
