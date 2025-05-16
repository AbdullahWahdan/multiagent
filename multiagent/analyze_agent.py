import time
import numpy as np
import matplotlib.pyplot as plt
from pacman import *
from game import *
from multiAgents import *  # Replace with your actual agent class

def analyze_agent(num_games=10, layout='mediumClassic'):
    clear_times = []
    
    for _ in range(num_games):
        start_time = time.time()
        # Run game with your agent
        options = {
            'pacman': ReflexAgent(),
            'layout': layout,
            'numGames': 1,
            'quietText': True
        }
        games = Game()
        
        if games[0]['state'].isWin():
            clear_times.append(time.time() - start_time)
    
    if not clear_times:
        print("Agent didn't win any games!")
        return
    
    # Statistics
    print("\n=== Performance Report ===")
    print("Games played: %d" % num_games)
    print("Wins: %d (%.1f%%)" % (len(clear_times), 100*len(clear_times)/num_games))
    print("Avg clear time: %.2f sec" % np.mean(clear_times))
    print("Std deviation: %.2f sec" % np.std(clear_times))
    
    # Histogram
    plt.hist(clear_times, bins=10, edgecolor='black')
    plt.title("Pacman Clear Times (Layout: %s)" % layout)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    analyze_agent(num_games=10, layout='mediumClassic')