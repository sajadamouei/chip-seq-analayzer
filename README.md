# CHIP-seq Data Analayzer

This Python project includes scripts for processing, analyzing, and visualizing CHIP-seq data, specifically in .bed and .bedGraph formats. The main functionalities include data extraction, statistical analysis, and data visualization through histograms and boxplots.

## Scripts and Functionality

* **BED File Analyzer**
This script processes .bed files, calculating various metrics related to the 'Start' and 'End' positions of annotations within the files.

* **BEDGraph Plotter**
This script traverses through a specified directory and its subdirectories, searching for .bed files that contain a specific set of labels ("noPeaks", "peakStart", "peakEnd", "peaks"). This script also creates a simple plot of coverage against genomic position from a .bedGraph file. It also includes an example of how to plot a specific region of a .bedGraph file and display its labeled parts.

* **CHIP-seq Data Visualizer**
This script traverses through a specified directory and its subdirectories, searching for .bed files. It then processes these files to compute the length of each annotated part and creates a histogram and a boxplot for each label, showcasing the distribution of lengths.
