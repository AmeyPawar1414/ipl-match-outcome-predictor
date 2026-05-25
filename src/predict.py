import pickle
import numpy as np
import pandas as pd
# Load the trained model
with open('../models/random_forest.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_winner(team1, team2,
                   head_to_head_win_rate,
                   team1_won_toss,
                   toss_decision_bat,
                   venue_win_rate,
                   recent_form):
    """
    Predict IPL match winner.

    Parameters:
    -----------
    team1                : str   - Name of team 1
    team2                : str   - Name of team 2
    head_to_head_win_rate: float - Historical win rate of team1 vs team2 (0 to 1)
    team1_won_toss       : int   - 1 if team1 won toss, 0 if team2 won
    toss_decision_bat    : int   - 1 if toss winner chose to bat, 0 if field
    venue_win_rate       : float - team1 win rate at this venue (0 to 1)
    recent_form          : float - team1 win rate in last 5 matches (0 to 1)

    Returns:
    --------
    dict with predicted winner and win probability
    """
    features = pd.DataFrame([[
    head_to_head_win_rate,
    team1_won_toss,
    toss_decision_bat,
    venue_win_rate,
    recent_form
]], columns=[
    'team1_win_rate_vs_team2',
    'team1_won_toss',
    'toss_decision_bat',
    'team1_venue_win_rate',
    'team1_recent_form'
])

    prob = model.predict_proba(features)[0]
    team1_win_prob = round(prob[1] * 100, 1)
    team2_win_prob = round(prob[0] * 100, 1)
    predicted_winner = team1 if prob[1] > 0.5 else team2

    print(f"\n{'='*45}")
    print(f"  {team1} vs {team2}")
    print(f"{'='*45}")
    print(f"  {team1:<30} {team1_win_prob}%")
    print(f"  {team2:<30} {team2_win_prob}%")
    print(f"{'='*45}")
    print(f"  Predicted Winner: {predicted_winner}")
    print(f"{'='*45}\n")

    return {
        'team1': team1,
        'team2': team2,
        'team1_win_prob': team1_win_prob,
        'team2_win_prob': team2_win_prob,
        'predicted_winner': predicted_winner
    }


# --- Try it out ---
if __name__ == '__main__':
    predict_winner(
        team1='Mumbai Indians',
        team2='Chennai Super Kings',
        head_to_head_win_rate=0.55,  # MI wins 55% of h2h matches
        team1_won_toss=1,            # MI won the toss
        toss_decision_bat=0,         # chose to field
        venue_win_rate=0.60,         # MI wins 60% at Wankhede
        recent_form=0.80             # MI won 4 of last 5
    )