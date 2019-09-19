import sys
import mido

# Console command to play a file
def play():
    exec(open(sys.argv[1]).read())
