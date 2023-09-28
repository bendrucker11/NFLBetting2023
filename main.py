from nflStatsModule.analysis.stadium import stadium_analysis

# stadium_analysis.ou_distance_temp_breakdown(2016, range(20, 90, 10)) 

# Some thing I found on the above call: 
# 40-50 temp low lines (low dist esp) over hits a lot.
# 60-70 temp seems very under heavy
# 70-80 temp has a lot of games. pretty split
# above 80 temp leans a towards overs

stadium_analysis.ou_distance_temp_breakdown(2016, [40, 45, 67, 73])
# Another example of how break down can be