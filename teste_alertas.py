import pyautogui

pyautogui.alert(
    text='Automação começará dentro de 5 segundos',
    title='Automação de whatsapp',
    button='ok'
)

resposta = pyautogui.confirm(text='Deseja continuar?', title='confirmação', buttons=['sim','não'])

if resposta == 'sim':
    email = pyautogui.prompt(text='Digite seu e-mail', title='obrigatório')
    senha = pyautogui.password(text='Digite sua senha', title='obrigatório', mask='*')
    print(f'Email: {email} \nSenha: {senha}\nAutomação iniciada')
    pyautogui.click(1185,197, duration=2)
    pyautogui.typewrite(email)
    pyautogui.press('enter')
    pyautogui.write(senha)
else:
    print('Automação cancelada')