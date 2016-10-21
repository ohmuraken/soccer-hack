import os
import pandas as pd
import numpy as np


def get_data_file(file_name):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, "data", file_name)


def get_soccer_data(league, year):
    file_name = "{}_{}_{}.csv".format(league, year, year+1)
    return pd.read_csv(get_data_file(file_name))


def get_result_data(league, year, team):
    league_year_df = get_soccer_data(league, year)
    team_match_df = league_year_df[(league_year_df["HomeTeam"]==team) | (league_year_df["AwayTeam"]==team)]
    team_home_match_df = team_match_df[team_match_df["HomeTeam"]==team]
    team_away_match_df = team_match_df[team_match_df["AwayTeam"]==team]
    num_of_all_match = team_match_df.shape[0]

    num_of_home_win = 0
    num_of_home_lose = 0
    num_of_home_draw = 0
    for result in team_home_match_df["FTR"]:
        if result == "H":
            num_of_home_win += 1
        elif result == "A":
            num_of_home_lose += 1
        elif result == "D":
            num_of_home_draw += 1


    num_of_away_win = 0
    num_of_away_lose = 0
    num_of_away_draw = 0
    for result in team_away_match_df["FTR"]:
        if result == "A":
            num_of_away_win += 1
        elif result == "H":
            num_of_away_lose += 1
        elif result == "D":
            num_of_away_draw += 1

    home_win_percentage = num_of_home_win / (num_of_all_match)/2
    home_lose_percentage = num_of_home_lose / (num_of_all_match)/2
    home_draw_percentage = num_of_home_draw / (num_of_all_match)/2
    away_win_percentage = num_of_away_win / (num_of_all_match)/2
    away_lose_percentage = num_of_away_lose / (num_of_all_match)/2
    away_draw_percentage = num_of_away_draw / (num_of_all_match)/2

    total_num_of_win = num_of_home_win + num_of_away_win
    total_num_of_lose = num_of_home_lose + num_of_away_lose
    total_num_of_draw = num_of_home_draw + num_of_away_draw
    total_win_percentage = total_num_of_win / num_of_all_match
    total_lose_percentage = total_num_of_lose / num_of_all_match
    total_draw_percentage = total_num_of_draw / num_of_all_match

    report = {
        "num_of_home_win": num_of_home_win,
        "num_of_home_lose": num_of_home_lose,
        "num_of_home_draw": num_of_home_draw,
        "num_of_away_win": num_of_away_win,
        "num_of_away_lose": num_of_away_lose,
        "num_of_away_draw": num_of_away_draw,
        "home_win_percentage": home_win_percentage,
        "home_lose_percentage": home_lose_percentage,
        "home_draw_percentage": home_draw_percentage,
        "away_win_percentage": away_win_percentage,
        "away_lose_percentage": away_lose_percentage,
        "away_draw_percentage": away_draw_percentage,
        "total_num_of_win": total_num_of_win,
        "total_num_of_lose": total_num_of_lose,
        "total_num_of_draw": total_num_of_draw,
        "total_win_percentage": total_win_percentage,
        "total_lose_percentage": total_lose_percentage,
        "total_draw_percentage": total_draw_percentage
    }
    return report


def description():
    return open(get_data_file("notes.txt"), "r").read()
