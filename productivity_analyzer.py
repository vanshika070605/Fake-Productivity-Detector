import pandas as pd

df = pd.read_csv("activity.csv")

total_time = df["Time_Minutes"].sum()

productive_time = df[df["Category"] == "Productive"]["Time_Minutes"].sum()

score = (productive_time / total_time) * 100

print("Productivity Score:", round(score, 2), "%")

if score >= 70:
    print("Highly Productive")
elif score >= 50:
    print("Moderately Productive")
else:
    print("Fake Productivity Detected")
import matplotlib.pyplot as plt

data = df.groupby("Category")["Time_Minutes"].sum()

plt.pie(data, labels=data.index, autopct="%1.1f%%")
plt.title("Productivity Analysis")
plt.show()

focus_score = ((productive_time / total_time) * 100) + 10

if focus_score > 100:
    focus_score = 100

print("Focus Score:", round(focus_score, 2), "%")
