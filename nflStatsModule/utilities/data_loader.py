import pandas as pd




def load_weekly_data():
    return pd.read_csv('nflStatsModule/utilities/data/weekly_data_updated_08_23.csv')

def load_yearly_data():
    return pd.read_csv('nflStatsModule/utilities/data/yearly_data_updated_08_23.csv')

def load_spread_data():
    return pd.read_csv('nflStatsModule/utilities/data/spreadspoke_scores.csv')

def load_recent_spread_data(year):
    df = load_spread_data()
    return df[df['schedule_season'] >= year]

def clean_over_under(df):
    return df.dropna(subset=['over_under_line'])


def load_teams_data():
    return pd.read_csv('nflStatsModule/utilities/data/nfl_teams.csv')

def load_stadium_data():
    return pd.read_csv('nflStatsModule/utilities/data/nfl_stadiums.csv')

def load_coordinate_data():
    return pd.read_csv('nflStatsModule/utilities/data/NFL_Stadium_Latitude_and_Longtitude.csv')
