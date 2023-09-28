from ...utilities.stadium.stadium_distance import games_distance_traveled
import matplotlib.pyplot as plt

def graph_ou_distance_traveled():   
    dist_df = games_distance_traveled(2015)
    plt.scatter(dist_df["distance"], dist_df["over_under_line"], c=dist_df["over_under_result"].map({'Under': 'red', 'Over': 'green', 'Push': 'black'}))
    plt.title("Distance Traveled vs OU Line")
    plt.xlabel("Distance")
    plt.ylabel("OU Line")
    plt.show()
