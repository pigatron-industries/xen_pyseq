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
        self.clock.wait(length)


    def run(self, function, *args):
        self.executor.submit(function, *args)


    #####################
    # Control Functions #
    #####################

    def noteOn(self, channel, note, velocity):
        msg = mido.Message('note_on', channel=channel, note=note, velocity=velocity)
        logging.info("noteOn {0}".format(msg.bytes()))
        self.outport.send(msg)


    def noteOff(self, channel, note):
        msg = mido.Message('note_off', channel=channel, note=note, velocity=0)
        logging.info("noteOff {0}".format(msg.bytes()))
        self.outport.send(msg)
