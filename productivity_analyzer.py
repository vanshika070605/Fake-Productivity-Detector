import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("activity.csv")

# Data cleaning (IMPORTANT)
df["Category"] = df["Category"].str.lower()

# Total time
total_time = df["Time_Minutes"].sum()

if total_time == 0:
    print("No data found in CSV")
    exit()

# Productivity calculation
productive_time = df[df["Category"] == "productive"]["Time_Minutes"].sum()
distraction_time = df[df["Category"] == "distracting"]["Time_Minutes"].sum()

score = (productive_time / total_time) * 100
focus_score = min(score + 10, 100)
distraction_score = (distraction_time / total_time) * 100

# ================= REPORT =================
print("\n===== DAILY PRODUCTIVITY REPORT =====")
print("Productivity Score:", round(score, 2), "%")
print("Focus Score:", round(focus_score, 2), "%")
print("Distraction Score:", round(distraction_score, 2), "%")

if score >= 70:
    print("Status: Highly Productive")
elif score >= 50:
    print("Status: Moderately Productive")
else:
    print("Status: Fake Productivity Detected")

print("=====================================\n")

# ================= SAVE REPORT =================
with open("report.txt", "w") as f:
    f.write("===== DAILY PRODUCTIVITY REPORT =====\n")
    f.write(f"Productivity Score: {score:.2f}%\n")
    f.write(f"Focus Score: {focus_score:.2f}%\n")
    f.write(f"Distraction Score: {distraction_score:.2f}%\n")

# ================= GRAPH =================
data = df.groupby("Category")["Time_Minutes"].sum()

data.plot(kind="bar")
plt.title("Time Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Minutes")
plt.show()
