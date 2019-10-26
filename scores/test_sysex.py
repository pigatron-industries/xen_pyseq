import protobuf.ChannelConfig_pb2 as channelConfig

config = channelConfig.ChannelConfig()
channelMapping = config.channelMapping.add()
channelMapping.midiChannel = 1
channelMapping.cvChannelFrom = 1
channelMapping.cvChannelTo = 1
channelMapping = config.channelMapping.add()
channelMapping.midiChannel = 2
channelMapping.cvChannelFrom = 2
channelMapping.cvChannelTo = 2
logging.info(config.SerializeToString())

sysex(config.SerializeToString())
wait(L4)
