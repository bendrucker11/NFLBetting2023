import pandas as pd

'''Filter pandas dataframes using these functions'''

def filter_since_year(df: pd.DataFrame, year):
    if 'season' in df.columns.values:
      return df[df['season'] >= year]
    elif 'schedule_season' in df.columns.values:
      return df[df['schedule_season'] >= year]
    else:
      return df    


def calculate_ou_result(row):
    '''Helper function for clean_over_under to add in the result'''
    total_score = int(row["score_home"]) + int(row["score_away"])
    over_under_line = float(row["over_under_line"])

    if total_score > over_under_line:
        return "Over"
    elif total_score < over_under_line:
        return "Under"
    else:
        return "Push"

def clean_over_under(df):
    '''Removes games without ou lines and adds the result'''
    df = df.dropna(subset=['over_under_line'])
    df["over_under_result"] = None
    for index, row in df.iterrows():
        result = calculate_ou_result(row)
        df.at[index, "over_under_result"] = result
    df["over_under_line"] = df["over_under_line"].astype(float)
    return df


def clean_temperature(df):
    '''Removes games without temperature'''
    df = df.dropna(subset=['weather_temperature'])
    return df

def min_temp(df, temp):
    return df[df['weather_temperature'] >= temp]


def max_temp(df, temp):
    return df[df['weather_temperature'] <= temp]
