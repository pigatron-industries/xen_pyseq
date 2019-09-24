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

def setChannel(channelFrom, channelTo=-1):
    seq.setChannel(channelFrom, channelTo)


#################
# Note Commands #
#################
def wait(length):
    seq.wait(length)


# Note on.
# Note number can be float to introduce pitch bend.
def noteOn(note, velocity=DEFAULT_VELOCITY, start=0, channel=-1):
    bend = note - int(note)
    if bend > 0:
        pitchBend(channel, bend, start)
    seq.noteOn(int(note), velocity, start, channel)


def noteOff(note, start=0, channel=-1, ):
    seq.noteOff(int(note), start, channel)


# note on then note off after length of time
def note(note, velocity=DEFAULT_VELOCITY, length=0, start=0, channel=-1):
    if length == 0:
        length = seq.noteLength
    noteOn(note, velocity, start, channel)
    noteOff(note, start+length, channel)


# pitch bend in cents. floating point in range from -2 to 2
def pitchBend(bend, start=0, channel=-1):
    seq.pitchBend(bend * 4096, start, channel)


#TODO

# fix channel rotation for note off messages

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
