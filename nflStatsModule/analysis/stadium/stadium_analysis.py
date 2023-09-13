from ...utilities.data_loader import *
import pandas as pd
from geopy.distance import geodesic as GD

def join_spread_coords():
    spread_df = load_spread_data()
    coord_df = load_coordinate_data()
    merged = pd.merge(spread_df, coord_df, left_on='team_home', right_on='Team', how='left')
    return merged


def calculate_distance(row):
    coord_df = load_coordinate_data()

    home = (coord_df.loc[coord_df['Team'] == row['team_home'], 'latitude'].values[0],
                       coord_df.loc[coord_df['Team'] == row['team_home'], 'longitude'].values[0])
    away = (coord_df.loc[coord_df['Team'] == row['team_away'], 'latitude'].values[0],
                       coord_df.loc[coord_df['Team'] == row['team_away'], 'longitude'].values[0])
    
    return GD(home, away).miles

def calculate_ou_result(row):
        total_score = int(row['score_home']) + int(row['score_away'])
        over_under_line = float(row['over_under_line'])
        
        if total_score > over_under_line:
            return 'Over'
        elif total_score < over_under_line:
            return 'Under'
        else:
            return 'Push'

def add_ou_distance(df):
    df = clean_over_under(df)
    df['distance'] = None
    df['over_under_result'] = None
    for index, row in df.iterrows():
        df.at[index, 'distance'] = calculate_distance(row)
        df.at[index, 'over_under_result'] = calculate_ou_result(row)
    return df







