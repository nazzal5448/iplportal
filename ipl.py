import pandas as pd
import numpy as np

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
ipl = pd.read_csv(ipl_matches)

teams=list(ipl["Team1"].unique())

def teamVteam(team1, team2):
    teams_df = ipl[(((ipl["Team1"] == team1) & (ipl["Team2"] == team2)) |
                    ((ipl["Team1"] == team2) & (ipl["Team2"] == team1)))]
    total_matches = teams_df.shape[0]

    if total_matches == 0:
        result = {
            "Total matches played": str(total_matches),
            f"Matches won by {team1}": "NA",
            f"Matches won by {team2}": "NA",
            "Draws": "NA",
            f"{team1} win percentage": "NA",
            f"{team2} win percentage": "NA"
        }
        return result

    team1_wins = teams_df["WinningTeam"].value_counts().get(team1, 0)
    team2_wins = teams_df["WinningTeam"].value_counts().get(team2, 0)

    draws = total_matches - (team1_wins + team2_wins)

    win_prcnt_1 = round(((team1_wins / total_matches) * 100), 2) if total_matches > 0 else "NA"
    win_prcnt_2 = round(((team2_wins / total_matches) * 100), 2) if total_matches > 0 else "NA"

    return {
        "Total matches played": str(total_matches),
        f"Matches won by {team1}": str(team1_wins),
        f"Matches won by {team2}": str(team2_wins),
        "Draws": str(draws),
        f"{team1} win percentage": str(win_prcnt_1),
        f"{team2} win percentage": str(win_prcnt_2)
    }


def teamRecord(team):
    team_df = ipl[(ipl["Team1"] == team) | (ipl["Team2"] == team)]
    overall_matches = team_df.shape[0]

    overall_wins = team_df["WinningTeam"].value_counts().get(team, 0)
    overall_losses = overall_matches - overall_wins
    no_result = overall_matches - (overall_wins + overall_losses)

    overall_win_prcnt = round(((overall_wins / overall_matches) * 100), 2) if overall_matches > 0 else "NA"
    overall_loss_prcnt = round(((overall_losses / overall_matches) * 100), 2) if overall_matches > 0 else "NA"

    toss_wins = team_df["TossWinner"].value_counts().get(team, 0)
    toss_win_prcnt = round(((toss_wins / overall_matches) * 100), 2) if overall_matches > 0 else "NA"

    overall = {
        "Total matches played": str(overall_matches),
        "Tosses Won": str(toss_wins),
        "Tosses win percentage": str(toss_win_prcnt),
        "Matches won": str(overall_wins),
        "Matches lost": str(overall_losses),
        "No result": str(no_result),
        f"Win percentage": str(overall_win_prcnt),
        f"Loss percentage": str(overall_loss_prcnt)
    }

    record_dict = {}
    record_dict["Overall Record"] = overall
    teams = list(ipl["Team1"].unique())

    for team_ in teams:
        if team_ != team:
            resp = teamVteam(team, team_)
            record_dict[f"Record Against {team_}"] = resp

    return record_dict
