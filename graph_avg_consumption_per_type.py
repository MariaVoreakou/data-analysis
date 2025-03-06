import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'data/Data.csv'
data = pd.read_csv(file_path)

# Clean and preprocess the data
data['Avg_Power_Consumption_mW'] = data['Avg_Power_Consumption_mW'].str.replace(',', '').astype(float)

# Clean the 'Type' column by stripping whitespace
data['Type'] = data['Type'].str.strip()

# Group by 'Type' and calculate the mean of 'Avg_Power_Consumption_mW'
avg_consumption_per_type_cleaned = data.groupby('Type')['Avg_Power_Consumption_mW'].mean()

# Plot the results
plt.figure(figsize=(8, 6))
avg_consumption_per_type_cleaned.plot(kind='bar', color='skyblue')
plt.title('Average Power Consumption per Exchange Type')
plt.xlabel('Type')
plt.ylabel('Average Power Consumption (mW)')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot as a PNG file
output_path = 'output/Graphs/average_power_consumption_per_type.png'
plt.savefig(output_path)

# Show the plot
plt.show()

print(f"Plot saved as {output_path}")
