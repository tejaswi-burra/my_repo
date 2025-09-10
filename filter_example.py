import pandas as pd

# Sample data
data = {
    "Name": ["Amit", "Riya", "Karan", "Meena"],
    "Marks": [85, 72, 90, 60],
    "City": ["Delhi", "Hyderabad", "Delhi", "Chennai"]
}

df = pd.DataFrame(data)

# Filter students who scored less than 80
low_scorers = df[df["Marks"] < 80]

print("Students scoring less than 80:")
print(low_scorers)
