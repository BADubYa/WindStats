# WindStats

#### Copyright: 2017

**Author: Beth Williams** 

**Email: Beth.A.Williams6744@gmail.com**

**Description:**

WindStats is a python 3.4 script operating as an add on or extension to the Sailing Trip Planner application.  WindPlots.py generates scatter plots using matplotlib. The actual wind condition data points are added to the excel file as they are collected real-time, which is then imported into an sqlite3 database for storing and querying.  Plots are based on the Wind categories used in STP application (no wind, light wind, moderate wind, strong wind). Currently the data being used is a sample set, and is not real data.

Each function in WindPlots.py needs to be called from the python interpretive shell. This includes:
1. Creating the Database
2. Populating the Database with Data
3. Calling each plot function (4 in total) to generate each plot.
