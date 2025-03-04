# Import required libraries (assumed to be imported earlier in the script)
import matplotlib.pyplot as plt
import pandas as pd

# Basic Plotting: Line Plot
# Let’s start with a simple line plot using the student data from Part 3:
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dana'],
    'Math': [85, 92, 78, 95],
    'Science': [88, 85, 90, 92]
}
# Creating a pandas DataFrame from the given data, enabling easy data manipulation and analysis.
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

# Bar Chart: Comparing Categories
# For categorical data, bar charts shine. Let’s plot average scores:
# Add Average column
df['Average'] = (df['Math'] + df['Science']) / 2

# Bar chart
plt.bar(df['Name'], df['Average'], color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
plt.title('Average Scores by Student')
plt.xlabel('Student')
plt.ylabel('Average Score')
plt.show()

# Scatter Plot: Exploring Relationships
# Scatter plots reveal relationships between variables.
# Let’s plot Math vs. Science scores:
plt.scatter(df['Math'], df['Science'], color='purple', s=100, alpha=0.6)
plt.title('Math vs. Science Scores')
plt.xlabel('Math Score')
plt.ylabel('Science Score')
for i, name in enumerate(df['Name']):
    plt.annotate(name, (df['Math'][i], df['Science'][i]), xytext=(5, 5), textcoords='offset points')
plt.show()

# Subplots: Multiple Views
# In AI, you often compare multiple aspects.
# Subplots let you do this in one figure:
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))  # 1 row, 2 columns

# Plot 1: Math scores
ax1.plot(df['Name'], df['Math'], 'b-o')
ax1.set_title('Math Scores')
ax1.set_xlabel('Student')
ax1.set_ylabel('Score')

# Plot 2: Science scores
ax2.plot(df['Name'], df['Science'], 'g-s')
ax2.set_title('Science Scores')
ax2.set_xlabel('Student')
ax2.set_ylabel('Score')

plt.tight_layout()  # Adjust spacing
plt.show()

# Real-World AI Example: Time Series
# Imagine you’re analyzing daily temperatures for an AI weather model:
# Weather data
weather = pd.DataFrame({
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Temp': [22, 25, 19, 28, 24]
})

plt.plot(weather['Day'], weather['Temp'], 'r-^', label='Temperature')
plt.title('Daily Temperatures')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.xticks(rotation=45)  # Rotate x-axis labels
plt.show()

# Histogram: Data Distribution
# In AI, histograms help you understand data spread.
# Let’s plot all scores:
all_scores = pd.concat([df['Math'], df['Science']])
plt.hist(all_scores, bins=5, color='skyblue', edgecolor='black')
plt.title('Distribution of All Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()

# Exercise
# 1. Create a bar chart of temperatures.
# 2. Add a second bar chart for rainfall using dual axes (hint: plt.twinx()).
# 3. Label everything clearly.
# Solution:

# Step 1: Create a DataFrame with weather data
# - 'Day' column lists days of the week (categorical x-axis data)
# - 'Temp' column holds temperature values in Celsius (numerical data for first y-axis)
# - 'Rain' column holds rainfall values in millimeters (numerical data for second y-axis)
weather = pd.DataFrame({
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Temp': [22, 25, 19, 28, 24],
    'Rain': [0.1, 0.0, 0.3, 0.2, 0.0]
})

# Step 2: Initialize a figure and primary axes
# - `plt.subplots()` creates a figure (fig) and one set of axes (ax1)
# - `fig` controls the overall plot, while `ax1` is for the temperature bars
fig, ax1 = plt.subplots()

# Step 3: Plot temperature bars on the primary axes (ax1)
# - `ax1.bar()` creates bars with 'Day' on x-axis and 'Temp' on y-axis
# - `color='lightblue'` sets a distinct color for temperature bars
# - `label='Temp'` names this data for the legend
ax1.bar(weather['Day'], weather['Temp'], color='lightblue', label='Temp')

# Step 4: Label the x-axis (shared by both plots)
# - `set_xlabel('Day')` labels the x-axis as days of the week
ax1.set_xlabel('Day')

# Step 5: Label the primary y-axis (temperature)
# - `set_ylabel()` names the y-axis for temperature, with units (°C)
# - `color='blue'` matches the label color to the bars for clarity
ax1.set_ylabel('Temperature (°C)', color='blue')

# Step 6: Customize the primary y-axis ticks
# - `tick_params()` sets the y-axis tick labels to blue, aligning with the bars and label
# - `axis='y'` specifies we’re modifying the y-axis (not x)
ax1.tick_params(axis='y', labelcolor='blue')

# Step 7: Create a secondary y-axis sharing the same x-axis
# - `ax1.twinx()` generates `ax2`, a second axes overlaid on `ax1`
# - This allows plotting rainfall on a separate y-axis while sharing the 'Day' x-axis
ax2 = ax1.twinx()

# Step 8: Plot rainfall bars on the secondary axes (ax2)
# - `ax2.bar()` creates bars for 'Rain' on the same 'Day' x-axis
# - `color='lightgreen'` distinguishes rainfall bars from temperature
# - `alpha=0.6` adds transparency to avoid fully overlapping temperature bars
# - `label='Rain'` names this data for the legend
ax2.bar(weather['Day'], weather['Rain'], color='lightgreen', alpha=0.6, label='Rain')

# Step 9: Label the secondary y-axis (rainfall)
# - `set_ylabel()` names the y-axis for rainfall, with units (mm)
# - `color='green'` matches the label to the rainfall bars
ax2.set_ylabel('Rainfall (mm)', color='green')

# Step 10: Customize the secondary y-axis ticks
# - `tick_params()` sets the y-axis tick labels to green, aligning with the bars and label
ax2.tick_params(axis='y', labelcolor='green')

# Step 11: Add a title to the plot
# - `plt.title()` sets a descriptive title at the top of the figure
# - Applies to the entire plot (both axes)
plt.title('Temperature and Rainfall by Day')

# Step 12: Add a legend for both datasets
# - `fig.legend()` creates a combined legend for `ax1` (Temp) and `ax2` (Rain)
# - `loc='upper center'` places it above the plot
# - `bbox_to_anchor=(0.5, -0.05)` shifts it below the plot area (centered)
# - `ncol=2` arranges labels side by side (Temp | Rain)
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2)

# Step 13: Display the plot
# - `plt.show()` renders the figure with both bar charts and dual axes
plt.show()