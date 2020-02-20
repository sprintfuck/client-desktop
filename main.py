
import sys
import os
import subprocess
import re
from time import sleep, time


def get_active_window_title():
    root = subprocess.Popen(['xprop', '-root', '_NET_ACTIVE_WINDOW'], stdout=subprocess.PIPE)
    stdout, stderr = root.communicate()

    m = re.search(b'^_NET_ACTIVE_WINDOW.* ([\w]+)$', stdout)
    if m != None:
        window_id = m.group(1)
        window = subprocess.Popen(['xprop', '-id', window_id, 'WM_NAME'], stdout=subprocess.PIPE)
        stdout, stderr = window.communicate()
    else:
        return None

    match = re.match(b"WM_NAME\(\w+\) = (?P<name>.+)$", stdout)
    if match != None:
        return match.group("name").strip(b'"')

    return None


if __name__ == "__main__":
    stats = []
    current_stat_name = None
    current_stat_time = time()
    while 1:
        active_window_title = get_active_window_title()
        if current_stat_name is None:
            current_stat_name = active_window_title
        elif current_stat_name != active_window_title:
            stats.append([current_stat_name, time() - current_stat_time])
            current_stat_time = time()
            current_stat_name = active_window_title

        sleep(1)
