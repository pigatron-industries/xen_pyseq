
print("========================")
print(" Starting Test Sequence")
print("========================")

setBpm(120)
setNoteLength(L8)
setChannel(0)

noteOn(60)

wait(L4)

noteOff(60)

wait(L8)


print("======================")
print(" End Of Test Sequence")
print("======================")
