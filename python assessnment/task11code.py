import pandas as pd
from datetime import datetime, time

def calculate_time_based_toll_rates(df):
    # Create a dictionary to map the day of the week to its proper case string
    day_mapping = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }

    # Convert the date column to datetime format
    df['date'] = pd.to_datetime(df['date'])

    # Function to determine the day of the week in proper case
    def get_proper_day_name(date):
        return day_mapping[date.weekday()]

    # Apply the function to get the proper day names
    df['day_name'] = df['date'].apply(get_proper_day_name)

    # Function to calculate toll rates based on time intervals
    def calculate_toll(row):
        start_time = row['date'].time()
        if row['day_name'] in ['Saturday', 'Sunday']:
            return 0.7  # Constant discount factor for weekends
        elif time(0, 0, 0) <= start_time < time(10, 0, 0) or time(18, 0, 0) <= start_time <= time(23, 59, 59):
            return 0.8  # Discount factor for specified time ranges on weekdays
        else:
            return 1.2  # Discount factor for the remaining time range on weekdays

    # Apply the function to calculate toll rates
    df['toll_rate'] = df.apply(calculate_toll, axis=1)

    # Add start_day, start_time, end_day, and end_time columns
    df['start_day'] = df['day_name']
    df['end_day'] = df['day_name']
    df['start_time'] = df['date'].apply(lambda x: x.time())
    df['end_time'] = df['date'].apply(lambda x: (x + pd.DateOffset(days=1)).time())

    # Drop unnecessary columns
    df.drop(['date', 'day_name'], axis=1, inplace=True)

    return df


