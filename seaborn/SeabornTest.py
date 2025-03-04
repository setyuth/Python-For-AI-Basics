import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# print(sns.__file__)
# print(plt.__file__)
# print(pd.__file__)

# Let’s start with a simple example using the student data from previous parts:
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dana'],
    'Math': [85, 92, 78, 95],
    'Science': [88, 85, 90, 92]
}
df = pd.DataFrame(data)

# Simple scatter plot using Seaborn
sns.lmplot(x='Math', y='Science', data=df, fit_reg=False)
plt.title('Math vs. Science Scores')
plt.show()

# Sample dataset for testing Seaborn features
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dana', 'Eve', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Math': [85, 92, 78, 95, 88, 65, 90, 82, 77, 94],
    'Science': [88, 85, 90, 92, 80, 70, 87, 83, 79, 91],
    'English': [90, 88, 85, 93, 87, 75, 89, 84, 80, 92],
    'Study_Hours': [5, 6, 4, 7, 5.5, 3, 6.5, 4.5, 4, 6],
    'Grade_Level': ['Freshman', 'Sophomore', 'Freshman', 'Sophomore', 'Freshman', 'Freshman', 'Sophomore', 'Sophomore', 'Freshman', 'Sophomore'],
    'Pass': [True, True, False, True, True, False, True, True, False, True]
}
df = pd.DataFrame(data)

# 1. Pair Plot
# Create a pair plot with Seaborn
sns.pairplot(
    df,                         # DataFrame to plot
    hue='Grade_Level',          # Color points by Grade_Level (Freshman vs Sophomore)
    vars=['Math', 'Science', 'English', 'Study_Hours'],  # Select numerical columns to compare
    markers=['o', 's']          # Use circles for Freshman, squares for Sophomore
)
# Display the plot
plt.show()

# 2. Heatmap: Display a correlation matrix:
# Calculate correlation matrix for numerical columns
corr = df[['Math', 'Science', 'English', 'Study_Hours']].corr()
# Create a heatmap
sns.heatmap(
    corr,              # Correlation matrix to plot
    annot=True,        # Show correlation values on the heatmap
    cmap='coolwarm',   # Use red (positive) to blue (negative) color scheme
    vmin=-1, vmax=1    # Set color scale range from -1 to 1
)
# Add a title
plt.title('Correlation Heatmap of Student Metrics')
# Display the plot
plt.show()

# 3. Violin Plot: Distribution by Category
# A violin plot shows the distribution of a numerical variable across categories:
# Create a violin plot
sns.violinplot(
    x='Grade_Level',    # Categorical variable for x-axis (Freshman vs Sophomore)
    y='Math',           # Numerical variable for y-axis (Math scores)
    data=df             # DataFrame source
)
# Add a title
plt.title('Math Score Distribution by Grade Level')
# Display the plot
plt.show()

# 4. Swarm Plot: Individual Points
# A swarm plot displays individual data points without overlap:
# Create a swarm plot
sns.swarmplot(
    x='Pass',           # Categorical variable for x-axis (True vs False)
    y='Science',        # Numerical variable for y-axis (Science scores)
    data=df,            # DataFrame source
    hue='Grade_Level'   # Color points by Grade_Level
)
# Add a title
plt.title('Science Scores by Pass Status')
# Display the plot
plt.show()

# 5. Box Plot (Bonus): Comparing Distributions
# A box plot summarizes numerical data distributions across multiple variables:
# Create a horizontal box plot for multiple columns
sns.boxplot(
    data=df[['Math', 'Science', 'English']],  # Select numerical columns to plot
    orient='h' # Horizontal orientation for readability
)
# Add a title
plt.title('Box Plot of Student Scores Across Subjects')
# Display the plot
plt.show()

# An Exercise:
# Using the student dataset, try these tasks:
# 1. Create a box plot of English scores by Grade_Level.
# 2. Create a heatmap of correlations excluding Study_Hours.
# 3. Create a violin plot of Study_Hours by Pass status.
# Hint: Use sns.boxplot for ranges, df.corr() for correlations,
# and sns.violinplot for distributions.

# 1. Box plot of English scores by Grade_Level
sns.boxplot(
    x='Grade_Level',    # Categorical x-axis (Freshman vs Sophomore)
    y='English',        # Numerical y-axis (English scores)
    data=df             # DataFrame source
)
plt.title('English Scores by Grade Level')  # Add a descriptive title
plt.show()          # Display the plot

# 2. Heatmap of correlations excluding Study_Hours
corr = df[['Math', 'Science', 'English']].corr()  # Calculate correlations for selected columns
sns.heatmap(
    corr,              # Correlation matrix to plot
    annot=True,        # Display correlation values
    cmap='coolwarm'    # Color scheme for visual clarity
)
plt.title('Correlation Heatmap (Excluding Study_Hours)')  # Title for context
plt.show()          # Display the plot

# 3. Violin plot of Study_Hours by Pass status
sns.violinplot(
    x='Pass',           # Categorical x-axis (True vs False)
    y='Study_Hours',    # Numerical y-axis (study hours)
    data=df             # DataFrame source
)
plt.title('Study Hours by Pass Status')  # Add a title
plt.show() # Display the plot



