import pandas as pd
import os

# Dictionary with experiment paths
experiments = {
    ################################Data Distribution###########################################
    #100_1_Direct_3_100 vs 100_1_Fanout_3_100
    '100_1_Direct_3_100': {
        "read_path": "data/Data_Distribution/100_1_Direct_3_100/Disk_Read.csv",
        "write_path": "data/Data_Distribution/100_1_Direct_3_100/Disk_Write.csv",
    },
    '100_1_Fanout_3_100': {
        "read_path": "data/Data_Distribution/100_1_Fanout_3_100/Disk_Read.csv",
        "write_path": "data/Data_Distribution/100_1_Fanout_3_100/Disk_Write.csv"
    },

    #100_1_Direct_3_500 vs 100_1_Fanout_3_500
    '100_1_Direct_3_500': {
        "read_path": "data/Data_Distribution/100_1_Direct_3_500/Disk_Read.csv",
        "write_path": "data/Data_Distribution/100_1_Direct_3_500/Disk_Write.csv",
    },
    '100_1_Fanout_3_500': {
        "read_path": "data/Data_Distribution/100_1_Fanout_3_500/Disk_Read.csv",
        "write_path": "data/Data_Distribution/100_1_Fanout_3_500/Disk_Write.csv",

    },

    #100_1_Direct_3_1000 vs 100_1_Fanout_3_1000   
    '100_1_Direct_3_1000': {
        "read_path": "data/Data_Distribution/100_1_Direct_3_1000/Disk_Read.csv",
        "write_path": "data/Data_Distribution/100_1_Direct_3_1000/Disk_Write.csv",
    },
    '100_1_Fanout_3_1000': {
        "read_path": "data/Data_Distribution/100_1_Fanout_3_1000/Disk_Read.csv",
        "write_path": "data/Data_Distribution/100_1_Fanout_3_1000/Disk_Write.csv",
    },
    #300_1_Direct_3_100 vs 300_1_Fanout_3_100
    '300_1_Direct_3_100': {
        "read_path": "data/Data_Distribution/300_1_Direct_3_100/Disk_Read.csv",
        "write_path": "data/Data_Distribution/300_1_Direct_3_100/Disk_Write.csv",
    },
    '300_1_Fanout_3_100': {
        "read_path": "data/Data_Distribution/300_1_Fanout_3_100/Disk_Read.csv",
        "write_path": "data/Data_Distribution/300_1_Fanout_3_100/Disk_Write.csv",
    },

    #300_1_Direct_3_500 vs 300_1_Fanout_3_500
    '300_1_Direct_3_500': {
        "read_path": "data/Data_Distribution/300_1_Direct_3_500/Disk_Read.csv",
        "write_path": "data/Data_Distribution/300_1_Direct_3_500/Disk_Write.csv",
    },
    '300_1_Fanout_3_500': {
        "read_path": "data/Data_Distribution/300_1_Fanout_3_500/Disk_Read.csv",
        "write_path": "data/Data_Distribution/300_1_Fanout_3_500/Disk_Write.csv",
    },

    #300_1_Direct_3_1000 vs 300_1_Fanout_3_1000   
    '300_1_Direct_3_1000': {
        "read_path": "data/Data_Distribution/300_1_Direct_3_1000/Disk_Read.csv",
        "write_path": "data/Data_Distribution/300_1_Direct_3_1000/Disk_Write.csv",
    },
    '300_1_Fanout_3_1000': {
        "read_path": "data/Data_Distribution/300_1_Fanout_3_1000/Disk_Read.csv",
        "write_path": "data/Data_Distribution/300_1_Fanout_3_1000/Disk_Write.csv",
    },

    ################################Account driven###########################################
    #100_1_Direct_100_100 vs 100_1_Fanout_100_100
    '100_1_Direct_100_100': {
        "read_path": "data/Account_Driven/100_1_Direct_100_100/Disk_Read.csv",
        "write_path": "data/Account_Driven/100_1_Direct_100_100/Disk_Write.csv",
    },
    '100_1_Fanout_100_100': {
        "read_path": "data/Account_Driven/100_1_Fanout_100_100/Disk_Read.csv",
        "write_path": "data/Account_Driven/100_1_Fanout_100_100/Disk_Write.csv",
    },

    #100_1_Direct_500_500 vs 100_1_Fanout_500_500
    '100_1_Direct_500_500': {
        "read_path": "data/Account_Driven/100_1_Direct_500_500/Disk_Read.csv",
        "write_path": "data/Account_Driven/100_1_Direct_500_500/Disk_Write.csv",
    },
    '100_1_Fanout_500_500': {
        "read_path": "data/Account_Driven/100_1_Fanout_500_500/Disk_Read.csv",
        "write_path": "data/Account_Driven/100_1_Fanout_500_500/Disk_Write.csv",
    },

    #100_1_Direct_1000_1000 vs 100_1_Fanout_1000_1000   
    '100_1_Direct_1000_1000': {
        "read_path": "data/Account_Driven/100_1_Direct_1000_1000/Disk_Read.csv",
        "write_path": "data/Account_Driven/100_1_Direct_1000_1000/Disk_Write.csv",
    },
    '100_1_Fanout_1000_1000': {
        "read_path": "data/Account_Driven/100_1_Fanout_1000_1000/Disk_Read.csv",
        "write_path": "data/Account_Driven/100_1_Fanout_1000_1000/Disk_Write.csv",
    },
    #300_1_Direct_100_100 vs 300_1_Fanout_100_100
    '300_1_Direct_100_100': {
        "read_path": "data/Account_Driven/300_1_Direct_100_100/Disk_Read.csv",
        "write_path": "data/Account_Driven/300_1_Direct_100_100/Disk_Write.csv",
    },
    '300_1_Fanout_100_100': {
        "read_path": "data/Account_Driven/300_1_Fanout_100_100/Disk_Read.csv",
        "write_path": "data/Account_Driven/300_1_Fanout_100_100/Disk_Write.csv",
    },

    #300_1_Direct_500_500 vs 300_1_Fanout_500_500
    '300_1_Direct_500_500': {
        "read_path": "data/Account_Driven/300_1_Direct_500_500/Disk_Read.csv",
        "write_path": "data/Account_Driven/300_1_Direct_500_500/Disk_Write.csv",
    },
    '300_1_Fanout_500_500': {
        "read_path": "data/Account_Driven/300_1_Fanout_500_500/Disk_Read.csv",
        "write_path": "data/Account_Driven/300_1_Fanout_500_500/Disk_Write.csv",
    },

    #300_1_Direct_1000_1000 vs 300_1_Fanout_1000_1000   
    '300_1_Direct_1000_1000': {
        "read_path": "data/Account_Driven/300_1_Direct_1000_1000/Disk_Read.csv",
        "write_path": "data/Account_Driven/300_1_Direct_1000_1000/Disk_Write.csv",
    },
    '300_1_Fanout_1000_1000': {
        "read_path": "data/Account_Driven/300_1_Fanout_1000_1000/Disk_Read.csv",
        "write_path": "data/Account_Driven/300_1_Fanout_1000_1000/Disk_Write.csv",
    },

    ################################Normal Flows###########################################
    '100_1_Topic_3_3': {
        "read_path": "data/Normal/100_1_Topic_3_3/Disk_Read.csv",
        "write_path": "data/Normal/100_1_Topic_3_3/Disk_Write.csv",
    },
    '100_1_Topic_3_50': {
        "read_path": "data/Normal/100_1_Topic_3_50/Disk_Read.csv",
        "write_path": "data/Normal/100_1_Topic_3_50/Disk_Write.csv",
    },
    '100_1_Topic_3_100': {
        "read_path": "data/Normal/100_1_Topic_3_100/Disk_Read.csv",
        "write_path": "data/Normal/100_1_Topic_3_100/Disk_Write.csv",
    },
    '100_1_Topic_3_500': {
        "read_path": "data/Normal/100_1_Topic_3_500/Disk_Read.csv",
        "write_path": "data/Normal/100_1_Topic_3_500/Disk_Write.csv",
    },
    '100_1_Topic_3_1000': {
        "read_path": "data/Normal/100_1_Topic_3_1000/Disk_Read.csv",
        "write_path": "data/Normal/100_1_Topic_3_1000/Disk_Write.csv",
    },
    '100_1_Topic_100_100': {
        "read_path": "data/Normal/100_1_Topic_100_100/Disk_Read.csv",
        "write_path": "data/Normal/100_1_Topic_100_100/Disk_Write.csv",
    },
    '100_1_Topic_500_500': {
        "read_path": "data/Normal/100_1_Topic_500_500/Disk_Read.csv",
        "write_path": "data/Normal/100_1_Topic_500_500/Disk_Write.csv",
    },
    '100_1_Topic_1000_1000': {
        "read_path": "data/Normal/100_1_Topic_1000_1000/Disk_Read.csv",
        "write_path": "data/Normal/100_1_Topic_1000_1000/Disk_Write.csv",
    },
    '300_1_Topic_3_3': {
        "read_path": "data/Normal/300_1_Topic_3_3/Disk_Read.csv",
        "write_path": "data/Normal/300_1_Topic_3_3/Disk_Write.csv",
    },
    '300_1_Topic_3_50': {
        "read_path": "data/Normal/300_1_Topic_3_50/Disk_Read.csv",
        "write_path": "data/Normal/300_1_Topic_3_50/Disk_Write.csv",
    },
    '300_1_Topic_3_100': {
        "read_path": "data/Normal/300_1_Topic_3_100/Disk_Read.csv",
        "write_path": "data/Normal/300_1_Topic_3_100/Disk_Write.csv",
    },
    '300_1_Topic_3_500': {
        "read_path": "data/Normal/300_1_Topic_3_500/Disk_Read.csv",
        "write_path": "data/Normal/300_1_Topic_3_500/Disk_Write.csv",
    },
    '300_1_Topic_3_1000': {
        "read_path": "data/Normal/300_1_Topic_3_1000/Disk_Read.csv",
        "write_path": "data/Normal/300_1_Topic_3_1000/Disk_Write.csv",
    },
    '300_1_Topic_100_100': {
        "read_path": "data/Normal/300_1_Topic_100_100/Disk_Read.csv",
        "write_path": "data/Normal/300_1_Topic_100_100/Disk_Write.csv",
    },
    '300_1_Topic_500_500': {
        "read_path": "data/Normal/300_1_Topic_500_500/Disk_Read.csv",
        "write_path": "data/Normal/300_1_Topic_500_500/Disk_Write.csv",
    },
    '300_1_Topic_1000_1000': {
        "read_path": "data/Normal/300_1_Topic_1000_1000/Disk_Read.csv",
        "write_path": "data/Normal/300_1_Topic_1000_1000/Disk_Write.csv",
    },
}

# Function to convert values to megabytes (MB)
def convert_to_MB(value):
    if 'kB' in value:
        return float(value.replace(' kB', '')) / 1024
    elif 'MB' in value:
        return float(value.replace(' MB', ''))
    elif 'GB' in value:
        return float(value.replace(' GB', '')) * 1024
    elif 'B' in value:
        return float(value.replace(' B', '')) / (1024 * 1024) 
    else:
        return 0


def process_file(file_path):
    try:
        # Read the CSV file
        data = pd.read_csv(file_path)
        
        # Normalize column names and find the one starting with '/opt/erlang/'
        column_name = next(
            (col for col in data.columns if col.strip().lower().startswith('/opt/erlang/')), None
        )
        
        if column_name is None:
            #print(f"No column starting with '/opt/erlang/' found in {file_path}. Defaulting to zeros.")
            return pd.Series([0] * len(data))
    
        return data[column_name].apply(lambda x: convert_to_MB(x))
    
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return pd.Series([0])


# Process all experiments and calculate average disk access
results = []

for experiment_name, paths in experiments.items():
    write_path = paths.get("write_path")
    read_path = paths.get("read_path")
    
    # Process Write and Read files
    write_data_kB = process_file(write_path) if write_path else pd.Series([0])
    read_data_kB = process_file(read_path) if read_path else pd.Series([0])
    
    # Calculate the average disk access (Read + Write) in kB
    avg_disk_access_kB = (write_data_kB + read_data_kB).mean()
    
    # Append results
    results.append({
        "Experiment": experiment_name,
        "Average Disk Access (MB)": round(avg_disk_access_kB, 2)
    })

# Save results
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

output_file = os.path.join(output_folder, "avg_disk_access_results.csv")
results_df = pd.DataFrame(results)
results_df.to_csv(output_file, index=False)

print(f"Results have been saved to {output_file}.")
