import mido
from util import *

class Sequencer():

    def __init__(self, config):
        print("Sequencer::init")
        self.config = config
        self.outport = mido.open_output(name='foo', virtual=toBoolean(config['Output']['virtual']))

    def noteOn(msg):
        print(msg.bytes())
        outport.send(msg)
