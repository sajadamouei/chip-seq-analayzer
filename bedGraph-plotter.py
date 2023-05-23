import os
import pandas as pd

# The path to the directory that contains your bed files
rootDir = '.'

# List to store paths of matching files
matching_files = []

for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        # Check if the file is a .bed file
        if fname.endswith('.bed'):
            # Create the full file path
            full_path = os.path.join(dirName, fname)
            
            # Try opening the file with pandas
            try:
                # Assumes tab-delimited .bed file with NO header line
                df = pd.read_csv(full_path, sep='\t', header=None)

                # Check if there are at least 4 columns
                if df.shape[1] >= 4:
                    # Extract the labels column
                    labels = df.iloc[:, 3].unique()

                    # Check if all necessary labels are present
                    required_labels = ["noPeaks", "peakStart", "peakEnd", "peaks"]
                    if all(label in labels for label in required_labels):
                        matching_files.append(full_path)
            except Exception as e:
                print(f"Error reading file {full_path}: {str(e)}")

# Print matching files
for file in matching_files:
    print(file)


# The path to the directory that contains your .bed file
pd.read_csv('/file.bed', sep='\t')



import numpy as np
# Load data
data = np.loadtxt('/coverage.bedGraph', usecols=(1, 2, 3))

# Show plot of a sequence
fig = plt.figure(figsize=(10, 6))
plt.plot(data[:, 0], data[:, 2], color='blue')
plt.xlabel('Genomic Position')
plt.ylabel('Coverage')
plt.title('Coverage Plot')
plt.show()



# A plot of a specific region of a .bedGraph file and display its labeled parts

# Load data
# The path to the directory that contains your coverage.bedGraph file
data = np.loadtxt('/coverage.bedGraph', usecols=(1, 2, 3))

start_pos = . # Choose the start genomic position point
end_pos = . #Choose the end genomic position point

mask = (data[:, 0] >= start_pos) & (data[:, 0] <= end_pos)
data = data[mask, :]

# Show plot of a limited region of annotated part of a sequence
fig = plt.figure(figsize=(12, 3))
plt.plot(data[:, 0], data[:, 2], color='blue')
plt.xlabel('Genomic Position')
plt.ylabel('Coverage')
plt.title('Coverage Plot')
plt.axvspan(., ., alpha=0.2, color='red') # Choose a start and an end genomic position point
plt.axvspan(., ., alpha=0.2, color='yellow') # Choose a start and an end genomic position point
plt.axvspan(., ., alpha=0.2, color='orange') # Choose a start and an end genomic position point
plt.axvspan(., ., alpha=0.2, color='green') # Choose a start and an end genomic position point
plt.show()

