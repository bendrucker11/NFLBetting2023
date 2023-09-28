import pandas as pd

'''Get data from files using these functions.'''

def load_weekly_player_data():
    return pd.read_csv('nflStatsModule/utilities/data/datafiles/weekly_data_updated_08_23.csv')

def load_yearly_player_data():
    return pd.read_csv('nflStatsModule/utilities/data/datafiles/yearly_data_updated_08_23.csv')

def load_game_data():
    return pd.read_csv('nflStatsModule/utilities/data/datafiles/spreadspoke_scores.csv')

def load_teams_data():
    return pd.read_csv('nflStatsModule/utilities/data/datafiles/nfl_teams.csv')

def load_stadium_data():
    return pd.read_csv('nflStatsModule/utilities/data/datafiles/nfl_stadiums.csv')

def load_coordinate_data():
    return pd.read_csv('nflStatsModule/utilities/data/datafiles/NFL_Stadium_Latitude_and_Longtitude.csv')
