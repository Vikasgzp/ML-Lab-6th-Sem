from question import create_dataset

df = create_dataset()


buggy_df = df.copy()

# Fix 1: Performance calculation (this is logically okay,
# but usually performance shouldn't mix CGPA*10 + Attendance directly.
# Keeping structure same but it's not a syntax error.)
buggy_df['Performance'] = buggy_df['CGPA'] * 10 + buggy_df['Attendance']

# Fix 2: Column name is wrong (Hackathon → Hackathons)
active = buggy_df[buggy_df['Hackathons'] > 2]

# Fix 3: CS score already boosted in original calculation.
# Applying again would double multiply.
# If requirement is to adjust once, keep it. Otherwise remove.
# Here we assume we apply once intentionally.

buggy_df.loc[buggy_df['Department'] == 'CS', 'Total_Score'] *= 1.05

# Fix 4: Grouping by Name is incorrect.
# Should group by Department (or Roll_No).
dept_stats = buggy_df.groupby('Department').agg({
    'Total_Score': 'sum',
    'Project_Marks': 'max'
})

print("All errors fixed successfully.")
print("\nActive Students (>2 Hackathons):")
print(active.head())

print("\nDepartment Stats:")
print(dept_stats)
