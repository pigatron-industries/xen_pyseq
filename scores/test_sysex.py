import protobuf.ConfigMessage_pb2 as configMessage

message = configMessage.ConfigWrapper()
channelMapping = message.channelConfig.channelMapping.add()
channelMapping.midiChannel = 1
channelMapping.cvChannelFrom = 1
channelMapping.cvChannelTo = 1
channelMapping = message.channelConfig.channelMapping.add()
channelMapping.midiChannel = 2
channelMapping.cvChannelFrom = 2
channelMapping.cvChannelTo = 2
logging.info(message.SerializeToString())

sysex(message.SerializeToString())
wait(L4)
