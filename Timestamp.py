




from datetime import datetime

class Timestamp:

    def processTimestamp(self, unprocessed_timestamp):

        processed_timestamp = ''

        for char in str(unprocessed_timestamp):
            if char == ' ' or char == '-' or char == '.' or char == ':':
                char = '_'
            processed_timestamp += char

        return processed_timestamp

    def getTimestamp(self):

        return self.processTimestamp(datetime.now())

    def __init__(self):


        pass