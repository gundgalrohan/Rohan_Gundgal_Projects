Student Habits Analysis
An R-based exploratory data analysis project examining how student lifestyle habits (study hours, sleep, social media, attendance) correlate with academic performance.

Features
Data cleaning: removes missing and duplicate values
Pearson correlation matrix across key numeric variables
Three scatter plots with linear regression overlays:

Study Hours vs Exam Score
Social Media Hours vs Exam Score
Attendance % vs Exam Score

Tech Stack
R ggplot2 dplyr

How to Run
rinstall.packages(c("ggplot2", "dplyr"))
# Update the CSV path in the script, then:
source("student_habits_analysis.R")

Dataset
Expects a CSV with columns including: study_hours_per_day, social_media_hours, attendance_percentage, sleep_hours, exam_score.

Key Findings
More study hours → higher exam scores
More social media hours → lower scores
Better attendance → better performance
