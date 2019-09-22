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


    def wait(self, length):
        waitUntilTime = self.time + length
        while self.running and self.time < waitUntilTime:
            pass



    #########################
    # Internal clock thread #
    #########################

    def startInternal(self):
        self.time = 0
        try:
            while self.running:
                self.internalClockLoop()
        except Exception as e:
            logger.error("Unexpected error: {0}".format(e))


    def internalClockLoop(self):
        time.sleep(self.interval)
        self.time = self.time + 1
        self.seq.sendClock()
