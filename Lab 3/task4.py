from question import create_dataset
import matplotlib.pyplot as plt

df = create_dataset()

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 🔹 Plot 1: Average score by department (Bar Chart)
avg_score = df.groupby('Department')['Total_Score'].mean()
axes[0, 0].bar(avg_score.index, avg_score.values, color='skyblue')
axes[0, 0].set_title("Average Score by Department")
axes[0, 0].set_xlabel("Department")
axes[0, 0].set_ylabel("Average Total Score")

# 🔹 Plot 2: Attendance vs Total_Score (Scatter Plot)
axes[0, 1].scatter(df['Attendance'], df['Total_Score'], color='green', alpha=0.7)
axes[0, 1].set_title("Attendance vs Total Score")
axes[0, 1].set_xlabel("Attendance")
axes[0, 1].set_ylabel("Total Score")

# 🔹 Plot 3: CGPA Distribution (Histogram)
axes[1, 0].hist(df['CGPA'], bins=10, color='orange', edgecolor='black')
axes[1, 0].set_title("CGPA Distribution")
axes[1, 0].set_xlabel("CGPA")
axes[1, 0].set_ylabel("Frequency")

# 🔹 Plot 4: Project Marks by Lab Batch (Box Plot)
df.boxplot(column='Project_Marks', by='Lab_Batch', ax=axes[1, 1])
axes[1, 1].set_title("Project Marks by Lab Batch")
axes[1, 1].set_xlabel("Lab Batch")
axes[1, 1].set_ylabel("Project Marks")

plt.tight_layout()
plt.show()
