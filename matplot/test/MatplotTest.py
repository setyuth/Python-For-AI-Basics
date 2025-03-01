import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data from Part 3
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dana'],
    'Math': [85, 92, 78, 95],
    'Science': [88, 85, 90, 92]
}
df = pd.DataFrame(data)

# Plot Math scores
plt.plot(df['Name'], df['Math'], marker='o', label='Math')
plt.plot(df['Name'], df['Science'], marker='s', label='Science')
plt.title('Student Exam Scores')
plt.xlabel('Student')
plt.ylabel('Score')
plt.legend()
plt.grid(True)
plt.show()