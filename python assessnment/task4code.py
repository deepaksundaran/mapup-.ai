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


