# data-analysis
Repository with useful python files to get analyses (Correlation and regression analysis), avg consumptions, and more.
The following python files are used for csvs exported through grafana using Scaphandre, in order to measure energy consumption on a project with RabbitMQ.

## 🛠️ How to Run the Python Script for RabbitMQ Experiment Analysis
Below are step-by-step instructions on how to run the script on your local machine or a remote environment.

### 📦 1. Prerequisites
Make sure you have the following installed:

- Python 3.x

Required Python Libraries:

```bash
pip install pandas matplotlib statsmodels fpdf python-pptx
```
A code editor (e.g., VS Code, PyCharm) or a terminal.


### 📝 3. Save the Data
The Data should have the project structure as below:

```java
rabbitmq_analysis/
├── data/
│   ├── exp1/exp1_disk_read.csv
│   ├── ...
│   ├── exp2/exp1_disk_write.csv
│   ├── ...
├── output/
├── avg_power_consumption.py
├── equation.py
├── pearson.py
├── spearmans.py
```
### ▶️ 4. Run the Script

Open your terminal, select the .py file, and run:

```bash
python [filename].py
```

✅ Expected Outputs:
- Visualizations will appear during execution.
- Summary statistics and regression outputs will print in the terminal or will be automatically saved in the `output` folder.