'''
This file contains utility functions for the digital clock application.
'''
from datetime import datetime
def get_current_time(format_24h=True):
    if format_24h:
        return datetime.now().strftime("%H:%M:%S")
    else:
        return datetime.now().strftime("%I:%M:%S %p")