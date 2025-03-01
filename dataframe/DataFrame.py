import numpy as np
import pandas as pd

# Dictionary with data
# This DataFrame has rows (students) and columns (attributes).
# In AI, this could be a dataset for predicting student performance.
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dana'],
    'Math': [85, 92, 78, 95],
    'Science': [88, 85, 90, 92],
    'Attendance': [0.95, 0.80, 0.99, 0.90]
}

# Create DataFrame
df = pd.DataFrame(data)

print(df)

# In real AI projects, you’ll load data from files.
# Let’s assume you have a CSV file named students.csv with the same data.
# Here’s how to load it:
#df = pd.read_csv('D:\PYTHON-PROJECTS\DataFrame\students.csv')
#print(df)

# Exploring the Data
# Basic Info: This shows column names, data types, and if any values are missing.
print(df.info())

# Summary Statistics:
# This gives you means, standard deviations, and ranges—super
# useful for understanding data distributions in AI.
print(df.describe())

# Selecting and Filtering Data
# In AI, you often need specific parts of the data. Here’s how:
# Select Columns:
math_scores = df['Math']
print(math_scores)

# Select Multiple Columns:
scores = df[['Math', 'Science']]
print(scores)

# Filter Rows: Let’s find students with Math scores above 90:
high_math = df[df['Math'] > 90]
print(high_math)

# Adding and Modifying Data
# Let’s add a new column for “Average Score”:
df['Average'] = (df['Math'] + df['Science']) / 2
print(df)

# Now, let’s say Bob’s attendance was recorded incorrectly. Update it:
# In AI, you might update data like this to correct errors before modeling.
df.loc[df['Name']  == 'Bob', 'Attendance'] = 0.85
print(df)

# Handling Missing Data
# Real-world AI datasets often have missing values. Let’s introduce one and fix it:
# Introduce a missing value
df.loc[1, 'Science'] = np.nan
print(df)

# Drop Missing Values:
df_dropped = df.dropna()
print(df_dropped)

# Fill Missing Values: Let’s fill Bob’s Science score with the mean:
# In AI, you choose dropping or filling based on how much data you can afford to lose.
mean_science = df['Science'].mean()
df['Science'] = df['Science'].fillna(mean_science)
print(df)

# Practical AI Example: Feature Engineering
# In machine learning, you create new features to improve models.
# Let’s add a feature: “Pass/Fail” based on Average > 85.
# This binary feature could be a target variable for a classification model.
df['Pass'] = df['Average'] > 85
print(df)

# Grouping and Aggregation
# Suppose you’re analyzing data across groups.
# Let’s group by Pass/Fail and compute averages:
# This shows how passing students differ from failing ones—useful for insights in AI.
grouped = df.groupby('Pass').mean(numeric_only=True)
print(grouped)