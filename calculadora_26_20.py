import PySimpleGUI as sg

sg.theme('NeutralBlue')

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def calcular_aceleracao(forca, massa):
    if is_float(forca) and is_float(massa):
        forca = float(forca)
        massa = float(massa)
        
        a = forca / massa
        return a
    return None
    
def calcular_massa(forca, aceleracao):
    if is_float(forca) and is_float(aceleracao):
        forca = float(forca)
        aceleracao = float(aceleracao)
        
        m = forca / aceleracao
        return m
    return None
    
def calcular_forca(massa, aceleracao):
    if is_float(massa) and is_float(aceleracao):
        massa = float(massa)
        aceleracao = float(aceleracao)
        
        f = massa * aceleracao
        return f
    return None

def main():
    layout = [
        [sg.Text('Calculadora Segunda Lei de Newton', text_color='white', size=(30, 1), font=('Helvetica', 20))],
        [sg.Text(" ")],
        [sg.Text('Força (N):', text_color='white', font=('Helvetica', 13)), sg.InputText(key='forca', size=(41, 1))],
        [sg.Text('Massa (kg):', text_color='white', font=('Helvetica', 13)), sg.InputText(key='massa', size=(40, 1))],
        [sg.Text('Aceleração (m/s²):', text_color='white', font=('Helvetica', 13)), sg.InputText(key='aceleracao', size=(33, 1))],
        [sg.Text(" ")],
        [sg.Text("Respostas dos cálculos:", text_color='white', font=('Helvetica', 16), justification='center')],
        [sg.Text(" ")],
        [sg.Text("Massa calculada:", text_color='white', font=('Helvetica', 13)), sg.Text("", key='res_massa', justification='center', text_color='white')],
        [sg.Text("Aceleração calculada:", text_color='white', font=('Helvetica', 13)), sg.Text("", key='res_aceleracao', justification='center', text_color='white')],
        [sg.Text("Força calculada:", text_color='white', font=('Helvetica', 13)), sg.Text("", key='res_forca', justification='center', text_color='white')],
        [sg.Text(" ")],#
        [sg.Button('Calcular', button_color=('white', '#7a8896'),), sg.Button('Limpar', button_color=('white', '#7a8896')), sg.Column([[sg.Button('Sair', button_color=('white', '#7a8896'), pad=(20, 0))]], element_justification='right')],
    ]

    window = sg.Window('Segunda Lei de Newton', layout)

    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Sair':
            break
        
        if event == 'Calcular':
            massa = values['massa']
            aceleracao = values['aceleracao']
            forca = values['forca']
            
            if (is_float(massa) and is_float(aceleracao)) or (is_float(massa) and is_float(forca)) or (is_float(aceleracao) and is_float(forca)):
                m = calcular_massa(forca, aceleracao)
                a = calcular_aceleracao(forca, massa)
                f = calcular_forca(massa, aceleracao)
            
                window['res_massa'].update(value=str(m) if m is not None else '')
                window['res_aceleracao'].update(value=str(a) if a is not None else '')
                window['res_forca'].update(value=str(f) if f is not None else '')
            
            else:
                sg.popup_error("Preencha pelo menos dois campos com números para calcular.", text_color='white', font=('Helvetica', 12), button_color=('white', '#9d312c'))
                window['res_massa'].update(value='')
                window['res_aceleracao'].update(value='')
                window['res_forca'].update(value='')
              
        
        if event == 'Limpar':
            window['massa'].update('')
            window['aceleracao'].update('')
            window['forca'].update('')
            window['res_massa'].update(value='')
            window['res_aceleracao'].update(value='')
            window['res_forca'].update(value='')
            
    window.close()

if __name__ == '__main__':
    main()
