# Correcting the data with the latest provided values, including the new entry for "snuck" and "sneaked" at the "14-19" age category



# Updating the data dictionary with the provided counts

updated_data = {

    "age": ["Over 80", "70-79", "60-69", "50-59", "40-49", "30-39", "20-29", "14-19"],

    "snuck": [14, 7, 16, 61, 110, 143, 299, 90],  # Updated counts for "snuck", added 90 for "14-19"

    "sneaked": [58, 25, 26, 49, 41, 24, 26, 6]  # Counts for "sneaked", including 6 for "14-19"

}



# Convert the updated data into a DataFrame

import pandas as pd

df_updated = pd.DataFrame(updated_data)



# Define the file path for the updated CSV

updated_file_path = './snuck_sneaked_data.csv'



# Save the updated data to a CSV file

df_updated.to_csv(updated_file_path, index=False)



updated_file_path
