import sys
import os
import mido
import config
import logging
import threading
import sequencer
from constants import *


path = os.path.abspath(os.path.dirname(__file__))

# Load config
configfile = os.path.join(path, "../config.ini")
config = config.Config(configfile)

# Set root folder as search path for modules
root = os.path.join(path, "..")
sys.path.append(root)

# Setup logging
logging.basicConfig(format="%(message)s", level=logging.DEBUG, datefmt="%H:%M:%S")

# Create sequencer
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

####################
# Channel Rotation #
####################

def setChannel(channelFrom, channelTo=-1):
    currentThread = threading.current_thread()
    dictionary = currentThread.__dict__

    dictionary["channel"] = channelFrom
    dictionary["channelFrom"] = channelFrom
    if channelTo == -1:
        dictionary["channelTo"] = channelFrom
    else:
        dictionary["channelTo"] = channelTo


def getChannel():
    currentThread = threading.current_thread()
    dictionary = currentThread.__dict__

    channel = dictionary["channel"]
    channelTo = dictionary["channelTo"]
    channelFrom = dictionary["channelFrom"]
    if channel < channelTo:
        dictionary["channel"] = channel + 1
    elif channel == channelTo:
        dictionary["channel"] = channelFrom
    return channel


#################
# Note Commands #
#################
def wait(length):
    seq.wait(length)


# Note on.
# Note number can be float to introduce pitch bend.
def noteOn(note, velocity=DEFAULT_VELOCITY, start=0, channel=-1):
    if channel == -1:
        channel = getChannel()
    bend = note - int(note)
    if bend > 0:
        pitchBend(bend, start, channel)
    else:
        pitchBend(0, start, channel)
    seq.noteOn(int(note), velocity, start, channel)


def noteOff(note, start=0, channel=-1):
    if channel == -1:
        channel = getChannel()
    seq.noteOff(int(note), start, channel)


# note on then note off after length of time
def note(note, velocity=DEFAULT_VELOCITY, length=0, start=0, channel=-1):
    if channel == -1:
        channel = getChannel()
    if length == 0:
        length = seq.noteLength
    noteOn(note, velocity, start, channel)
    noteOff(note, start+length, channel)


# pitch bend in cents. floating point in range from -2 to 2
def pitchBend(bend, start=0, channel=-1):
    if channel == -1:
        channel = getChannel()
    seq.pitchBend(bend * 4096, start, channel)


def sysex(data):
    seq.sysex(data)

#TODO

#def pressure():
#   set pressure control

#def control():
#   set other control values
