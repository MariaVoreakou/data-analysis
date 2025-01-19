import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load the dataset
file_path = 'data/Data.csv'
data = pd.read_csv(file_path)

# Extract relevant columns and clean column names
data_subset = data[["Routing_Keys", "avg_Message_Rate", "Queues ", "Avg_Power_Consumption_mW"]].copy()
data_subset.rename(columns={"Queues ": "Queues", "Avg_Power_Consumption_mW": "avg_Power_Consumption"}, inplace=True)

# Clean and convert columns to numeric types
data_subset["avg_Message_Rate"] = data_subset["avg_Message_Rate"].replace(',', '.', regex=True).astype(float)
data_subset["Routing_Keys"] = data_subset["Routing_Keys"].astype(int)
data_subset["Queues"] = data_subset["Queues"].astype(int)
data_subset["avg_Power_Consumption"] = data_subset["avg_Power_Consumption"].replace(',', '.', regex=True).astype(float)


# Calculate the Pearson correlation matrix
pearson_correlation = data_subset.corr(method="pearson")

# Create the output directory if it doesn't exist
output_dir = 'output/'
os.makedirs(output_dir, exist_ok=True)

# Create and save the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(pearson_correlation, annot=True, cmap='coolwarm', fmt=".2f", cbar=True)
plt.title("Pearson Correlation Heatmap")
output_path = os.path.join(output_dir, "Pearson_Correlation_Heatmap.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()

print(f"Pearson correlation heatmap saved to: {output_path}")
