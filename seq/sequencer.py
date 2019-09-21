import mido
import config
import time

class Sequencer():

    def __init__(self, config):
        self.config = config


    def start(self):
        print("Sequencer::start")
        try:
            self.outport = mido.open_output(name=self.config.getStringConfig('Output', 'port', 'virtual'), virtual=self.config.getBooleanConfig('Output', 'virtual', True))
            time.sleep(0.5) #Wait some time for port to open
        except OSError as err:
            print("Error creating outport: {0}".format(err))
            print("Please configure port name in config.ini, possible port names are:")
            print(mido.get_output_names())
            raise


    def stop(self):
        print("Sequencer::stop")
        self.outport.reset();
        self.outport.close();


    def noteOn(self, msg):
        print("noteOn")
        print(msg.bytes())
        self.outport.send(msg)
