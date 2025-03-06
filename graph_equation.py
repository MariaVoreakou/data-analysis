import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import os

# Load the dataset
file_path = 'data/Data.csv'
data = pd.read_csv(file_path)

# Select relevant columns for analysis
relevant_columns = ["Routing_Keys", "avg_Message_Rate", "Queues ", "Consumers", "Avg_Power_Consumption_mW"]
subset_data = data[relevant_columns].copy()

# Clean and preprocess the data
subset_data.rename(columns={"Queues ": "Queues", "Avg_Power_Consumption_mW": "avg_Power_Consumption"}, inplace=True)

# Replace commas with dots and convert to float
subset_data["avg_Message_Rate"] = subset_data["avg_Message_Rate"].replace(',', '.', regex=True).astype(float)
subset_data["avg_Power_Consumption"] = subset_data["avg_Power_Consumption"].replace(',', '.', regex=True).astype(float)

# Prepare data for regression
X = subset_data[["Routing_Keys", "avg_Message_Rate", "Queues", "Consumers"]]
y = subset_data["avg_Power_Consumption"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Fit a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate the model's R-squared value
r2 = r2_score(y_test, y_pred)

# Get the model coefficients
coefficients = model.coef_
intercept = model.intercept_

# Formulate the equation
equation = f"avg_Power_Consumption = {intercept:.2f} + " + " + ".join(
    [f"({coef:.2f} * {col})" for coef, col in zip(coefficients, X.columns)]
)

# Print the equation and R-squared value
print(f"Equation: {equation}")
print(f"R-squared: {r2:.2f}")

# Create a graph to visualize predicted vs actual values
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7, label="Predicted vs Actual")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label="Ideal Fit")
plt.title("Predicted vs Actual Power Consumption")
plt.xlabel("Actual Power Consumption")
plt.ylabel("Predicted Power Consumption")
plt.legend()
plt.grid(True)

# Save the graph
output_dir = 'output/Graphs'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "Predicted_vs_Actual_Power_Consumption.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.show()

print(f"Graph saved to: {output_path}")
