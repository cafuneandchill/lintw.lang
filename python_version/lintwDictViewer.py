import PySimpleGUI as sg
from .lintwDict import lintw_dictionary as lintw_dict
from .lintw_lang import lintwchars


def findtrans(original, translated):
    index = None
    if not window[original].GetIndexes():
        index = window[original].GetIndexes()[0]
    if index is not None:
        window[translated].Update(disabled=True, scroll_to_index=index, set_to_index=index)
    return None


def printlatin(lintwese):
    ret = ''
    for c in lintwese:
        latin = lintwchars[c].latin
        if latin is not None:
            ret += latin
    window['latin'].update('\\ ' + ret + ' \\')
    return None


listbox_eng = []
listbox_lintwian = []
for word in lintw_dict:
    listbox_eng += [word]
    listbox_lintwian += [lintw_dict[word]]


sg.theme('LightPurple')

col1 = [[sg.Text('English', font='Helvetica 12')],
        [sg.Radio('Eng to Lintw', 'RADIO1', key='etl')],
        [sg.Listbox(listbox_eng, key='eng', size=(20, 14), font='Helvetica 12',
                    enable_events=True)]]

col2 = [[sg.Text('Lintwian', font='Helvetica 12')],
        [sg.Radio('Lintw to Eng', 'RADIO1', key='lte', default=True)],
        [sg.Listbox(listbox_lintwian, key='lintw', size=(20, 14), font='LintwBasic 13')]]

col3 = [[sg.Text('lintwian', key='lintwian', font='LintwBasic 16')],
        [sg.Text('Pronunciation', key='latin', font='Helvetica 11')],
        [sg.Text('Translation', key='translation', font='Helvetica 12')]]

layout = [[sg.Column(col1), sg.Column(col2), sg.Column(col3, key='trans_col')],
          [sg.Button('Exit')]]

window = sg.Window('lintwDictViewer', layout, size=(1000, 400), finalize=True)

window.Element('eng').expand(expand_x=False, expand_y=True)
window.Element('lintw').expand(expand_x=False, expand_y=True)
window.Element('trans_col').expand(expand_x=True, expand_y=True)
window.Element('latin').expand(expand_x=True)


while True:
    event, values = window.read()
    print(event, values)
    print(window['eng'])
    if event in (None, 'Exit'):
        break
    if values['etl'] is True:
        window['eng'].Update(disabled=False)
        window['lintw'].Update(disabled=True)
        findtrans('eng', 'lintw')
    else:
        window['eng'].Update(disabled=True)
        window['lintw'].Update(disabled=False)
        findtrans('lintw', 'eng')
    if values['lintw']:
        printlatin(str(values['lintw'][0]))
    
window.close()
del window
