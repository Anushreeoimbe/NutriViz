import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "nutrients_csvfile.csv"  # Update path if needed
nutrients_df = pd.read_csv(file_path)

# Convert necessary columns to numeric (handling 't' values)
numeric_cols = ['Grams', 'Calories', 'Protein', 'Fat', 'Sat.Fat', 'Fiber', 'Carbs']
for col in numeric_cols:
    nutrients_df[col] = pd.to_numeric(nutrients_df[col], errors='coerce')

# Drop rows with NaN values after conversion
nutrients_df.dropna(inplace=True)

# Set style
sns.set_style("whitegrid")

# 1. Histogram - Distribution of Calories
plt.figure(figsize=(8, 5))
sns.histplot(nutrients_df['Calories'], bins=20, kde=True, color='blue')
plt.title('Distribution of Calories')
plt.xlabel('Calories')
plt.ylabel('Frequency')
plt.savefig("calories_distribution.png")
plt.show()

# 2. Bar Plot - Average Protein Content by Category
plt.figure(figsize=(10, 5))
category_avg_protein = nutrients_df.groupby('Category')['Protein'].mean().sort_values()
category_avg_protein.plot(kind='bar', color='green')
plt.title('Average Protein Content by Category')
plt.xlabel('Category')
plt.ylabel('Protein (g)')
plt.xticks(rotation=45)
plt.show()

# 3. Pie Chart - Fat Distribution Across Categories
plt.figure(figsize=(7, 7))
category_fat = nutrients_df.groupby('Category')['Fat'].sum()
category_fat.plot(kind='pie', autopct='%1.1f%%', startangle=140, cmap='Set3')
plt.title('Fat Distribution by Food Category')
plt.show()

# 4. Scatter Plot - Calories vs. Protein
plt.figure(figsize=(8, 5))
sns.scatterplot(x=nutrients_df['Calories'], y=nutrients_df['Protein'], alpha=0.7, color='red')
plt.title('Calories vs. Protein Content')
plt.xlabel('Calories')
plt.ylabel('Protein (g)')
plt.show()

# 5. Box Plot - Fat Content Variation by Category
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Fat', data=nutrients_df, palette='coolwarm')
plt.xticks(rotation=45)
plt.title('Fat Content Variation by Food Category')
plt.show()

# 6. Pairplot - Relationships between Numerical Features
pairplot_fig = sns.pairplot(nutrients_df[numeric_cols], diag_kind='kde')
plt.show()

# 7. Heatmap - Correlation Between Nutritional Factors
plt.figure(figsize=(10, 6))
sns.heatmap(nutrients_df[numeric_cols].corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Between Nutritional Factors')
plt.show()

# 8. Violin Plot - Distribution of Calories by Category
plt.figure(figsize=(10, 6))
sns.violinplot(x='Category', y='Calories', data=nutrients_df, palette='muted')
plt.xticks(rotation=45)
plt.title('Distribution of Calories by Category')
plt.show()

# 9. Line Plot - Trends in Calories Over Food Categories
plt.figure(figsize=(10, 5))
category_calories_trend = nutrients_df.groupby('Category')['Calories'].mean()
category_calories_trend.plot(kind='line', marker='o', color='purple')
plt.title('Average Calories per Category')
plt.xlabel('Category')
plt.ylabel('Calories')
plt.xticks(rotation=45)
plt.show()

# 10. Top 5 Foods High in Protein
plt.figure(figsize=(8, 5))
top_protein = nutrients_df.nlargest(5, 'Protein')[['Food', 'Protein']]
sns.barplot(x='Protein', y='Food', data=top_protein, palette='Blues_r')
plt.title('Top 5 Foods High in Protein')
plt.xlabel('Protein (g)')
plt.ylabel('Food')
plt.show()

# 11. Top 5 Foods High in Fat
plt.figure(figsize=(8, 5))
top_fat = nutrients_df.nlargest(5, 'Fat')[['Food', 'Fat']]
sns.barplot(x='Fat', y='Food', data=top_fat, palette='Reds_r')
plt.title('Top 5 Foods High in Fat')
plt.xlabel('Fat (g)')
plt.ylabel('Food')
plt.show()


print("All visualizations generated and saved successfully!")
