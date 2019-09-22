import sys
import mido
import config
import logging
import sequencer

logging.basicConfig(format="%(message)s", level=logging.INFO, datefmt="%H:%M:%S")
config = config.Config('config.ini')
seq = sequencer.Sequencer(config)


# Console command to play a file
def play():
    seq.start()
    exec(open(sys.argv[1]).read())
    seq.stop()


def noteOn(channel, note, velocity):
    seq.noteOn(channel, note, velocity)


def noteOff(channel, note):
    seq.noteOff(channel, note)


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
