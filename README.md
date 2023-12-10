Question 1: Car Matrix Generation
Under the function named generate_car_matrix write a logic that takes the dataset-1.csv as a DataFrame. Return a new DataFrame that follows the following rules:

values from id_2 as columns
values from id_1 as index
dataframe should have values from car column
diagonal values should be 0.

CODE 

import pandas as pd

def generate_car_matrix():
    # Read the dataset into a DataFrame
    df = pd.read_csv(r'C:\Users\DEEPAK\OneDrive\Desktop\python\datasets-1.csv')
    
    # Select the required columns
    filtered_df = df[['id_1', 'id_2', 'car']]
    
    # Create a pivot table to get car values in the desired matrix format
    car_matrix = filtered_df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    
    return car_matrix

# Call the function to get the desired DataFrame
result_matrix = generate_car_matrix()
print(result_matrix)

OUTPUT
id_2    801    802    803    804    805  ...    826    827    829    830    831
id_1                                     ...                                 

801    0.00   2.80   6.00   7.70  11.70  ...  30.87  32.53  36.32  38.27  39.24
802    2.80   0.00   3.40   5.20   9.20  ...  28.27  29.93  33.72  35.67  36.64
803    6.00   3.40   0.00   2.00   6.00  ...  25.07  26.73  30.52  32.47  33.44
804    7.70   5.20   2.00   0.00   4.40  ...  23.47  25.13  28.92  30.87  31.84
805   11.70   9.20   6.00   4.40   0.00  ...  19.37  21.03  24.82  26.77  27.74
806   13.40  10.90   7.70   6.10   2.00  ...  17.77  19.43  23.22  25.17  26.14
807   16.90  14.30  11.10   9.50   5.40  ...  14.17  15.83  19.62  21.57  22.54
808   19.60  17.10  13.90  12.30   8.20  ...  11.47  13.13  16.92  18.87  19.84
809   21.00  18.50  15.30  13.70   9.60  ...  10.27  11.93  15.72  17.67  18.64
821   23.52  20.92  17.72  16.12  12.02  ...   8.01   9.43  13.26  15.17  16.15
822   24.67  22.07  18.87  17.27  13.17  ...   6.55   8.00  11.81  13.74  14.68
823   26.53  23.93  20.73  19.13  15.03  ...   4.74   6.15  10.00  11.89  12.87
824   27.92  25.32  22.12  20.52  16.42  ...   3.50   4.92   8.77  10.66  11.64
825   29.08  26.48  23.28  21.68  17.58  ...   2.20   3.65   7.46   9.35  10.33
826   30.87  28.27  25.07  23.47  19.37  ...   0.00   2.05   5.81   7.71   8.69
827   32.53  29.93  26.73  25.13  21.03  ...   2.05   0.00   4.14   6.06   7.04
829   36.32  33.72  30.52  28.92  24.82  ...   5.81   4.14   0.00   2.38   3.36
830   38.27  35.67  32.47  30.87  26.77  ...   7.71   6.06   2.38   0.00   1.39
831   39.24  36.64  33.44  31.84  27.74  ...   8.69   7.04   3.36   1.39   0.00
![TASK1](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/c34afa2b-72cb-4067-803e-ad6112cc77d6)
![task1answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/ba1757e6-b9de-4709-84fb-9535a6c4755c)

Question 2: Car Type Count Calculation
Create a Python function named get_type_count that takes the dataset-1.csv as a DataFrame. Add a new categorical column car_type based on values of the column car:

low for values less than or equal to 15,
medium for values greater than 15 and less than or equal to 25,
high for values greater than 25.
Calculate the count of occurrences for each car_type category and return the result as a dictionary. Sort the dictionary alphabetically based on keys.

CODE
import pandas as pd

def get_type_count(df):
    # Add a new column 'car_type' based on conditions
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'], right=False)
    
    # Count occurrences for each car_type category
    type_count = df['car_type'].value_counts().to_dict()
    
    # Sort the dictionary alphabetically based on keys
    sorted_type_count = dict(sorted(type_count.items()))
    
    return sorted_type_count

# Read the dataset into a DataFrame
dataset_df = pd.read_csv(r'C:\Users\DEEPAK\OneDrive\Desktop\python\datasets-1.csv')

# Call the function to get the count of occurrences for each car_type category
result = get_type_count(dataset_df)
print(result)

OUTPUT

{'high': 56, 'low': 196, 'medium': 89}


![TASK2](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/a588f630-4c4f-4d55-95f2-406cd5f6d33c)
![task2answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/853b5f88-ea04-40b0-be53-55160f89a86d)

Question 3: Bus Count Index Retrieval
Create a Python function named get_bus_indexes that takes the dataset-1.csv as a DataFrame. The function should identify and return the indices as a list (sorted in ascending order) where the bus values are greater than twice the mean value of the bus column in the DataFrame.

CODE
import pandas as pd

def get_bus_indexes(df):
    # Calculate the mean value of the 'bus' column
    bus_mean = df['bus'].mean()
    
    # Identify indices where 'bus' values are greater than twice the mean
    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()
    
    # Sort the indices in ascending order
    bus_indexes.sort()
    
    return bus_indexes

# Read the dataset into a DataFrame
dataset_df = pd.read_csv(r'C:\Users\DEEPAK\OneDrive\Desktop\python\datasets-1.csv')

# Call the function to get the indices where 'bus' values are greater than twice the mean
result = get_bus_indexes(dataset_df)
print(result)

OUTPUT

[2, 7, 12, 17, 25, 30, 54, 64, 70, 97, 144, 145, 149, 154, 160, 201, 206, 210, 215, 234, 235, 245, 250, 309, 314, 319, 322, 323, 334, 340]

![TASK3](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/19346ddb-8ce4-4a0d-8a9b-a0dc21872870)![task3answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/4d688ce9-9965-4bd5-8048-29ba7a047e95)

Question 4: Route Filtering
Create a python function filter_routes that takes the dataset-1.csv as a DataFrame. The function should return the sorted list of values of column route for which the average of values of truck column is greater than 7.

CODE

import pandas as pd

def filter_routes(df):
    # Calculate average 'truck' values per 'route'
    route_avg_truck = df.groupby('route')['truck'].mean()
    
    # Filter routes where the average 'truck' values are greater than 7
    filtered_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
    
    # Sort the list of routes
    filtered_routes.sort()
    
    return filtered_routes

# Read the dataset into a DataFrame
dataset_df = pd.read_csv(r'C:\Users\DEEPAK\OneDrive\Desktop\python\datasets-1.csv')


# Get the sorted list of routes where average 'truck' values are greater than 7
result = filter_routes(dataset_df)
print(result)

OUTPUT

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

![TASK4](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/2c56e611-8023-4161-98ba-c9c4b6ca6c6f)

![task4answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/b1374d0d-2f0c-40d3-ad11-876e23b93b6b)

Question 5: Matrix Value Modification
Create a Python function named multiply_matrix that takes the resulting DataFrame from Question 1, as input and modifies each value according to the following logic:

If a value in the DataFrame is greater than 20, multiply those values by 0.75,
If a value is 20 or less, multiply those values by 1.25.
The function should return the modified DataFrame which has values rounded to 1 decimal place.

CODE

import pandas as pd

# Generate initial DataFrame
def generate_car_matrix():
    df = pd.read_csv(r"C:\Users\DEEPAK\OneDrive\Desktop\dataset\datasets-1.csv")
    pivot_table = df.pivot(index='id_1', columns='id_2', values='car')
    pivot_table.values[[range(len(pivot_table))]*2] = 0
    return pivot_table

# Modify values in the DataFrame
def multiply_matrix(dataframe):
    modified_df = dataframe.copy()
    modified_df[dataframe > 20] *= 0.75
    modified_df[dataframe <= 20] *= 1.25
    modified_df = modified_df.round(1)
    return modified_df

# Use both functions together
car_matrix = generate_car_matrix()
modified_car_matrix = multiply_matrix(car_matrix)

# Display the modified DataFrame
print(modified_car_matrix)

OUPUT 

id_2  801  802  803  804  805  806  807  808  809  821  822  823  824  825  826  827  829  830  831
id_1
801   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
802   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
803   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
804   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
805   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
806   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
807   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
808   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
809   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
821   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
822   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
823   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
824   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
825   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
826   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
827   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
829   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
830   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
831   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0

![TASK5](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/3378a7d0-0e9b-466b-ba5c-70b756a4a8e0)


![task5answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/f614de67-1144-4d27-976b-a0f624214b6c)


Question 6: Time Check
You are given a dataset, dataset-2.csv, containing columns id, id_2, and timestamp (startDay, startTime, endDay, endTime). The goal is to verify the completeness of the time data by checking whether the timestamps for each unique (id, id_2) pair cover a full 24-hour period (from 12:00:00 AM to 11:59:59 PM) and span all 7 days of the week (from Monday to Sunday).

Create a function that accepts dataset-2.csv as a DataFrame and returns a boolean series that indicates if each (id, id_2) pair has incorrect timestamps. The boolean series must have multi-index (id, id_2).

CODE

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

OUTPUT

0       False
1       False
2       False
3       False
4       False
        ...  
9249    False
9250    False
9251    False
9252    False
9253    False
Length: 9254, dtype: bool




![TASK6](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/47385083-5f14-40f1-9370-9da53157d8d6)


![task6answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/68d7b1ee-eb38-4e8d-bc86-968fbc86689c)

Question 1: Distance Matrix Calculation
Create a function named calculate_distance_matrix that takes the dataset-3.csv as input and generates a DataFrame representing distances between IDs.

The resulting DataFrame should have cumulative distances along known routes, with diagonal values set to 0. If distances between toll locations A to B and B to C are known, then the distance from A to C should be the sum of these distances. Ensure the matrix is symmetric, accounting for bidirectional distances between toll locations (i.e. A to B is equal to B to A).

CODE

import pandas as pd

def calculate_distance_matrix(df):
    # Create an empty DataFrame with unique IDs to store distances
    unique_ids = sorted(set(df['id_start']).union(set(df['id_end'])))
    distance_matrix = pd.DataFrame(0, columns=unique_ids, index=unique_ids)
    
    # Calculate cumulative distances between IDs
    for _, row in df.iterrows():
        start_id, end_id, distance = row['id_start'], row['id_end'], row['distance']
        distance_matrix.at[start_id, end_id] += distance
        distance_matrix.at[end_id, start_id] += distance  # Ensure symmetry
    
    # Set diagonal values to 0
    distance_matrix.values[[range(len(distance_matrix))]*2] = 0
    
    return distance_matrix

# Read the dataset into a DataFrame
dataset_df = pd.read_csv(r"C:\Users\DEEPAK\OneDrive\Desktop\dataset\dataset-3.csv")

# Calculate the distance matrix
result_distance_matrix = calculate_distance_matrix(dataset_df)
print(result_distance_matrix)

OUTPUT

         1001400  1001402  1001404  1001406  1001408  1001410  1001412  1001414  1001416  ...  1001464  1001466  1001468  1001470  1001472  1001488  1004354  1004355  1004356
1001400      0.0      9.7      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001402      9.7      0.0     20.2      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001404      0.0     20.2      0.0     16.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001406      0.0      0.0     16.0      0.0     21.7      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001408      0.0      0.0      0.0     21.7      0.0     11.1      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001410      0.0      0.0      0.0      0.0     11.1      0.0     15.6      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001412      0.0      0.0      0.0      0.0      0.0     15.6      0.0     18.2      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001414      0.0      0.0      0.0      0.0      0.0      0.0     18.2      0.0     13.2  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001416      0.0      0.0      0.0      0.0      0.0      0.0      0.0     13.2      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001418      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0     13.6  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001420      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001422      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001424      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001426      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001428      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001430      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001432      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001434      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001436      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001437      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001438      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001440      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001442      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      4.5        0      0.0        0
1001444      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.7        0
1001446      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001448      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001450      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001452      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001454      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001456      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001458      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001460      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001461      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        0
1001462      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...     26.7      0.0      0.0      0.0        0      0.0        0      0.0        0
1001464      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      8.5      0.0      0.0        0      0.0        0      0.0        0
1001466      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      8.5      0.0     10.7      0.0        0      0.0        0      0.0        0
1001468      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0     10.7      0.0     10.6        0      0.0        0      0.0        0
1001470      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0     10.6      0.0       16      0.0        0      0.0        0
1001472      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0     16.0        0      0.0        0      0.0        0
1001488      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      0.0        4
1004354      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        0      2.0        2
1004355      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      0.0        2      0.0        0
1004356      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0      0.0  ...      0.0      0.0      0.0      0.0        0      4.0        2      0.0        0

[43 rows x 43 columns]

![TASK7](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/2085bf24-8279-47cb-a563-5366c9dc2ab2)


![task7answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/d883cdbc-3d04-41b0-bf95-edfaff8baa58)


Question 2: Unroll Distance Matrix
Create a function unroll_distance_matrix that takes the DataFrame created in Question 1. The resulting DataFrame should have three columns: columns id_start, id_end, and distance.

All the combinations except for same id_start to id_end must be present in the rows with their distance values from the input DataFrame.

CODE 

import pandas as pd

def calculate_distance_matrix(df):
    unique_ids = sorted(set(df['id_start']).union(set(df['id_end'])))
    distance_matrix = pd.DataFrame(0, columns=unique_ids, index=unique_ids)
    
    for _, row in df.iterrows():
        start_id, end_id, distance = row['id_start'], row['id_end'], row['distance']
        distance_matrix.at[start_id, end_id] += distance
        distance_matrix.at[end_id, start_id] += distance
    
    distance_matrix.values[[range(len(distance_matrix))]*2] = 0
    return distance_matrix

def unroll_distance_matrix(distance_matrix):
    ids = distance_matrix.index.tolist()
    unrolled_distances = []
    
    for i in range(len(ids)):
        for j in range(len(ids)):
            id_start = ids[i]
            id_end = ids[j]
            
            if id_start != id_end and distance_matrix.at[id_start, id_end] != 0:
                distance = distance_matrix.at[id_start, id_end]
                unrolled_distances.append([id_start, id_end, distance])
    
    result_df = pd.DataFrame(unrolled_distances, columns=['id_start', 'id_end', 'distance'])
    return result_df

# Read the dataset into a DataFrame
dataset_df = pd.read_csv(r"C:\Users\DEEPAK\OneDrive\Desktop\dataset\dataset-3.csv")

# Calculate the distance matrix
result_distance_matrix = calculate_distance_matrix(dataset_df)
print("Distance Matrix:")
print(result_distance_matrix)
print()

# Unroll the distance matrix
result_unrolled_distances = unroll_distance_matrix(result_distance_matrix)
print("Unrolled Distances:")
print(result_unrolled_distances)

OUTPUT
Unrolled Distances:
    id_start   id_end  distance
0    1001400  1001402       9.7
1    1001402  1001400       9.7
2    1001402  1001404      20.2
3    1001404  1001402      20.2
4    1001404  1001406      16.0
..       ...      ...       ...
83   1004354  1004356       2.0
84   1004355  1001444       0.7
85   1004355  1004354       2.0
86   1004356  1001488       4.0
87   1004356  1004354       2.0

[88 rows x 3 columns]



![TASK8](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/8791c17f-9be8-419a-9d96-95be7c400933)


![TASK88](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/7506fef2-0758-4800-a094-6c608442cc88)




![task8answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/573450ba-769d-4b0f-b2cf-a1202602e469)


Question 3: Finding IDs within Percentage Threshold
Create a function find_ids_within_ten_percentage_threshold that takes the DataFrame created in Question 2 and a reference value from the id_start column as an integer.

Calculate average distance for the reference value given as an input and return a sorted list of values from id_start column which lie within 10% (including ceiling and floor) of the reference value's average.


CODE

import pandas as pd

def calculate_distance_matrix(df):
    unique_ids = sorted(set(df['id_start']).union(set(df['id_end'])))
    distance_matrix = pd.DataFrame(0, columns=unique_ids, index=unique_ids)
    
    for _, row in df.iterrows():
        start_id, end_id, distance = row['id_start'], row['id_end'], row['distance']
        distance_matrix.at[start_id, end_id] += distance
        distance_matrix.at[end_id, start_id] += distance
    
    distance_matrix.values[[range(len(distance_matrix))]*2] = 0
    return distance_matrix

def unroll_distance_matrix(distance_matrix):
    ids = distance_matrix.index.tolist()
    unrolled_distances = []
    
    for i in range(len(ids)):
        for j in range(len(ids)):
            id_start = ids[i]
            id_end = ids[j]
            
            if id_start != id_end and distance_matrix.at[id_start, id_end] != 0:
                distance = distance_matrix.at[id_start, id_end]
                unrolled_distances.append([id_start, id_end, distance])
    
    result_df = pd.DataFrame(unrolled_distances, columns=['id_start', 'id_end', 'distance'])
    return result_df

def find_ids_within_percentage_threshold(df, reference_id):
    # Calculate average distance for the reference value
    reference_avg_distance = df[df['id_start'] == reference_id]['distance'].mean()
    
    # Calculate lower and upper threshold values (10% above and below average distance)
    lower_threshold = reference_avg_distance - (reference_avg_distance * 0.1)
    upper_threshold = reference_avg_distance + (reference_avg_distance * 0.1)
    
    # Filter IDs within the 10% threshold
    filtered_ids = df[(df['distance'] >= lower_threshold) & (df['distance'] <= upper_threshold)]['id_start'].unique()
    sorted_filtered_ids = sorted(filtered_ids)
    
    return sorted_filtered_ids

# Read the dataset into a DataFrame
dataset_df = pd.read_csv(r"C:\Users\DEEPAK\OneDrive\Desktop\dataset\dataset-3.csv")

# Calculate the distance matrix
result_distance_matrix = calculate_distance_matrix(dataset_df)

# Unroll the distance matrix
result_unrolled_distances = unroll_distance_matrix(result_distance_matrix)

# Find IDs within 10% threshold for a reference ID (e.g., reference_id = 100 as an example)
reference_id = 100  # Change this value as needed
ids_within_threshold = find_ids_within_percentage_threshold(result_unrolled_distances, reference_id)
print(f"IDs within 10% threshold of average distance for ID {reference_id}:")
print(ids_within_threshold)

OUTPUT

IDs within 10% threshold of average distance for ID 100:
[]

![TASK9](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/3a91886d-2ca1-44e8-8148-e32216059a2f)


![TASK99](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/93adb789-0f62-495f-a3b7-b3264ae9756d)

![TASK999](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/e6065a66-8be9-4b01-80a2-60a0b91c59f1)

![task9answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/67f37d52-e2f1-49e3-bc27-a770d3519779)

Question 4: Calculate Toll Rate
Create a function calculate_toll_rate that takes the DataFrame created in Question 2 as input and calculates toll rates based on vehicle types.

The resulting DataFrame should add 5 columns to the input DataFrame: moto, car, rv, bus, and truck with their respective rate coefficients. The toll rates should be calculated by multiplying the distance with the given rate coefficients for each vehicle type:

0.8 for moto
1.2 for car
1.5 for rv
2.2 for bus
3.6 for truck

CODE

import pandas as pd

def calculate_distance_matrix(df):
    unique_ids = sorted(set(df['id_start']).union(set(df['id_end'])))
    distance_matrix = pd.DataFrame(0, columns=unique_ids, index=unique_ids)
    
    for _, row in df.iterrows():
        start_id, end_id, distance = row['id_start'], row['id_end'], row['distance']
        distance_matrix.at[start_id, end_id] += distance
        distance_matrix.at[end_id, start_id] += distance
    
    distance_matrix.values[[range(len(distance_matrix))]*2] = 0
    return distance_matrix

def unroll_distance_matrix(distance_matrix):
    ids = distance_matrix.index.tolist()
    unrolled_distances = []
    
    for i in range(len(ids)):
        for j in range(len(ids)):
            id_start = ids[i]
            id_end = ids[j]
            
            if id_start != id_end and distance_matrix.at[id_start, id_end] != 0:
                distance = distance_matrix.at[id_start, id_end]
                unrolled_distances.append([id_start, id_end, distance])
    
    result_df = pd.DataFrame(unrolled_distances, columns=['id_start', 'id_end', 'distance'])
    return result_df

def calculate_toll_rate(df):
    df['moto'] = df['distance'] * 0.8
    df['car'] = df['distance'] * 1.2
    df['rv'] = df['distance'] * 1.5
    df['bus'] = df['distance'] * 2.2
    df['truck'] = df['distance'] * 3.6
    
    return df

# Read the dataset into a DataFrame
dataset_df = pd.read_csv(r"C:\Users\DEEPAK\OneDrive\Desktop\dataset\dataset-3.csv")

# Calculate the distance matrix
result_distance_matrix = calculate_distance_matrix(dataset_df)

# Unroll the distance matrix
result_unrolled_distances = unroll_distance_matrix(result_distance_matrix)

# Calculate toll rates based on vehicle types
result_with_toll_rates = calculate_toll_rate(result_unrolled_distances)
print(result_with_toll_rates)

OUTPUT

    id_start   id_end  distance   moto    car     rv    bus  truck
0    1001400  1001402       9.7   7.76  11.64  14.55  21.34  34.92
1    1001402  1001400       9.7   7.76  11.64  14.55  21.34  34.92
2    1001402  1001404      20.2  16.16  24.24  30.30  44.44  72.72
3    1001404  1001402      20.2  16.16  24.24  30.30  44.44  72.72
4    1001404  1001406      16.0  12.80  19.20  24.00  35.20  57.60
..       ...      ...       ...    ...    ...    ...    ...    ...
83   1004354  1004356       2.0   1.60   2.40   3.00   4.40   7.20
84   1004355  1001444       0.7   0.56   0.84   1.05   1.54   2.52
85   1004355  1004354       2.0   1.60   2.40   3.00   4.40   7.20
86   1004356  1001488       4.0   3.20   4.80   6.00   8.80  14.40
87   1004356  1004354       2.0   1.60   2.40   3.00   4.40   7.20

[88 rows x 8 columns]





![TASK10](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/2febf532-827f-4a4c-827f-383151780c76)




![TASK100](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/7d53f65c-45b9-4ff8-a893-1adb9eee6108)




![task10answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/a8dfdcdf-b17f-4533-83bc-04fc475e1232)

Question 5: Calculate Time-Based Toll Rates
Create a function named calculate_time_based_toll_rates that takes the DataFrame created in Question 3 as input and calculates toll rates for different time intervals within a day.

The resulting DataFrame should have these five columns added to the input: start_day, start_time, end_day, and end_time.

start_day, end_day must be strings with day values (from Monday to Sunday in proper case)
start_time and end_time must be of type datetime.time() with the values from time range given below.
Modify the values of vehicle columns according to the following time ranges:

Weekdays (Monday - Friday):

From 00:00:00 to 10:00:00: Apply a discount factor of 0.8
From 10:00:00 to 18:00:00: Apply a discount factor of 1.2
From 18:00:00 to 23:59:59: Apply a discount factor of 0.8
Weekends (Saturday and Sunday):

Apply a constant discount factor of 0.7 for all times.
For each unique (id_start, id_end) pair, cover a full 24-hour period (from 12:00:00 AM to 11:59:59 PM) and span all 7 days of the week (from Monday to Sunday).

CODE 

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




![TASK11](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/aee67faa-114f-4249-a976-08ca8200eca0)

    
![TASK111](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/e82c2bd1-e0d5-478f-8fe5-4711702c0aab)




