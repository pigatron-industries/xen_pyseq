import sys
import configparser
import sequencer

import mido

seq = None
config = None


# Console command to play a file
def play():
    exec(open(sys.argv[1]).read())


def noteOn(channel, note, velocity):
    msg = mido.Message('note_on', channel=channel, note=note, velocity=velocity)
    print(msg.bytes())


def init():
    config = configparser.ConfigParser()
    config.read('config.ini')
    seq = sequencer.Sequencer(config)


init()
