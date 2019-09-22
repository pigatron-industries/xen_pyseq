
print("========================")
print(" Starting Test Sequence")
print("========================")

channel = 0

setBpm(120)
setNoteLength(L4)

note(channel, 60)
note(channel, 62)
note(channel, 64)
note(channel, 65)
wait(L1)
note(channel, 62)
note(channel, 64)
note(channel, 66)
note(channel, 68)
wait(L1)
note(channel, 60)
note(channel, 62)
note(channel, 64)
note(channel, 65)
wait(L1)
note(channel, 62)
note(channel, 64)
note(channel, 66)
note(channel, 68)
wait(L1)


print("======================")
print(" End Of Test Sequence")
print("======================")
