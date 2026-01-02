import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_marks.csv")

# Basic information
print("Dataset Shape (rows, columns):")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

# Missing values check
print("\nMissing Values Count:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Create total score column (math + reading + writing)
df["total_score"] = df["math score"] + df["reading score"] + df["writing score"]

# Visualization 1: Distribution of total score
plt.figure()
plt.hist(df["total_score"], bins=20)
plt.title("Distribution of Total Student Scores")
plt.xlabel("Total Score")
plt.ylabel("Number of Students")
plt.show()

# Visualization 2: Gender vs Average Score
avg_scores = df.groupby("gender")["total_score"].mean()

plt.figure()
avg_scores.plot(kind="bar")
plt.title("Average Total Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.show()
