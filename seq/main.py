import sys
import mido
import config
import logging
import sequencer
from constants import *

logging.basicConfig(format="%(message)s", level=logging.DEBUG, datefmt="%H:%M:%S")
config = config.Config('config.ini')
seq = sequencer.Sequencer(config)
NOTE_LENGTH = L4


# Console command to play a file
def play():
    seq.start()
    exec(open(sys.argv[1]).read())
    seq.stop()

#################
# Set variables #
#################
def setBpm(bpm):
    seq.setBpm(bpm)

def setNoteLength(length):
    seq.noteLength = length


#################
# Note Commands #
#################
def wait(length):
    seq.wait(length)


def noteOn(channel, note, velocity=DEFAULT_VELOCITY, start=0):
    seq.noteOn(channel, note, velocity, start)


def noteOff(channel, note, start=0):
    seq.noteOff(channel, note, start)


# note on then note off after length of time
def note(channel, note, velocity=DEFAULT_VELOCITY, start=0, length=0):
    if length == 0:
        length = seq.noteLength
    noteOn(channel, note, velocity, start)
    noteOff(channel, note, start+length)


#TODO

# Floating point note values which automatically send pitch bend message with note_on

#def noteOn(channel, note, velocity, length):
#   NoteOn with time length until note off is triggered

#def wait(length)
#   wait some time based on clock

#def pitchBend():
#   send pitch bend message

#def pressure():
#   set pressure control

#def control():
#   set other control values
