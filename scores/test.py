
print("========================")
print(" Starting Test Sequence")
print("========================")

channel = 0

setBpm(120)
setNoteLength(L16)

note(channel, 60)
note(channel, 61)
note(channel, 62)
note(channel, 63)
wait(L1)


print("======================")
print(" End Of Test Sequence")
print("======================")
