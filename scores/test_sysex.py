import protobuf.ConfigMessage_pb2 as configMessage

message = configMessage.ConfigWrapper()
channelMapping = message.channelConfig.channelMapping.add()
channelMapping.midiChannel = 0
channelMapping.cvChannelFrom = 0
channelMapping.cvChannelTo = 1

message.scale.cents.extend([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]);



sysex(message.SerializeToString())
wait(L4)
