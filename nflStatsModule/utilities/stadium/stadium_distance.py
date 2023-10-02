from ..data import file_loader as fl
from ..data import data_filter as f
from geopy.distance import geodesic as GD


def calculate_distance(row):
    coord_df = fl.load_coordinate_data()

    home = (
        coord_df.loc[coord_df["Team"] == row["team_home"], "latitude"].values[0],
        coord_df.loc[coord_df["Team"] == row["team_home"], "longitude"].values[0],
    )
    away = (
        coord_df.loc[coord_df["Team"] == row["team_away"], "latitude"].values[0],
        coord_df.loc[coord_df["Team"] == row["team_away"], "longitude"].values[0],
    )

    return GD(home, away).miles


def add_distance_col(df):
    df["distance"] = None
    for index, row in df.iterrows():
        df.at[index, "distance"] = calculate_distance(row)
    return df

def games_distance_traveled(year):
    '''Return a table that contains game data with the distance traveled by the away team.'''
    df = fl.load_game_data()
    df = f.filter_since_year(df, year)
    return add_distance_col(df)

def ou_temp_distance_table(year, min_temp=None, max_temp=None):
    df = games_distance_traveled(year)
    df = f.clean_over_under(df)
    df = f.clean_temperature(df)
    if min_temp:
        df = f.min_temp(df, min_temp)
    if max_temp:
        df = f.max_temp(df ,max_temp)
    return df
