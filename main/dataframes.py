import pandas as pd

# read csv's
yearly_data = pd.read_csv('data/yearly_data_updated_08_23.csv')
weekly_data = pd.read_csv('data/weekly_data_updated_08_23.csv')
spread_data = pd.read_csv('data/spreadspoke_scores.csv')
teams_data = pd.read_csv('data/nfl_teams.csv')

# drop rows where spread_favorite or over_under_line are nan
spread_data = spread_data.dropna(subset=['spread_favorite', 'over_under_line'])
# drop rows before year
year = 2005
recent_spread_data = spread_data[spread_data['schedule_season'] >= year]

print(len(recent_spread_data))