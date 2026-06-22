import pandas as pd
import random

phishing_templates = [
    "Verify your bank account immediately",
    "Your account has been suspended",
    "Click here to claim your reward",
    "You won a lottery prize",
    "Reset your password now",
    "Urgent action required",
    "Security alert detected",
    "Confirm your login credentials"
]

safe_templates = [
    "Meeting scheduled for tomorrow",
    "Project deadline is Friday",
    "Please review the attached document",
    "Happy birthday and best wishes",
    "Team lunch planned next week",
    "Conference starts at 10 AM",
    "Weekly report submission reminder",
    "Let's discuss the project tomorrow"
]

data = []

for _ in range(2500):
    data.append([random.choice(phishing_templates), "phishing"])

for _ in range(2500):
    data.append([random.choice(safe_templates), "safe"])

random.shuffle(data)

df = pd.DataFrame(data, columns=["text", "label"])
df.to_csv("emails.csv", index=False)

print(f"Dataset created with {len(df)} emails")