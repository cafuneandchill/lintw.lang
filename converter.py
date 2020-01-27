import PySimpleGUI as sg

import lintw_lang


def eng_to_lintw(word):
    output = lintw_lang.converttext(str(word))
    lintwese = ""
    latin = ""

    for x in output:
        lintwese += x['lintwese']
        latin += x['latin']

    window['lintwese'].update(lintwese)
    window['latin'].update(latin)

    return None


sg.theme('LightPurple')

layout = [[sg.Text("Type in the English words")],
          [sg.Multiline(key='english', size=(45, 5), font='Helvetica 12', autoscroll=True, focus=True)],
          [sg.Text("Lintwese:"), sg.Button('Copy', key='cp_lintwese')],
          [sg.Multiline(key='lintwese', size=(45, 5), font='LintwBasic 14', disabled=True)],
          [sg.Text("Pronunciation:"), sg.Button('Copy', key='cp_latin')],
          [sg.Multiline(key='latin', size=(45, 5), font='Helvetica 12 italic', disabled=True)],
          [sg.Button('Exit')]]

window = sg.Window('English to Lintwese Converter', layout, resizable=True, finalize=True)
# window.Size = (600, 400)
window.Element('english').expand(expand_x=True, expand_y=True)
window.Element('lintwese').expand(expand_x=True, expand_y=True)
window.Element('latin').expand(expand_x=True, expand_y=True)

while True:
    event, values = window.read(timeout=100, timeout_key="_TIMEOUT_")
    print(event, values)
    if event is None or event == 'Exit':
        break
    eng_to_lintw(values['english'])
window.close()
del window
