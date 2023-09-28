from ...utilities.stadium.stadium_distance import ou_temp_distance_table
import matplotlib.pyplot as plt

def graph_ou_distance_traveled(year_since, min_temp=None, max_temp=None):   
    dist_df = ou_temp_distance_table(year_since, min_temp, max_temp)
    plt.scatter(dist_df["distance"], dist_df["over_under_line"], c=dist_df["over_under_result"].map({'Under': 'red', 'Over': 'green', 'Push': 'black'}))
    plt.suptitle("Distance Traveled vs OU Line")
    if min_temp and max_temp:
        plt.title(f"Since {year_since}. Temp {min_temp} to {max_temp}.")
    elif min_temp:
        plt.title(f"Since {year_since}. Min Temp {min_temp}.")
    elif max_temp:
        plt.title(f"Since {year_since}. Max Temp {max_temp}.")
    else:
        plt.title(f"Since {year_since}.")
    plt.xlabel("Distance")
    plt.ylabel("OU Line")
    plt.show()

def ou_distance_temp_breakdown(year_since, temp_breaks: list):
    # Currently this will double show games at the exact temp listed. If the list is [20, 30], it will show a game that is exactly 20 on both the 20 and below, and the 20-30.
    # Can fix maybe if all temp are Ints, just add 1 so its up to 20, then 21-30, then 31 and up.
    '''
    Inputting a list of temperatures, it outputs the ou vs distance chart with breaks at each temp in list.
    temp_breaks must be a list with at least one temperature value.
    '''
    graph_ou_distance_traveled(year_since)
    graph_ou_distance_traveled(year_since, max_temp=temp_breaks[0])
    for i in range(len(temp_breaks) - 1):
        # Inefficient way currently. Recalculates distances and whole table each time.
        graph_ou_distance_traveled(year_since, temp_breaks[i], temp_breaks[i+1])
    graph_ou_distance_traveled(year_since, min_temp=temp_breaks[-1])
