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


# Note on.
# Note number can be float to introduce pitch bend.
def noteOn(channel, note, velocity=DEFAULT_VELOCITY, start=0):
    bend = note - int(note)
    if bend > 0:
        pitchBend(channel, bend, start)
    seq.noteOn(channel, int(note), velocity, start)


def noteOff(channel, note, start=0):
    seq.noteOff(channel, int(note), start)


# note on then note off after length of time
def note(channel, note, velocity=DEFAULT_VELOCITY, start=0, length=0):
    if length == 0:
        length = seq.noteLength
    noteOn(channel, note, velocity, start)
    noteOff(channel, note, start+length)


# pitch bend in cents. floating point in range from -2 to 2
def pitchBend(channel, bend, start=0):
    seq.pitchBend(channel, bend * 4096, start)


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
