import protobuf.ConfigMessage_pb2 as configMessage



message = configMessage.ConfigWrapper()

notes = 19
centsPerNote = 1200/notes

for i in range(notes):
    noteCents = (i+1) * centsPerNote
    message.scale.cents.extend([int(noteCents)])

print(message.scale.cents)

sysex(message.SerializeToString())
wait(L4)
