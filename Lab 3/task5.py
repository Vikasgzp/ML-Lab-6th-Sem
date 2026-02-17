from question import create_dataset
df = create_dataset()

# 🔹 Function 1: Analyze Department
def analyze_department(dept_code):
    dept_df = df[df['Department'] == dept_code]
    
    avg_score = dept_df['Total_Score'].mean()
    
    top_student = dept_df.loc[dept_df['Total_Score'].idxmax(), 'Name']
    
    weak_count = len(dept_df[dept_df['Total_Score'] < 60])
    
    return round(avg_score, 2), top_student, weak_count


# 🔹 Function 2: Compare Batches
def compare_batches(batch1, batch2):
    batch1_mean = df[df['Lab_Batch'].str.startswith(batch1)]['Total_Score'].mean()
    batch2_mean = df[df['Lab_Batch'].str.startswith(batch2)]['Total_Score'].mean()
    
    difference = round(abs(batch1_mean - batch2_mean), 2)
    
    if batch1_mean > batch2_mean:
        better = batch1
    else:
        better = batch2
        
    return better, difference


# Check all departments
departments = df['Department'].unique()

for dept in departments:
    avg, top, weak = analyze_department(dept)
    print(f"\nDepartment: {dept}")
    print(f"Average Score: {avg}")
    print(f"Top Student: {top}")
    print(f"Weak Students (<60): {weak}")

# Compare A and B batches
better_batch, diff = compare_batches('A', 'B')
print(f"\nBetter Batch: {better_batch}")
print(f"Difference in Average Score: {diff}")
