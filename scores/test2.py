
print("========================")
print(" Starting Test Sequence")
print("========================")

channel = 0

setBpm(120)
setNoteLength(L4)

note(channel, 60)
wait(L4)

note(channel, 60)
pitchBend(channel, 0.5)
wait(L2)


print("======================")
print(" End Of Test Sequence")
print("======================")
