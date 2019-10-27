import protobuf.ConfigMessage_pb2 as configMessage

message = configMessage.ConfigWrapper()
channelMapping = message.channelConfig.channelMapping.add()
channelMapping.midiChannel = 0
channelMapping.cvChannelFrom = 0
channelMapping.cvChannelTo = 1
logging.info(message.SerializeToString())

sysex(message.SerializeToString())
wait(L4)
