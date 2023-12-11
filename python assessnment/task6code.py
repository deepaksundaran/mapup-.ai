import pandas as pd

def verify_time_data(df):
    # Combine date and time columns to create datetime columns
    df['start_datetime'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'], errors='coerce')
    df['end_datetime'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'], errors='coerce')
    
    # Check completeness of time data for each (id, id_2) pair
    completeness_check = df.groupby(['id', 'id_2']).apply(check_completeness).reset_index(drop=True)
    
    return completeness_check

def check_completeness(group):
    # Check if all 7 days of the week are covered and the duration spans at least 7 days
    days_covered = group['start_datetime'].dt.dayofweek.nunique() == 7 and group['end_datetime'].dt.dayofweek.nunique() == 7
    duration_span = (group['end_datetime'] - group['start_datetime']).max() >= pd.Timedelta(days=7)
    
    return days_covered and duration_span

# Read the dataset-2.csv file into a DataFrame
data = pd.read_csv(r"C:\Users\DEEPAK\OneDrive\Desktop\dataset\dataset-2.csv")

# Verify the completeness of time data
result = verify_time_data(data)
print(result)


