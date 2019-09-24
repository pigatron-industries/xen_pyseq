
print("========================")
print(" Starting Test Sequence")
print("========================")

setBpm(120)
setNoteLength(L8)
setChannel(0)

noteOn(60)
noteOn(62)
noteOn(64)
noteOn(65)

wait(L4)

noteOff(60)
noteOff(62)
noteOff(64)
noteOff(65)

wait(L4)

note(60)
note(62)
note(64)
note(65)

wait(L4)

note(62)
note(64)
note(66)
note(68)

wait(L4)


print("======================")
print(" End Of Test Sequence")
print("======================")
