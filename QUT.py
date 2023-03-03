


import Timestamp
from qrcode import make
from os import mkdir
from shutil import rmtree
import logman

filename = 'QUT'

class QUT:

    def getURL(self):

        method_name = 'getURL'
        FQFN = filename + ' ' + method_name + ' '
        logman.writeLog(logman.LOG_INFO,  FQFN, self.URL)

        return self.URL

    def setURL(self, url):

        method_name = 'setURL'
        FQFN = filename + ' ' + method_name + ' '
        logman.writeLog(logman.LOG_INFO, FQFN, self.URL)

        self.URL = url

        return

    def generateQR(self):

        if self.URL == 'donate':
            return 'donate'

        return make(self.getURL())

    def getPath(self):

        return 'gen_QR/' + self.timestamp + '.png'

    def saveQRAsPNG(self, qrcode):

        if self.qr_mode == 'github':
            return qrcode.save('gen_QR/github' + '.png')

        if self.qr_mode == 'donate':
            return qrcode.save('gen_QR/donate' + '.png')

        ts_obj = Timestamp.Timestamp()

        self.timestamp = ts_obj.getTimestamp()

        return qrcode.save('gen_QR/' + self.timestamp + '.png')

    def deleteQRs(self):

        rmtree(self.qr_path)
        mkdir(self.qr_path)

        return

    def generateDonateAndGithubURLs(self):

        github_url = 'https://github.com/KrIZILLoX-Krizi'
        self.URL = github_url
        self.qr_mode = 'github'
        self.saveQRAsPNG(self.generateQR())
        donate_url = 'upi://pay?pa=ujggj@ibl&pn=Aashish%20Kumar&mc=0000&mode=02&purpose=00'
        self.URL = donate_url
        self.qr_mode = 'donate'
        self.saveQRAsPNG(self.generateQR())
        self.qr_mode = ''

    def __init__(self):

        self.timestamp = ''
        self.URL = ''
        self.qr_path = 'gen_QR'
        self.qr_mode = ''

        pass
