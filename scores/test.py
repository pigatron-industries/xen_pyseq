import time

print("========================")
print(" Starting Test Sequence ")
print("========================")

channel = 0

setBpm(120)
setNoteLength(L8)

s = time.time()
noteOn(channel, 60)
noteOn(channel, 62)
noteOn(channel, 64)
noteOn(channel, 65)
logging.info(time.time() - s)

wait(L4)

s = time.time()
noteOff(channel, 62)
noteOff(channel, 64)
noteOff(channel, 66)
noteOff(channel, 68)
logging.info(time.time() - s)

wait(L4)

s = time.time()
note(channel, 60, length=L4)
note(channel, 62, length=L4)
note(channel, 64, length=L4)
note(channel, 65, length=L4)
logging.info(time.time() - s)

wait(L2)



print("======================")
print(" End Of Test Sequence ")
print("======================")
