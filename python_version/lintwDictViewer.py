import PySimpleGUI as sg

import csv

from lintw_lang import tolatin


def findtrans():
    index = None
    if not window[original].GetIndexes():
        index = window[original].GetIndexes()[0]
    if index is not None:
        window[translated].Update(disabled=True, scroll_to_index=index, set_to_index=index)
    return None


def printlatin(lintwese):
    ret = tolatin(lintwese)
    window['latin'].update('\\ ' + ret + ' \\')
    return None


listbox_lintwian = []
with open('lintwDict.csv', newline='') as csvdict:
    dictionary_reader = csv.DictReader(csvdict, fieldnames=["latin", "lintwese", "lexical_category"])
    for row in dictionary_reader:
        if row["lintwese"] == listbox_lintwian[-1]:
            continue
        listbox_lintwian.append(row["lintwese"])
print(listbox_lintwian)

sg.theme('LightPurple')

col1 = [[sg.Listbox(listbox_lintwian, key='lintw', size=(20, 14), font='LintwBasic 16',
                    enable_events=True)]]

col2 = [[sg.Text('lintwian', key='lintwian', font='LintwBasic 16')],
        [sg.Text('Pronunciation', key='latin', font='Helvetica 11')],
        [sg.Text('Translation', key='translation', font='Helvetica 12')]]

layout = [[sg.Column(col1), sg.Column(col2,  key='trans_col')],
          [sg.Button('Exit')]]

window = sg.Window('lintwDictViewer', layout, size=(1000, 400), finalize=True)

window.Element('lintw').expand(expand_x=False, expand_y=True)
window.Element('trans_col').expand(expand_x=True, expand_y=True)
window.Element('latin').expand(expand_x=True)


while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    findtrans(window['lintw'])

    if values['lintw']:
        printlatin(str(values['lintw'][0]))
    
window.close()
del window
