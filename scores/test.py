
print("========================")
print(" Starting Test Sequence")
print("========================")

channel = 0

setBpm(120)
setNoteLength(L8)

noteOn(channel, 60)
noteOn(channel, 62)
noteOn(channel, 64)
noteOn(channel, 65)

wait(L4)

noteOff(channel, 60)
noteOff(channel, 62)
noteOff(channel, 64)
noteOff(channel, 65)

wait(L4)

note(channel, 60)
note(channel, 62)
note(channel, 64)
note(channel, 65)

wait(L4)

note(channel, 62)
note(channel, 64)
note(channel, 66)
note(channel, 68)

wait(L4)


print("======================")
print(" End Of Test Sequence")
print("======================")
