# Open Source Document

By: David Leifer, M.S. Geography, B.A. Environmental Geography.

Disclaimer: I don't have a medical degree.


- In progress: anatomy section notes, background ch12.

- Todo 0: ch 12 summary statistics dataset 2, discussion, conclusion
- Todo 1: Edit chapters 6-7, 10 into .pdf. code is grey background. italicized jupyter methods.
- Todo 2: Edit chapter 13 conclusions.
- Todo 3: Edit chapters 0-13 into .md and proofread.


This document is designed as a textbook specifically for students seeking to learn more about quantitative methods. It attempts to blend several disciplines into a linear concept: computer science and statistics, anatomy and skateboarding, along with front and backend web development. It is an exercise to learn techniques in how Operating Systems or Databases are built before accidentally building annoying automated misinformation viruses. The code will not get anyone wealthy but will hopefully provide the tools to avoid self-inflicted bodily harm.

Graduate level students that already have a firm understanding of basic programming and mathematics would benefit from learning the material. It might also be interesting for engineering, computer science, or statistic students to see material applied to real world problems.

Chapters 0-10 are in a lesson plan structure.

Chapters 11 and 12 are a peer-referenced writeup on skateboarding and anatomy.

The 'ExerciseStatisticsVersions' folder has working ipynb files with functions that are used throughout the course. The code morphed into an import file 'exercise_module.py' and handles parsing and statistics that are similar to basic commands in the Python libraries Pandas and SciPy. Most of the files used in the course are found in 'data' with the exception of 'A0.csv' and 'A1.tsv' with the idea that the reader can puzzle out the format to record their own information.

### Chapter 0: Introduction to Computers
Uses Python to introduce how computers work. By the end of the class you should be able to execute code using existing Python libraries like Pandas.

### Chapter 1 : SciPy and Matplotlib
This chapter is written by the reader to learn about website scraping and further knowledge on SciPy for statistics and Matplotlib for data visualization. It is similar to my graduate thesis and the general outline is below:

- Weeks 0-5 would include using a library similar to the former Twitter website's API Tweepy to collect text information.

- Weeks 8-11 would include learning data visualization with Matplotlib.

- Weeks 12-15 would learn basic statistical functions with SciPy.

### Chapter 2: Timeseries Rasters for Geoserver
This course installs Geoserver on Linux to display raster time series data in a local host. The steps are nearly identical to installing the libraries in a cloud provider or web server such as Google Cloud Platform or Amazon Web Services but does not include HTTPS certificate installation.

### Chapter 3: Linux Automation
Describes how to use BASH to install several Python libraries to download rasters and perform calculations.

### Chapter 4: GDAL Installation
Installs GDAL to build the GeoTIFF rasters in XYZ tile format, which will be hosted on a web server and displayed in the next chapters on web development.

### Chapter 5: GIS Web Development
Uses the JavaScript package manager NPM to install OpenLayers to display the XYZ tiles.

### Chapter 6: Quantiles
Example program that uses Python's Numpy to generate quantiles to more effectively visualize numerical summaries.

### Chapter 7: AngularJS
Builds a time slider to more effectively view an index and the statistical summaries for raster data.

### Chapter 8: CSV Parser
Develops a basic version of the CSV parser as seen in the Pandas library to learn more about the computer science concepts Time and Space complexity.

### Chapter 9: Descriptive Statistics
Efficiently implement basic descriptive statistics to further an understanding of how computers work.

### Chapter 10: Python Graph
Create a black and white python graph using no libraries.

### Chapter 11: Skateboarding and Anatomy I
Discusses learning basic skateboarding tricks and the anatomy and physiological functions necessary to avoid severe bodily injury. Written at an undergraduate level for Kinesiology.

### Chapter 12: Skateboarding and Anatomy II
An in-depth analysis with more data and a summary of anatomy information learned while skateboarding from June-December, 2024. Written at a graduate level for Kinesiology.

### Chapter 13: Conclusions
Concludes the textbook with a summary of what was covered.
