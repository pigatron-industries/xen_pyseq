import mido
import config
import time
import threading
import concurrent.futures
import logging
import clock
from constants import *

defaultPortName = 'virtual'


class Sequencer():

    #######################
    # Lifecycle Functions #
    #######################

    def __init__(self, config):
        self.config = config
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=20)
        self.noteLength = DEFAULT_NOTE_LENGTH
        self.messageQueue = []
        self.channelFrom = 0
        self.channelTo = 0
        self.channel = 0;


    def start(self):
        logging.info("Sequencer::start")
        try:
            self.outport = mido.open_output(name=self.config.getStringConfig('Output', 'port', defaultPortName), virtual=self.config.getBooleanConfig('Output', 'virtual', True))
            time.sleep(0.5) #Wait some time for port to open
            self.startClock()
        except OSError as e:
            print("Error creating outport: {0}".format(e))
            print("Please configure port name in config.ini, possible port names are:")
            print(mido.get_output_names())
            raise


    def stop(self):
        logging.info("Sequencer::stop")
        self.clock.stop()
        self.outport.reset()
        self.outport.close()


    ####################
    # Sequencer thread #
    ####################

    def startClock(self):
        self.clock = clock.Clock(self)
        self.run(self.clock.tickLoop)


    def run(self, function, *args):
        self.executor.submit(function, *args)


    def tick(self):
        self.sendClock()
        self.sendQueuedMessages()


    def queueMessage(self, tick, msg):
        while len(self.messageQueue) < tick+1:
            self.messageQueue.append({})
            self.messageQueue[len(self.messageQueue)-1] = []
        self.messageQueue[int(tick)].append(msg)


    def sendQueuedMessages(self):
        if len(self.messageQueue) >= self.clock.time+1:
            messages = self.messageQueue[self.clock.time]
            if len(messages) > 0:
                logging.debug("Time = {}".format(self.clock.time))
                for message in messages:
                    logging.debug(message)
                    self.outport.send(message)


    ####################
    # Timing Functions #
    ####################

    def setBpm(self, bpm):
        self.clock.setBpm(bpm)


    def sendClock(self):
        msg = mido.Message('clock', time=self.clock.time)
        self.outport.send(msg)


    def wait(self, length):
        waitUntilTime = self.clock.time + length
        while self.clock.running and self.clock.time < waitUntilTime:
            pass


    #####################
    # Control Functions #
    #####################

    def noteOn(self, note, velocity, start=0, channel=0):
        msg = mido.Message('note_on', channel=channel, note=note, velocity=velocity, time=self.clock.time+start)
        self.queueMessage(self.clock.time + start, msg)


    def noteOff(self, note, start=0, channel=0):
        msg = mido.Message('note_off', channel=channel, note=note, velocity=0, time=self.clock.time+start)
        self.queueMessage(self.clock.time + start, msg)


    def pitchBend(self, bend, start=0, channel=0):
        msg = mido.Message('pitchwheel', channel=channel, pitch=int(bend))
        self.queueMessage(self.clock.time + start, msg)
