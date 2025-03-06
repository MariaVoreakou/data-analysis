import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load the dataset
data = pd.read_csv('data/Data.csv')

columns_to_convert = ['Avg_Power_Consumption_mW', 'avg_Message_Rate']
for col in columns_to_convert:
    data[col] = data[col].str.replace(',', '.').astype(float)


numeric_data = data.select_dtypes(include=['float64', 'int64'])

# Calculate the Spearman's rank correlation coefficient matrix
spearman_correlation = numeric_data.corr(method="spearman")

# Create the output directory
output_dir = 'output/Graphs'
os.makedirs(output_dir, exist_ok=True)

# Save the heatmap as a PNG file
plt.figure(figsize=(10, 8))
sns.heatmap(spearman_correlation, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Spearman's Rank Correlation Heatmap")
output_path = os.path.join(output_dir, "Spearman_Correlation_Heatmap.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()

print(f"Heatmap saved to: {output_path}")
