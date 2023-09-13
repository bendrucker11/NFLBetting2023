from nflStatsModule.analysis.stadium.stadium_analysis import *
from nflStatsModule.utilities.data_loader import *




dist_df = load_recent_spread_data(2005)
dist_df = add_ou_distance(dist_df)

print(dist_df[['team_home', 'team_away', 'over_under_line', 'over_under_result', 'distance']])
