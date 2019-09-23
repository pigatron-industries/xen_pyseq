import time
import logging
import sequencer

defaultBpm = 120
ticksPerBeat = 24


class Clock():


    def __init__(self, sequencer):
        self.time = 0
        self.running = True
        self.seq = sequencer
        self.setBpm(defaultBpm)


    def setBpm(self, bpm):
        logging.info("Clock::setBpm {0}".format(bpm))
        self.bpm = bpm
        self.interval = 60/bpm/ticksPerBeat


    def stop(self):
        self.running = False
