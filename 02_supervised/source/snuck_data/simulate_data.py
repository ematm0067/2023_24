import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load the CSV data into a DataFrame."""
    return pd.read_csv(file_path)

def generate_simulated_data(df):
    simulated_data = {'age': [], 'usage': []}  # 'usage' is 1 for "snuck" and 0 for "sneaked"
    
    for _, row in df.iterrows():
        age_group = row['age']
        snuck_count = row['snuck']
        sneaked_count = row['sneaked']
        total_count = row['simulated_samples']
        
        # Determine age range
        if age_group == 'Over 80':
            age_min, age_max = 80, 85
        else:
            age_min, age_max = map(int, age_group.split('-'))
        
        # Calculate number of "snuck" and "sneaked" samples based on proportions
        if total_count > 0:  # Avoid division by zero
            snuck_samples = int(round((snuck_count / (snuck_count + sneaked_count)) * total_count))
        else:
            snuck_samples = 0
        sneaked_samples = total_count - snuck_samples
        
        # Generate ages and usages
        ages = np.random.randint(age_min, age_max + 1, size=total_count)
        usages = [1] * snuck_samples + [0] * sneaked_samples  # 1 for "snuck", 0 for "sneaked"
        np.random.shuffle(usages)  # Shuffle to mix "snuck" and "sneaked" samples
        
        simulated_data['age'].extend(ages)
        simulated_data['usage'].extend(usages)
    
    return pd.DataFrame(simulated_data)
# Path to the CSV file
file_path = './snuck_sneaked_data.csv'

# Load the data
df = load_data(file_path)
df['total_samples'] = df['snuck'] + df['sneaked']
simulated_size=200
df['fraction_of_total'] = df['total_samples'] / df['total_samples'].sum()
df['simulated_samples'] = np.round(simulated_size * df['fraction_of_total']).astype(int)




# Generate the adjusted simulated data
simulated_df = generate_simulated_data(df)

# Display the simulated data
print(simulated_df)

def jitter_y(y):

    jitter = 0.05  # Define the amount of jitter

    return y + np.random.uniform(-jitter, jitter, size=len(y))


jittered_usage = jitter_y(simulated_df['usage'])



plt.figure(figsize=(10, 6))

# Scatter plot for "snuck" and "sneaked"
# "snuck" samples (usage == 1)
plt.scatter(simulated_df[simulated_df['usage'] == 1]['age'], simulated_df[simulated_df['usage'] == 1]['usage'], label='Snuck', alpha=0.6, marker='o', color='blue')

# "sneaked" samples (usage == 0)

plt.scatter(simulated_df['age'], jittered_usage, c=['blue' if u == 1 else 'red' for u in simulated_df['usage']], alpha=0.6)


plt.xlabel('Age')
plt.ylabel('Usage')
plt.yticks([0, 1], ['Sneaked', 'Snuck'])  # Set the y-ticks to match the usage labels
plt.title('Simulated Usage of "Snuck" vs "Sneaked" by Age')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
