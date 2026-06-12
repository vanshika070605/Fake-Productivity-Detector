import pandas as pd

df = pd.read_csv("activity.csv")

total_time = df["Time_Minutes"].sum()

productive_time = df[df["Category"] == "Productive"]["Time_Minutes"].sum()

# Productivity Score
score = (productive_time / total_time) * 100
print("Productivity Score:", round(score, 2), "%")

# Focus Score
focus_score = min(score + 10, 100)
print("Focus Score:", round(focus_score, 2), "%")

# Distraction Score (ADDED)
distraction_time = df[df["Category"] == "Distracting"]["Time_Minutes"].sum()
distraction_score = (distraction_time / total_time) * 100
print("Distraction Score:", round(distraction_score, 2), "%")

# Status
if score >= 70:
    print("Highly Productive")
elif score >= 50:
    print("Moderately Productive")
else:
    print("Fake Productivity Detected")
