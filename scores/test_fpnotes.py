import scales.eq12

print("========================")
print(" Starting Test Sequence")
print("========================")

setBpm(120)
setNoteLength(L4)
setChannel(0, 4)

noteOn(60)
wait(L4)

noteOn(60.5)
wait(L4)

noteOn(61)
wait(L4)

noteOn(61.5)
wait(L4)

noteOn(62)
wait(L4)

noteOn(62.5)
wait(L4)

noteOn(63)
wait(L4)

noteOn(63.5)
wait(L4)

wait(L4)


print("======================")
print(" End Of Test Sequence")
print("======================")
