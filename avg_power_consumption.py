import pandas as pd
import os

# Dictionary with experiment paths
experiments = {
    ################################Data Distribution###########################################
    #100_1_Direct_3_100 vs 100_1_Fanout_3_100
    '100_1_Direct_3_100': {
        "power_path": "data/Data_Distribution/100_1_Direct_3_100/Power_Consumption_Cmdline.csv",
    },
    '100_1_Fanout_3_100': {
        "power_path": "data/Data_Distribution/100_1_Fanout_3_100/Power_Consumption_Cmdline.csv",
    },

    #100_1_Direct_3_500 vs 100_1_Fanout_3_500
    '100_1_Direct_3_500': {
        "power_path": "data/Data_Distribution/100_1_Direct_3_500/Power_Consumption_Cmdline.csv",
    },
    '100_1_Fanout_3_500': {
        "power_path": "data/Data_Distribution/100_1_Fanout_3_500/Power_Consumption_Cmdline.csv",
    },

    #100_1_Direct_3_1000 vs 100_1_Fanout_3_1000   
    '100_1_Direct_3_1000': {
        "power_path": "data/Data_Distribution/100_1_Direct_3_1000/Power_Consumption_Cmdline.csv",
    },
    '100_1_Fanout_3_1000': {
        "power_path": "data/Data_Distribution/100_1_Fanout_3_1000/Power_Consumption_Cmdline.csv",
    },
    #300_1_Direct_3_100 vs 300_1_Fanout_3_100
    '300_1_Direct_3_100': {
        "power_path": "data/Data_Distribution/300_1_Direct_3_100/Power_Consumption_Cmdline.csv",
    },
    '300_1_Fanout_3_100': {
        "power_path": "data/Data_Distribution/300_1_Fanout_3_100/Power_Consumption_Cmdline.csv",
    },

    #300_1_Direct_3_500 vs 300_1_Fanout_3_500
    '300_1_Direct_3_500': {
        "power_path": "data/Data_Distribution/300_1_Direct_3_500/Power_Consumption_Cmdline.csv",
    },
    '300_1_Fanout_3_500': {
        "power_path": "data/Data_Distribution/300_1_Fanout_3_500/Power_Consumption_Cmdline.csv",
    },

    #300_1_Direct_3_1000 vs 300_1_Fanout_3_1000   
    '300_1_Direct_3_1000': {
        "power_path": "data/Data_Distribution/300_1_Direct_3_1000/Power_Consumption_Cmdline.csv",
    },
    '300_1_Fanout_3_1000': {
        "power_path": "data/Data_Distribution/300_1_Fanout_3_1000/Power_Consumption_Cmdline.csv",
    },

    ################################Account driven###########################################
    #100_1_Direct_100_100 vs 100_1_Fanout_100_100
    '100_1_Direct_100_100': {
        "power_path": "data/Account_Driven/100_1_Direct_100_100/Power_Consumption_Cmdline.csv",
    },
    '100_1_Fanout_100_100': {
        "power_path": "data/Account_Driven/100_1_Fanout_100_100/Power_Consumption_Cmdline.csv",
    },

    #100_1_Direct_500_500 vs 100_1_Fanout_500_500
    '100_1_Direct_500_500': {
        "power_path": "data/Account_Driven/100_1_Direct_500_500/Power_Consumption_Cmdline.csv",
    },
    '100_1_Fanout_500_500': {
        "power_path": "data/Account_Driven/100_1_Fanout_500_500/Power_Consumption_Cmdline.csv",
    },

    #100_1_Direct_1000_1000 vs 100_1_Fanout_1000_1000   
    '100_1_Direct_1000_1000': {
        "power_path": "data/Account_Driven/100_1_Direct_1000_1000/Power_Consumption_Cmdline.csv",
    },
    '100_1_Fanout_1000_1000': {
        "power_path": "data/Account_Driven/100_1_Fanout_1000_1000/Power_Consumption_Cmdline.csv",
    },
    #300_1_Direct_100_100 vs 300_1_Fanout_100_100
    '300_1_Direct_100_100': {
        "power_path": "data/Account_Driven/300_1_Direct_100_100/Power_Consumption_Cmdline.csv",
    },
    '300_1_Fanout_100_100': {
        "power_path": "data/Account_Driven/300_1_Fanout_100_100/Power_Consumption_Cmdline.csv",
    },

    #300_1_Direct_500_500 vs 300_1_Fanout_500_500
    '300_1_Direct_500_500': {
        "power_path": "data/Account_Driven/300_1_Direct_500_500/Power_Consumption_Cmdline.csv",
    },
    '300_1_Fanout_500_500': {
        "power_path": "data/Account_Driven/300_1_Fanout_500_500/Power_Consumption_Cmdline.csv",
    },

    #300_1_Direct_1000_1000 vs 300_1_Fanout_1000_1000   
    '300_1_Direct_1000_1000': {
        "power_path": "data/Account_Driven/300_1_Direct_1000_1000/Power_Consumption_Cmdline.csv",
    },
    '300_1_Fanout_1000_1000': {
        "power_path": "data/Account_Driven/300_1_Fanout_1000_1000/Power_Consumption_Cmdline.csv",
    },

    ################################Normal Flows###########################################
    '100_1_Topic_3_3': {
        "power_path": "data/Normal/100_1_Topic_3_3/Power_Consumption_Cmdline.csv",
    },
    '100_1_Topic_3_50': {
        "power_path": "data/Normal/100_1_Topic_3_50/Power_Consumption_Cmdline.csv",
    },
    '100_1_Topic_3_100': {
        "power_path": "data/Normal/100_1_Topic_3_100/Power_Consumption_Cmdline.csv",
    },
    '100_1_Topic_3_500': {
        "power_path": "data/Normal/100_1_Topic_3_500/Power_Consumption_Cmdline.csv",
    },
    '100_1_Topic_3_1000': {
        "power_path": "data/Normal/100_1_Topic_3_1000/Power_Consumption_Cmdline.csv",
    },
    '100_1_Topic_100_100': {
        "power_path": "data/Normal/100_1_Topic_100_100/Power_Consumption_Cmdline.csv",
    },
    '100_1_Topic_500_500': {
        "power_path": "data/Normal/100_1_Topic_500_500/Power_Consumption_Cmdline.csv",
    },
    '100_1_Topic_1000_1000': {
        "power_path": "data/Normal/100_1_Topic_1000_1000/Power_Consumption_Cmdline.csv",
    },
    '300_1_Topic_3_3': {
        "power_path": "data/Normal/300_1_Topic_3_3/Power_Consumption_Cmdline.csv",
    },
    '300_1_Topic_3_50': {
        "power_path": "data/Normal/300_1_Topic_3_50/Power_Consumption_Cmdline.csv",
    },
    '300_1_Topic_3_100': {
        "power_path": "data/Normal/300_1_Topic_3_100/Power_Consumption_Cmdline.csv",
    },
    '300_1_Topic_3_500': {
        "power_path": "data/Normal/300_1_Topic_3_500/Power_Consumption_Cmdline.csv",
    },
    '300_1_Topic_3_1000': {
        "power_path": "data/Normal/300_1_Topic_3_1000/Power_Consumption_Cmdline.csv",
    },
    '300_1_Topic_100_100': {
        "power_path": "data/Normal/300_1_Topic_100_100/Power_Consumption_Cmdline.csv",
    },
    '300_1_Topic_500_500': {
        "power_path": "data/Normal/300_1_Topic_500_500/Power_Consumption_Cmdline.csv",
    },
    '300_1_Topic_1000_1000': {
        "power_path": "data/Normal/300_1_Topic_1000_1000/Power_Consumption_Cmdline.csv",
    },
}

# Function to convert values to mW
def convert_to_mW(value):
    if 'mW' in value:
        return float(value.replace(' mW', ''))
    elif 'W' in value:
        return float(value.replace(' W', '')) * 1000
    return 0

results = []

for experiment_name, paths in experiments.items():
    power_path = paths["power_path"]
    
    try:
        data = pd.read_csv(power_path)
        
        erlang_column_name = next(
            (col for col in data.columns if col.startswith("/opt/erlang/lib")), None
        )
        
        if erlang_column_name is None:
            raise ValueError("No column found that starts with '/opt/erlang/lib'")
        
        erlang_data = data[erlang_column_name]
        
        # Apply conversion
        erlang_data_mW = erlang_data.apply(convert_to_mW)
        
        # Average power consumption in mW
        avg_erlang_power_mW = erlang_data_mW.mean()
        
        results.append({
            "Experiment": experiment_name,
            "Average Power Consumption (mW)": round(avg_erlang_power_mW, 2)
        })
    
    except Exception as e:
        results.append({
            "Experiment": experiment_name,
            "Error": str(e)
        })

output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

output_file = os.path.join(output_folder, "avg_power_consumption_results.csv")
results_df = pd.DataFrame(results)
results_df.to_csv(output_file, index=False)

print(f"Results have been saved to {output_file}.")