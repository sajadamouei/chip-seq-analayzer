import os
import pandas as pd
import numpy as np

def process_bed_files(directory):
    peakstart_count = 0
    peakstart_total_length = 0
    peakend_count = 0
    peakend_total_length = 0
    peaks_count = 0
    peaks_total_length = 0
    nopeaks_count = 0
    nopeaks_total_length = 0
    total_length = 0
    all_lengths = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.bed'):
                file_path = os.path.join(root, file)
                df = pd.read_csv(file_path, sep='\t', header=None)
                df.columns = ['Chromosome', 'Start', 'End', 'Label']
                df['Length'] = df['End'] - df['Start']

                peakstart_df = df[df['Label'] == 'peakStart']
                peakstart_count += len(peakstart_df)
                peakstart_total_length += peakstart_df['Length'].sum()

                peakend_df = df[df['Label'] == 'peakEnd']
                peakend_count += len(peakend_df)
                peakend_total_length += peakend_df['Length'].sum()

                peaks_df = df[df['Label'] == 'peaks']
                peaks_count += len(peaks_df)
                peaks_total_length += peaks_df['Length'].sum()

                nopeaks_df = df[df['Label'] == 'noPeaks']
                nopeaks_count += len(nopeaks_df)
                nopeaks_total_length += nopeaks_df['Length'].sum()

                total_length += df['Length'].sum()
                all_lengths.extend(df['Length'].tolist())

    average_length = sum(all_lengths) / len(all_lengths) if all_lengths else 0
    longest_length = max(all_lengths) if all_lengths else 0
    smallest_length = min(all_lengths) if all_lengths else 0
    std_dev = np.std(all_lengths) if all_lengths else 0

    print(f"Number of annotated parts with 'Peakstart' label: {peakstart_count}")
    print(f"Total length of annotated parts with 'Peakstart' label: {peakstart_total_length}")
    print(f"Number of annotated parts with 'Peakend' label: {peakend_count}")
    print(f"Total length of annotated parts with 'Peakend' label: {peakend_total_length}")
    print(f"Number of annotated parts with 'peaks' label: {peaks_count}")
    print(f"Total length of annotated parts with 'peaks' label: {peaks_total_length}")
    print(f"Number of annotated parts with 'noPeaks' label: {nopeaks_count}")
    print(f"Total length of annotated parts with 'noPeaks' label: {nopeaks_total_length}")
    print(f"Total length of all annotated parts: {total_length}")
    print(f"Length of the longest annotated part: {longest_length}")
    print(f"Length of the smallest annotated part: {smallest_length}")
    print(f"Average of annotated parts length: {average_length}")
    print(f"Standard deviation of annotated parts length: {std_dev}")

# replace 'path_to_directory' with the path of your directory containing .bed files
process_bed_files('/path_to_directory')
