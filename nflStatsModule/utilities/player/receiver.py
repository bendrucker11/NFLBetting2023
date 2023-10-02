import pandas as pd
from ..data import file_loader as fl
from ..data import data_filter as f


def weekly_players_with_games():
    players_df = fl.load_weekly_player_data()

    teams_df = fl.load_teams_data()
    teams_df = f.simplify_teams_df(teams_df)

    games_df = fl.load_game_data()
    games_df = f.drop_playoff_games(games_df)
    games_df["schedule_week"] = games_df["schedule_week"].astype(int)
    games_df["schedule_season"] = games_df["schedule_season"].astype(int)

    players_df = pd.merge(players_df, teams_df, left_on='team', right_on='team_id')

    merged_df_home = pd.merge(players_df, games_df, left_on=['week', 'season', 'team_name'], right_on=['schedule_week', 'schedule_season', 'team_home'])
    merged_df_away = pd.merge(players_df, games_df, left_on=['week', 'season', 'team_name'], right_on=['schedule_week', 'schedule_season', 'team_away'])

    merged_df = pd.concat([merged_df_home, merged_df_away], axis=0, ignore_index=True)

    return merged_df

def single_player_with_games(name):
  # should make it that it converts to lowercase to make easier? DeVonta != Devonta
  players = weekly_players_with_games()
  player = players[players['name'] == name]
  return player