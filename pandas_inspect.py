import pandas as pd  

data = {
    "Name": ["Amit", "Riya", "Karan", "Meena"],
    "Age": [21, 22, 20, 23],
    "Marks": [85, 90, 78, 92]
}
df = pd.DataFrame(data)

print("DataFrame:\n", df)
print("\nHead:\n", df.head())     # first rows
print("\nInfo:\n"); df.info()     # column info
print("\nColumns:", df.columns)   # column names
print("Index:", df.index)         # row labels
print("Data types:\n", df.dtypes) # datatypes of each column
print("Unique count:\n", df.nunique()) # unique values per column
print("Shape:", df.shape)         # rows x cols     
print("Size:", df.size)           # total elements

