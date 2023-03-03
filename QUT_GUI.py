

import pyperclip
import PySimpleGUI as sg
import QUT
import logman

filename = 'QUT_GUI'

while logman.openLog() != True:
    continue

logman.writeLog(logman.LOG_EVENT, filename, 'Log file opened')

qut_obj = QUT.QUT()
logman.writeLog(logman.LOG_EVENT, filename, 'QUT object created')

qut_obj.generateDonateAndGithubURLs()
logman.writeLog(logman.LOG_EVENT, filename, 'Donate and Github QR generated')

layout = [
            [sg.Input(key='--INPUTURL--')],
            [sg.Button(key='--PASTE--', button_text='PASTE'),
             sg.Button(key='--CONVERT--', button_text='CONVERT'),
             sg.Button(key='--CLEAR--', button_text='CLEAR')],
            [sg.Button(key='--SONG--', button_text='SONG'),
             sg.Button(key='--URL--', button_text='URL')],
            [sg.Image('gen_QR/github.png', key='--IMAGEQR--')],
            [sg.Button(key='--DONATE--', button_text='DONATE'),
             sg.Button(key='--GITHUB--', button_text='GITHUB'),
            [sg.Button(key='--DELETEQR--', button_text='DELETE QRs')]]
         ]
logman.writeLog(logman.LOG_EVENT, filename, 'Layout parsed')

window = sg.Window('QUT', layout, keep_on_top=True)
logman.writeLog(logman.LOG_EVENT, filename, 'Window created')

while True:
    event, values = window.read()

    if event in (None, 'Exit'):
        break

    if event == '--CONVERT--':
        qut_obj.setURL(values['--INPUTURL--'])
        qut_obj.saveQRAsPNG(qut_obj.generateQR())
        window['--IMAGEQR--'].update(qut_obj.getPath())
    elif event == '--DONATE--':
        window['--IMAGEQR--'].update('gen_QR/donate.png')
    elif event == '--CLEAR--':
        window['--INPUTURL--'].update('')
        window['--IMAGEQR--'].update('gen_QR/donate.png')
    elif event == '--PASTE--':
        window['--INPUTURL--'].update(pyperclip.paste())
    elif event == '--GITHUB--':
        window['--INPUTURL--'].update('')
        window['--IMAGEQR--'].update('gen_QR/github.png')
    elif event == '--DELETEQR--':
        qut_obj.deleteQRs()
        qut_obj.generateDonateAndGithubURLs()

    # print(event, values)
    logman.writeLog(logman.LOG_INFO, filename, event + ' ' + values['--INPUTURL--'])

window.close()
logman.writeLog(logman.LOG_EVENT, filename, 'Window closed')
logman.writeLog(logman.LOG_EVENT, filename, 'Closing logfile')
logman.closeLog()