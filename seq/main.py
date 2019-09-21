import sys
import mido
import config
import sequencer

config = config.Config('config.ini')
seq = sequencer.Sequencer(config)


# Console command to play a file
def play():
    seq.start()
    exec(open(sys.argv[1]).read())
    seq.stop()


def noteOn(channel, note, velocity):
    msg = mido.Message('note_on', channel=channel, note=note, velocity=velocity)
    seq.noteOn(msg)
