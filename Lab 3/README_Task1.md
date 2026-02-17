# 📊 Task 1: Student Categorization System

## 🎯 Objective

To categorize students based on performance metrics such as:

- Total Score
- Attendance
- Project Marks
- Hackathon Participation

---

## 📌 Rules for Categorization

### 🏆 Scholarship

- Total_Score > 85
- Attendance > 90

### 💼 Placement

- Total_Score > 75  
  OR
- Project_Marks > 25 AND Hackathons >= 2

### ⚠ Needs Help

- Total_Score < 60  
  OR
- Attendance < 75

### ✅ Regular

- All other students

---

## 🧠 Approach

1. Created a function `categorize_student()`
2. Applied conditional logic using if-elif-else
3. Generated new column `Category`
4. Counted students in each category
5. Identified department with most Scholarship students

---

## 📊 Outcome

- Students classified into 4 performance groups
- Easy identification of high achievers and weak performers
- Department-level scholarship analysis completed

---

## 📘 Concepts Used

- Pandas `apply()`
- Conditional logic
- Value counts
- Filtering & grouping
