import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# create some sample data
data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7],
    "Scores": [35, 40, 50, 55, 65, 70, 80]
}

df = pd.DataFrame(data)

# basic statistics
print("Mean score:", df["Scores"].mean())
print("Correlation:", df["Hours_Studied"].corr(df["Scores"]))

# visualization
plt.scatter(df["Hours_Studied"], df["Scores"])
plt.title("Hours Studied vs Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Scores")
plt.show()
