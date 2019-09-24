
print("========================")
print(" Starting Test Sequence")
print("========================")

setBpm(120)
setNoteLength(L4)
setChannel(0, 3)

noteOn(60, channel=0)
wait(L4)

noteOn(60.5, channel=1)
wait(L4)

noteOn(61, channel=2)
wait(L4)

noteOn(61.5, channel=3)
wait(L4)

noteOn(62, channel=0)
wait(L4)

noteOn(62.5, channel=1)
wait(L4)

noteOn(63, channel=2)
wait(L4)

noteOn(63.5, channel=3)
wait(L4)

wait(L4)


print("======================")
print(" End Of Test Sequence")
print("======================")
