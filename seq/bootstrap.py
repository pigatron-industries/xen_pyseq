import sys
import configparser
import sequencer

seq = sequencer.Sequencer
config = None

def init():
    config = configparser.ConfigParser()
    config.read('config.ini')
    seq = sequencer.Sequencer(config)

init()
