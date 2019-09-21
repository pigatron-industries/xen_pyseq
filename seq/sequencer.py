import mido
from util import *

class Sequencer():

    def __init__(self, config):
        print("Sequencer::init")
        self.config = config
        try:
            self.outport = mido.open_output(name=config['Output']['port'], virtual=toBoolean(config['Output']['virtual']))
        except OSError as err:
            print("Error creating outport: {0}".format(err))
            print("Please configure port name in config.ini, possible port names are:")
            print(mido.get_output_names())
            raise


    def noteOn(self, msg):
        print("noteOn")
        print(msg.bytes())
        self.outport.send(msg)
