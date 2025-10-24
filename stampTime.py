import time
import datetime
import pandas as pd
from dataclasses import dataclass
from typing import List

@dataclass
class ctfClass:
    name: str
    date: str
    link: str

class stampTime:

    # Initialize with start time (so we can reuse it amongst the function)
    def __init__(self):
        self.saveStart = datetime.datetime.now()

    # Starting time stamp (returns as int)
    def startTimeStamp(self, start):
        # Place timestamp into pandas to convert to timestamp and round by 1 day
        ts = pd.Timestamp(start)
        startTime = ts.round(freq='d')
        # Return in epoch timestamp form 
        return int(startTime.timestamp())
    
    # Ending time stamp, can tune gap in date (returns as int)
    def endTimeStamp(self, start, dayDelta):
        # Get end time from however many days after specified 
        initialize = start + datetime.timedelta(days=dayDelta)
        # Initialize in pandas with timestamp, then round by hours
        ts = pd.Timestamp(initialize)
        endTime = ts.round(freq='h')
        # Return in epoch timestamp form
        return int(endTime.timestamp())