import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# File path
file_path = "data/2k-factorial/data.csv"

# Load the dataset
df = pd.read_csv(file_path)

# Display the first few rows to understand the structure
df.head()


# Convert numeric columns (replace commas with dots and convert to float)
numeric_cols = ["Avg_Power_Consumption_mW", "avg_disk_access_MB", "avg_cpu_usage_%", "avg_memory_usage_MB"]
df[numeric_cols] = df[numeric_cols].replace({",": "."}, regex=True).astype(float)

# Extract relevant input columns
input_cols = ["Messages_rate", "Routing_Keys", "Exchanges", "Consumers-Queues"]
output_cols = numeric_cols

# Normalize input factors to (-1, +1) using min-max scaling
normalized_df = df.copy()
for col in input_cols:
    min_val, max_val = df[col].min(), df[col].max()
    normalized_df[col] = (2 * (df[col] - min_val) / (max_val - min_val)) - 1

# Display the cleaned and normalized data
normalized_df.head()

# Generate interaction terms
interaction_terms = {
    "Messages_Routing": normalized_df["Messages_rate"] * normalized_df["Routing_Keys"],
    "Messages_Exchanges": normalized_df["Messages_rate"] * normalized_df["Exchanges"],
    "Messages_Consumers": normalized_df["Messages_rate"] * normalized_df["Consumers-Queues"],
    "Routing_Exchanges": normalized_df["Routing_Keys"] * normalized_df["Exchanges"],
    "Routing_Consumers": normalized_df["Routing_Keys"] * normalized_df["Consumers-Queues"],
    "Exchanges_Consumers": normalized_df["Exchanges"] * normalized_df["Consumers-Queues"],
    "Messages_Routing_Exchanges": normalized_df["Messages_rate"] * normalized_df["Routing_Keys"] * normalized_df["Exchanges"],
    "Messages_Routing_Consumers": normalized_df["Messages_rate"] * normalized_df["Routing_Keys"] * normalized_df["Consumers-Queues"],
    "Messages_Exchanges_Consumers": normalized_df["Messages_rate"] * normalized_df["Exchanges"] * normalized_df["Consumers-Queues"],
    "Routing_Exchanges_Consumers": normalized_df["Routing_Keys"] * normalized_df["Exchanges"] * normalized_df["Consumers-Queues"],
    "Messages_Routing_Exchanges_Consumers": normalized_df["Messages_rate"] * normalized_df["Routing_Keys"] * normalized_df["Exchanges"] * normalized_df["Consumers-Queues"]
}

# Add interaction terms to the dataframe
for key, value in interaction_terms.items():
    normalized_df[key] = value

# Select relevant columns for the summary table
summary_df = normalized_df[["Experiment name", "Messages_rate", "Routing_Keys", "Exchanges", "Consumers-Queues"] +
                           list(interaction_terms.keys()) + output_cols]

# Export the summary table as CSV
export_path = "output/factorial_design_summary.csv"
summary_df.to_csv(export_path, index=False)

# Show the first few rows of the final dataset
summary_df.head()


# Create the output directory if it doesn't exist
output_dir = 'output/Graphs'
os.makedirs(output_dir, exist_ok=True)

# Set plot style
sns.set_theme(style="whitegrid")

# Correlation heatmap
plt.figure(figsize=(12, 8))
corr_matrix = summary_df.drop(columns=["Experiment name"]).corr()  # Remove non-numeric column
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap of Factors and Responses")
plt.show()

output_path = os.path.join(output_dir, "Correlation_Heatmap_Factors_Responses.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()

print(f"Correlation heatmap saved to: {output_path}")



# Define response variable
response_var = "Avg_Power_Consumption_mW"  # Change to other responses as needed

# Pairplot to visualize relationships
sns.pairplot(summary_df, vars=["Messages_rate", "Routing_Keys", "Exchanges", "Consumers-Queues", response_var], diag_kind="kde")
plt.title("Pairplot")
plt.show()

output_path = os.path.join(output_dir, "Pairplot.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()

print(f"Pairplot saved to: {output_path}")