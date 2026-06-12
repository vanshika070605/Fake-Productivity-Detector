import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("activity.csv")

df["Category"] = df["Category"].str.lower()

total_time = df["Time_Minutes"].sum()

if total_time == 0:
    score = 0
else:
    productive_time = df[df["Category"] == "productive"]["Time_Minutes"].sum()
    score = (productive_time / total_time) * 100

print("Productivity Score:", round(score, 2), "%")

if score >= 70:
    print("Highly Productive")
elif score >= 50:
    print("Moderately Productive")
else:
    print("Fake Productivity Detected")

# Pie chart
data = df.groupby("Category")["Time_Minutes"].sum()

plt.pie(data, labels=data.index, autopct="%1.1f%%")
plt.title("Productivity Analysis")
plt.show()

# Focus score
focus_score = min(score + 10, 100)
print("Focus Score:", round(focus_score, 2), "%")

focus_score = ((productive_time / total_time) * 100) + 10

if focus_score > 100:
    focus_score = 100

print("Focus Score:", round(focus_score, 2), "%")
