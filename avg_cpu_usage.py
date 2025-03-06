import pandas as pd
import os
import re

# Dictionary with experiment paths
experiments = {
    ################################Data Distribution###########################################
    #100_1_Direct_3_100 vs 100_1_Fanout_3_100
    '100_1_Direct_3_100': {
        "cpu_path": "data/Data_Distribution/100_1_Direct_3_100/Scaph_Process_Cpu.csv",
    },
    '100_1_Fanout_3_100': {
        "cpu_path": "data/Data_Distribution/100_1_Fanout_3_100/Scaph_Process_Cpu.csv",
    },

    #100_1_Direct_3_500 vs 100_1_Fanout_3_500
    '100_1_Direct_3_500': {
        "cpu_path": "data/Data_Distribution/100_1_Direct_3_500/Scaph_Process_Cpu.csv",
    },
    '100_1_Fanout_3_500': {
        "cpu_path": "data/Data_Distribution/100_1_Fanout_3_500/Scaph_Process_Cpu.csv",
    },

    #100_1_Direct_3_1000 vs 100_1_Fanout_3_1000   
    '100_1_Direct_3_1000': {
        "cpu_path": "data/Data_Distribution/100_1_Direct_3_1000/Scaph_Process_Cpu.csv",
    },
    '100_1_Fanout_3_1000': {
        "cpu_path": "data/Data_Distribution/100_1_Fanout_3_1000/Scaph_Process_Cpu.csv",
    },
    #300_1_Direct_3_100 vs 300_1_Fanout_3_100
    '300_1_Direct_3_100': {
        "cpu_path": "data/Data_Distribution/300_1_Direct_3_100/Scaph_Process_Cpu.csv",
    },
    '300_1_Fanout_3_100': {
        "cpu_path": "data/Data_Distribution/300_1_Fanout_3_100/Scaph_Process_Cpu.csv",
    },

    #300_1_Direct_3_500 vs 300_1_Fanout_3_500
    '300_1_Direct_3_500': {
        "cpu_path": "data/Data_Distribution/300_1_Direct_3_500/Scaph_Process_Cpu.csv",
    },
    '300_1_Fanout_3_500': {
        "cpu_path": "data/Data_Distribution/300_1_Fanout_3_500/Scaph_Process_Cpu.csv",
    },

    #300_1_Direct_3_1000 vs 300_1_Fanout_3_1000   
    '300_1_Direct_3_1000': {
        "cpu_path": "data/Data_Distribution/300_1_Direct_3_1000/Scaph_Process_Cpu.csv",
    },
    '300_1_Fanout_3_1000': {
        "cpu_path": "data/Data_Distribution/300_1_Fanout_3_1000/Scaph_Process_Cpu.csv",
    },

    ################################Account driven###########################################
    #100_1_Direct_100_100 vs 100_1_Fanout_100_100
    '100_1_Direct_100_100': {
        "cpu_path": "data/Account_Driven/100_1_Direct_100_100/Scaph_Process_Cpu.csv",
    },
    '100_1_Fanout_100_100': {
        "cpu_path": "data/Account_Driven/100_1_Fanout_100_100/Scaph_Process_Cpu.csv",
    },

    #100_1_Direct_500_500 vs 100_1_Fanout_500_500
    '100_1_Direct_500_500': {
        "cpu_path": "data/Account_Driven/100_1_Direct_500_500/Scaph_Process_Cpu.csv",
    },
    '100_1_Fanout_500_500': {
        "cpu_path": "data/Account_Driven/100_1_Fanout_500_500/Scaph_Process_Cpu.csv",
    },

    #100_1_Direct_1000_1000 vs 100_1_Fanout_1000_1000   
    '100_1_Direct_1000_1000': {
        "cpu_path": "data/Account_Driven/100_1_Direct_1000_1000/Scaph_Process_Cpu.csv",
    },
    '100_1_Fanout_1000_1000': {
        "cpu_path": "data/Account_Driven/100_1_Fanout_1000_1000/Scaph_Process_Cpu.csv",
    },
    #300_1_Direct_100_100 vs 300_1_Fanout_100_100
    '300_1_Direct_100_100': {
        "cpu_path": "data/Account_Driven/300_1_Direct_100_100/Scaph_Process_Cpu.csv",
    },
    '300_1_Fanout_100_100': {
        "cpu_path": "data/Account_Driven/300_1_Fanout_100_100/Scaph_Process_Cpu.csv",
    },

    #300_1_Direct_500_500 vs 300_1_Fanout_500_500
    '300_1_Direct_500_500': {
        "cpu_path": "data/Account_Driven/300_1_Direct_500_500/Scaph_Process_Cpu.csv",
    },
    '300_1_Fanout_500_500': {
        "cpu_path": "data/Account_Driven/300_1_Fanout_500_500/Scaph_Process_Cpu.csv",
    },

    #300_1_Direct_1000_1000 vs 300_1_Fanout_1000_1000   
    '300_1_Direct_1000_1000': {
        "cpu_path": "data/Account_Driven/300_1_Direct_1000_1000/Scaph_Process_Cpu.csv",
    },
    '300_1_Fanout_1000_1000': {
        "cpu_path": "data/Account_Driven/300_1_Fanout_1000_1000/Scaph_Process_Cpu.csv",
    },

    ################################Normal Flows###########################################
    '100_1_Topic_3_3': {
        "cpu_path": "data/Normal/100_1_Topic_3_3/Scaph_Process_Cpu.csv",
    },
    '100_1_Topic_3_50': {
        "cpu_path": "data/Normal/100_1_Topic_3_50/Scaph_Process_Cpu.csv",
    },
    '100_1_Topic_3_100': {
        "cpu_path": "data/Normal/100_1_Topic_3_100/Scaph_Process_Cpu.csv",
    },
    '100_1_Topic_3_500': {
        "cpu_path": "data/Normal/100_1_Topic_3_500/Scaph_Process_Cpu.csv",
    },
    '100_1_Topic_3_1000': {
        "cpu_path": "data/Normal/100_1_Topic_3_1000/Scaph_Process_Cpu.csv",
    },
    '100_1_Topic_100_100': {
        "cpu_path": "data/Normal/100_1_Topic_100_100/Scaph_Process_Cpu.csv",
    },
    '100_1_Topic_500_500': {
        "cpu_path": "data/Normal/100_1_Topic_500_500/Scaph_Process_Cpu.csv",
    },
    '100_1_Topic_1000_1000': {
        "cpu_path": "data/Normal/100_1_Topic_1000_1000/Scaph_Process_Cpu.csv",
    },
    '300_1_Topic_3_3': {
        "cpu_path": "data/Normal/300_1_Topic_3_3/Scaph_Process_Cpu.csv",
    },
    '300_1_Topic_3_50': {
        "cpu_path": "data/Normal/300_1_Topic_3_50/Scaph_Process_Cpu.csv",
    },
    '300_1_Topic_3_100': {
        "cpu_path": "data/Normal/300_1_Topic_3_100/Scaph_Process_Cpu.csv",
    },
    '300_1_Topic_3_500': {
        "cpu_path": "data/Normal/300_1_Topic_3_500/Scaph_Process_Cpu.csv",
    },
    '300_1_Topic_3_1000': {
        "cpu_path": "data/Normal/300_1_Topic_3_1000/Scaph_Process_Cpu.csv",
    },
    '300_1_Topic_100_100': {
        "cpu_path": "data/Normal/300_1_Topic_100_100/Scaph_Process_Cpu.csv",
    },
    '300_1_Topic_500_500': {
        "cpu_path": "data/Normal/300_1_Topic_500_500/Scaph_Process_Cpu.csv",
    },
    '300_1_Topic_1000_1000': {
        "cpu_path": "data/Normal/300_1_Topic_1000_1000/Scaph_Process_Cpu.csv",
    },
}

def convert_to_numeric(value):
    """Converts cpu usage strings to a numeric value."""
    try:
        if '%' in value:
            return float(value.replace(' %', ''))
        else:
            return 0
    except:
        return 0

def process_file(file_path):
    """Processes a CSV file to calculate row-wise summaries of 'erlang' columns."""
    try:
        # Read the CSV file
        data = pd.read_csv(file_path)

        erlang_columns = [col for col in data.columns if re.search(r'erlang', col, re.IGNORECASE)]

        if not erlang_columns:
            print(f"No 'erlang' columns found in {file_path}")
            return None

        # Convert all 'erlang' column values to numeric
        data[erlang_columns] = data[erlang_columns].map(convert_to_numeric)

        # Summarize row-wise for 'erlang' columns
        data['erlang_sum'] = data[erlang_columns].sum(axis=1)

        # Calculate the average for this scenario
        average_erlang_sum = data['erlang_sum'].mean()

        return average_erlang_sum

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return None

# Collect results for all experiments
results = []

for experiment_name, paths in experiments.items():
    cpu_path = paths.get("cpu_path")

    if not cpu_path or not os.path.exists(cpu_path):
        print(f"Memory path missing or file not found for {experiment_name}")
        continue

    # Process the file and calculate the average of 'erlang' sums
    average_erlang_sum = process_file(cpu_path)

    if average_erlang_sum is not None:
        results.append({
            "Experiment": experiment_name,
            "Average CPU usage of Erlang Processes (%)": round(average_erlang_sum, 2)
        })

# Save results to a file
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

output_file = os.path.join(output_folder, "avg_cpu_results.csv")
results_df = pd.DataFrame(results)
results_df.to_csv(output_file, index=False)

print(f"Average CPU results have been saved to {output_file}.")