
import sys
import os
import re
from time import sleep, time
# from stats import Stat
from process import get_active_window_title


if __name__ == "__main__":
    print('Start')
    # stats = []
    # current_stat_name = None
    # current_stat_time = time()
    while 1:
        active_window_title = get_active_window_title()
        # if current_stat_name is None:
            # current_stat_name = active_window_title
        # elif current_stat_name != active_window_title:
            # stats.append([current_stat_name, time() - current_stat_time])
            # current_stat_time = time()
            # current_stat_name = active_window_title
        print(active_window_title)
        sleep(3)
