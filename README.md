Code Use:
Run from the top level, like main.py.

Starts with nflStatsModule/utilities folder.
data/datafiles contains data.
data/file_loader.py contains functions to access that data.
data/data_filter.py contains functions to easily filter through the data

Other folders in data will contain functions that create pandas dataframes we can work with, loading them from file_loader.py and filtering with the data_filter.py functions.

Then nflStatsModule/analysis folder.
Will call from the corresponding folder in data.
For example, files in analysis/stadium folder will get the tables from functions made in utilities/stadium.
The analysis functions will use these tables that now contain all necessary information to do what we need them to.

main.py will simply call the functions in analysis folder
