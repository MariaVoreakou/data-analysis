import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the file
file_path = 'data/scenarios_paper.csv'
data = pd.read_csv(file_path)

# Clean the data by removing the " W" unit and converting to numeric values
for column in data.columns[1:]:
    data[column] = data[column].str.replace(' W', '').astype(float)

# Convert the Time column to a proper datetime format
data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S')

# Calculate the average power consumption for each scenario
averages = {column: data[column].mean() for column in data.columns[1:]}

# Plot the data with the average power consumption as dashed lines
plt.figure(figsize=(12, 6))

# Plot each scenario
for column in data.columns[1:]:
    plt.plot(data['Time'], data[column], label=column)

# Add dashed lines for averages
for i, (column, avg) in enumerate(averages.items()):
    avg_label = f"{column} Avg ({avg:.2f} W)"  # Add the average value to the label
    plt.axhline(y=avg, linestyle='--', label=avg_label, color=plt.gca().lines[i].get_color())

#plt.title("Overtime Power Consumption & Averages")
plt.xlabel("Time (Minutes)")
plt.ylabel("Power Consumption (W)")

# Adjust the legend to appear at the bottom
plt.legend(title="Scenarios and Averages", loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4)

plt.grid(True)
plt.tight_layout()
plt.show()
