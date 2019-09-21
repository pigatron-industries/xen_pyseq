import configparser


class Config():

    def __init__(self, filename):
        self.config = configparser.ConfigParser()
        self.config.read(filename)
        

    def getStringConfig(self, section, name, default):
        value = self.config[section][name];
        if not value:
            return default
        else:
            return value


    def getBooleanConfig(self, section, name, default):
        value = self.config[section][name];
        if not value:
            return default
        else:
            return (False, True)[value=='true']
