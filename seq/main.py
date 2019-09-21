#from bootstrap import *
import sys
import mido
import configparser
import sequencer


config = configparser.ConfigParser()
config.read('config.ini')
seq = sequencer.Sequencer(config)



# Console command to play a file
def play():
    exec(open(sys.argv[1]).read())


def noteOn(channel, note, velocity):
    msg = mido.Message('note_on', channel=channel, note=note, velocity=velocity)
    seq.noteOn(msg)
