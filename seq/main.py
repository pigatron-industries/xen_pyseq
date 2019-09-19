import sys
import mido
import sequencer

seq = sequencer.Sequencer()

# Console command to play a file
def play():
    exec(open(sys.argv[1]).read())

def noteOn(channel, note, velocity):
    msg = mido.Message('note_on', channel=channel, note=note, velocity=velocity)
    print(msg.bytes())
