
print("========================")
print(" Starting Test Sequence")
print("========================")

# TODO Note Names
A_0 = 21
AS0 = 22
B_0 = 23

# Note lengths
L1 = 24*4
L2 = L1/2
L4 = L1/4
L8 = L1/8
L16 = L1/16
L32 = L1/32



channel = 0

setBpm(120)
noteOn(channel, 60, 127)
noteOn(channel, 61, 127)
noteOn(channel, 62, 127)
noteOn(channel, 63, 127)
wait(L4)
noteOff(channel, 60)
noteOff(channel, 61)
noteOff(channel, 62)
noteOff(channel, 63)
wait(L4)
noteOn(channel, 60, 127)
noteOn(channel, 61, 127)
noteOn(channel, 62, 127)
noteOn(channel, 63, 127)
wait(L4)
noteOff(channel, 60)
noteOff(channel, 61)
noteOff(channel, 62)
noteOff(channel, 63)

print("======================")
print(" End Of Test Sequence")
print("======================")
