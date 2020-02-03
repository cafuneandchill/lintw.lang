import PySimpleGUI as sg

import lintw_lang


def eng_to_lintw(english_word):
    output = lintw_lang.converttext(str(english_word))
    lintwese = ""
    latin = ""

    for word in output:
        lintwese += word['lintwese']
        latin += word['latin']

    window['lintwese'].update(lintwese)
    window['latin'].update(latin)

    return None


sg.theme('LightPurple')

layout = [[sg.Text("Type in the English words")],
          [sg.Multiline(key='english', size=(45, 5), font='Helvetica 12',
                        autoscroll=True, focus=True, enable_events=True)],
          [sg.Text("Lintwese:"), ],
          [sg.Multiline(key='lintwese', size=(45, 5), font='LintwBasic 14',
                        disabled=True)],
          [sg.Text("Pronunciation:"), ],
          [sg.Multiline(key='latin', size=(45, 5), font='Helvetica 12 italic',
                        disabled=True)],
          [sg.Button('Exit')]]

window = sg.Window('English to Lintwese Converter', layout, resizable=True, finalize=True)
# window.Size = (600, 400)
window.Element('english').expand(expand_x=True, expand_y=True)
window.Element('lintwese').expand(expand_x=True, expand_y=True)
window.Element('latin').expand(expand_x=True, expand_y=True)

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    eng_to_lintw(values['english'])
window.close()
del window
