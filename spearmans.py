import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load the dataset
data = pd.read_csv('data/Data.csv')

# Select only numeric columns
numeric_data = data.select_dtypes(include=['float64', 'int64'])

# Calculate the Spearman's rank correlation coefficient matrix
spearman_correlation = numeric_data.corr(method="spearman")

# Create the output directory if it doesn't exist
output_dir = 'output/'
os.makedirs(output_dir, exist_ok=True)

# Save the heatmap as a PNG file
plt.figure(figsize=(10, 8))
sns.heatmap(spearman_correlation, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Spearman's Rank Correlation Heatmap")
output_path = os.path.join(output_dir, "Spearman_Correlation_Heatmap.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()

print(f"Heatmap saved to: {output_path}")
