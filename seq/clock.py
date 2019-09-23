import time
import logging
import sequencer

defaultBpm = 120
ticksPerBeat = 24


class Clock():


    def __init__(self, sequencer):
        self.tick = 0
        self.running = True
        self.seq = sequencer
        self.setBpm(defaultBpm)


    def setBpm(self, bpm):
        logging.debug("Clock::setBpm {0}".format(bpm))
        self.bpm = bpm
        self.interval = 60/bpm/ticksPerBeat


    def stop(self):
        self.running = False


    def wait(self, length):
        waitUntilTime = self.tick + length
        while self.running and self.tick < waitUntilTime:
            pass



    #########################
    # Internal clock thread #
    #########################

    def startInternal(self):
        self.tick = 0
        try:
            while self.running:
                self.internalClockLoop()
        except Exception as e:
            logging.error("Unexpected error: {0}".format(e))


    def internalClockLoop(self):
        time.sleep(self.interval)
        self.tick = self.tick + 1
        self.seq.sendClock()
