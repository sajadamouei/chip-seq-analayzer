import os
import pandas as pd
import matplotlib.pyplot as plt

# The path to the directory that contains your bed files
root_dir = '.'

# Create an empty DataFrame to hold lengths and labels
data = pd.DataFrame(columns=['Length', 'Label'])

# Traverse through directories and subdirectories
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        # Check if the file is a bed file
        if file.endswith('.bed'):
            # Read the bed file into a pandas DataFrame
            df = pd.read_csv(os.path.join(subdir, file), sep='\t', header=None, names=['Chromosome', 'Start', 'End', 'Label'])
            
            # Calculate the length of the annotated part
            df['Length'] = df['End'] - df['Start']
            
            # Select only 'Length' and 'Label' columns
            df = df[['Length', 'Label']]
            
            # Append data to the main DataFrame
            data = pd.concat([data, df])

# Ensure 'Length' column in the final DataFrame is of type int
data['Length'] = data['Length'].astype(int)

# Create a histogram for each label
labels = data['Label'].unique()

for label in labels:
    plt.figure()
    data[data['Label'] == label]['Length'].hist(bins=50)
    plt.title('Length distribution for {}'.format(label))
    plt.xlabel('Length')
    plt.ylabel('Frequency')
    plt.grid(False)
    plt.show()
    
    
# Create a boxplot for each label
labels = data['Label'].unique()

for label in labels:
    plt.figure()
    data[data['Label'] == label].boxplot(column='Length')
    plt.title('Length distribution for {}'.format(label))
    plt.ylabel('Length')
    plt.grid(False)
    plt.show()
