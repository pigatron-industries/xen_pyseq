import mido
import config
import time
import threading
import logging

class Sequencer():

    def __init__(self, config):
        self.config = config


    def start(self):
        logging.info("Sequencer::start")
        try:
            self.outport = mido.open_output(name=self.config.getStringConfig('Output', 'port', 'virtual'), virtual=self.config.getBooleanConfig('Output', 'virtual', True))
            time.sleep(0.5) #Wait some time for port to open
        except OSError as err:
            print("Error creating outport: {0}".format(err))
            print("Please configure port name in config.ini, possible port names are:")
            print(mido.get_output_names())
            raise


    def stop(self):
        logging.info("Sequencer::stop")
        self.outport.reset();
        self.outport.close();


    def noteOn(self, channel, note, velocity):
        msg = mido.Message('note_on', channel=channel, note=note, velocity=velocity)
        logging.info("noteOn {0}".format(msg.bytes()))
        self.outport.send(msg)


    def noteOff(self, channel, note):
        msg = mido.Message('note_off', channel=channel, note=note, velocity=0)
        logging.info("noteOff {0}".format(msg.bytes()))
        self.outport.send(msg)
