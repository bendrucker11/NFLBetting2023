import pandas as pd


def load_stadium_data(file_path):
    return file_path

def load_weekly_data():
    return pd.read_csv('nflStatsModule/utilities/data/weekly_data_updated_08_23.csv')

def load_yearly_data():
    return pd.read_csv('nflStatsModule/utilities/data/yearly_data_updated_08_23.csv')

def load_spread_data():
    return pd.read_csv('nflStatsModule/utilities/data/spreadspoke_scores.csv')

def load_teams_data():
    return pd.read_csv('nflStatsModule/utilities/data/nfl_teams.csv')

def load_stadium_data():
    return pd.read_csv('nflStatsModule/utilities/data/nfl_stadiums.csv')
