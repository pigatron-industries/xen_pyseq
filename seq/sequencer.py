import mido
import config

class Sequencer():

    def __init__(self, config):
        print("Sequencer::init")
        self.config = config
        try:
            self.outport = mido.open_output(name=self.config.getStringConfig('Output', 'port', 'virtual'), virtual=self.config.getBooleanConfig('Output', 'virtual', True))
        except OSError as err:
            print("Error creating outport: {0}".format(err))
            print("Please configure port name in config.ini, possible port names are:")
            print(mido.get_output_names())
            raise


    def noteOn(self, msg):
        print("noteOn")
        print(msg.bytes())
        self.outport.send(msg)
