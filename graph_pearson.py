import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load the dataset
file_path = 'data/Data.csv'
data = pd.read_csv(file_path)

columns_to_convert = ['Avg_Power_Consumption_mW', 'avg_Message_Rate']
for col in columns_to_convert:
    data[col] = data[col].str.replace(',', '.').astype(float)


numeric_data = data.select_dtypes(include=['float64', 'int64'])

# Calculate the Pearson correlation matrix
pearson_correlation = numeric_data.corr(method="pearson")

# Create the output directory if it doesn't exist
output_dir = 'output/Graphs'
os.makedirs(output_dir, exist_ok=True)

# Create and save the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(pearson_correlation, annot=True, cmap='coolwarm', fmt=".2f", cbar=True)
plt.title("Pearson Correlation Heatmap")
output_path = os.path.join(output_dir, "Pearson_Correlation_Heatmap.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()

print(f"Pearson correlation heatmap saved to: {output_path}")
