import sys
import mido
import config
import logging
import sequencer
from constants import *

logging.basicConfig(format="%(message)s", level=logging.INFO, datefmt="%H:%M:%S")
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


def noteOn(channel, note, velocity=DEFAULT_VELOCITY):
    seq.noteOn(channel, note, velocity)


def noteOff(channel, note):
    seq.noteOff(channel, note)


def waitNoteOff(channel, note, velocity, length):
    wait(length)
    noteOff(channel, note)

# Asynchronus not on then note off after length of time
def note(channel, note, velocity=DEFAULT_VELOCITY, length=0):
    if length == 0:
        length = seq.noteLength
    noteOn(channel, note, velocity)
    seq.run(waitNoteOff, channel, note, velocity, length)


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
