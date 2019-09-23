import mido
import config
import time
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


    def start(self):
        logging.info("Sequencer::start")
        try:
            self.outport = mido.open_output(name=self.config.getStringConfig('Output', 'port', defaultPortName), virtual=self.config.getBooleanConfig('Output', 'virtual', True))
            time.sleep(0.5) #Wait some time for port to open
            self.startClock()
        except OSError as e:
            logger.error("Error creating outport: {0}".format(e))
            logger.error("Please configure port name in config.ini, possible port names are:")
            logger.error(mido.get_output_names())
            raise


    def stop(self):
        logging.info("Sequencer::stop")
        self.clock.stop()
        self.outport.reset()
        self.outport.close()


    ####################
    # Timing Functions #
    ####################

    def startClock(self):
        self.clock = clock.Clock(self)
        self.run(self.clock.startInternal)


    def setBpm(self, bpm):
        self.clock.setBpm(bpm)


    def sendClock(self):
        msg = mido.Message('clock')
        self.outport.send(msg)


    def wait(self, length):
        self.sendQueuedMessages()
        self.clock.wait(length)


    def run(self, function, *args):
        self.executor.submit(function, *args)


    #####################
    # Queue Functions #
    #####################

    def queueMessage(self, tick, msg):
        while len(self.messageQueue) < tick+1:
            self.messageQueue.append({})
            self.messageQueue[len(self.messageQueue)-1] = []
        self.messageQueue[int(tick)].append(msg)


    def sendQueuedMessages(self):
        print(self.clock.tick)
        messages = self.messageQueue[self.clock.tick]
        for message in messages:
            self.outport.send(message)


    #####################
    # Control Functions #
    #####################

    def noteOn(self, channel, note, velocity, start=0):
        msg = mido.Message('note_on', channel=channel, note=note, velocity=velocity)
        logging.debug("noteOn {0}".format(msg.bytes()))
        self.queueMessage(self.clock.tick + start, msg)
        self.outport.send(msg)


    def noteOff(self, channel, note, start=0):
        msg = mido.Message('note_off', channel=channel, note=note, velocity=0)
        logging.debug("noteOff {0} {1}".format(start, msg.bytes()))
        self.queueMessage(self.clock.tick + start, msg)
        self.outport.send(msg)
