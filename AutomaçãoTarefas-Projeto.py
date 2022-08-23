import pyperclip as pyp
import pyautogui as pt
import time


pt.PAUSE = 1


def bem_vindo():
    print("""===================================BEM VINDO A AUTOMAÇÃO PYTHON====================================
===============================================================================================
=================================Desenvolvido por: Tiago Nascimento Moreira====================""")


def menu():

    print('')

    print("""Lista de tarefas:
    1- Configurar Logins;
    2- Login "WMS";
    3- Extração de relatorio;
    9- Sair;
    10- Teste Again;
    """)

    print('')

    esc = input("""insira a tarefa a ser executada:  """)
    if esc == "1":
        return conf_login()
    elif esc == "2":
        return login_software()
    elif esc == "3":
        return extrac()
    elif esc == "9":
        print("Encerrando..."), time.sleep(3), exit()
    elif esc == "10":
        return again()
    elif esc:
        print("Escolha a opção correta"), menu()


def conf_login():
    global login_WMS
    global senha_WMS
    global login_site
    global senha_site

    print("""Configurar Login:
    1- WMS;
    2- Site;
    3- Voltar;
    """)

    esc_login = input("Insira a tarefa a ser executada: ")
    if esc_login == "1":
        login_WMS = input("Insira Login: ")
        senha_WMS = input("Insira a senha: ")
        time.sleep(3), print("Login e Senha salvos com sucesso!!!")
    elif esc_login == "2":
        login_site = input("Insira Login: ")
        senha_site = input("Insira senha: ")
        time.sleep(3), print("Login e Senha salvos com sucesso!!!")
    elif esc_login == "3":
        return menu()

    conf_login()


def extrac():

    print('')

    print(""" Escolha o relatorio a ser extraido:
    1- Portaria;
    2- Expedicao;
    3- Recebimento;
    4- Voltar.
    """)

    print('')

    ext = input("Insira a tarefa a ser executada: ")
    if ext == "1":
        return rel_portaria()
    elif ext == "2":
        return rel_expedicao()
    elif ext == "3":
        return rel_recebimento()
    elif ext == "4":
        return menu()
    elif ext:
        print("Escolha a opção correta"), extrac()


def login_software():

    print('')

    pt.alert("Insira o seu login corretamente para executar com exito a tarefa")

    site = input("Insira o site: ")

    print('')

    sis = 'sistema.wms'

    pt.alert("Ira iniciar a tarefa, não mexa em nada...")

    # Abrir o sistema
    pt.hotkey('winleft')

    pyp.copy(sis)

    pt.hotkey('ctrl', 'v')

    pt.hotkey('enter')

    time.sleep(10)

    pt.click(683, 672)

    pt.click(1117, 675)

    time.sleep(5)

    # 'Logar' no sistema com "Login" e "Senha"
    pyp.copy(login_WMS)

    pt.hotkey('ctrl', 'v')

    pt.hotkey('tab')

    pyp.copy(senha_WMS)

    pt.hotkey('ctrl', 'v')

    pt.hotkey('tab')

    pyp.copy(site)

    pt.hotkey('ctrl', 'v')

    pt.hotkey('tab')

    pt.hotkey('enter')

    pt.alert('FIM TAREFA!!!')


def rel_portaria():

    print('')

    pt.alert("Ira iniciar a tarefa, não mexa em nada...")

    link = ''

    # Abrir o navegador
    pt.hotkey('winleft')

    pt.write('chrome')

    pt.hotkey('enter')

    pt.hotkey('ctrl', 't')

    time.sleep(2)

    # Abrir o site
    pyp.copy(link)

    pt.hotkey('ctrl', 'v')

    pt.hotkey('enter')

    time.sleep(10)

    # Entrar no sistema com "Login" e "Senha"
    pyp.copy(login_site)

    pt.hotkey('ctrl', 'v')

    pt.hotkey('tab')

    pyp.copy(senha_site)

    pt.hotkey('ctrl', 'v')

    pt.hotkey('enter')

    time.sleep(10)

    pt.hotkey('enter')

    # Extrair o relatorio "portaria"
    pt.click(111, 295)

    pt.click(100, 336)

    time.sleep(10)

    pt.click(431, 278)

    pt.click(560, 398)

    pt.alert("Tarefa finalizada!")

    again()


def rel_expedicao():
    print('')

    pt.alert("Ira iniciar a tarefa, não mexa em nada...")

    link = ''

    # Abrir o navegador
    pt.hotkey('winleft')

    pt.write('chrome')

    pt.hotkey('enter')

    pt.hotkey('ctrl', 't')

    time.sleep(2)

    # Abrir o site
    pyp.copy(link)

    pt.hotkey('ctrl', 'v')

    pt.hotkey('enter')

    time.sleep(10)

    # Entrar no sistema com "Login" e "Senha"
    pyp.copy(login_site)

    pt.hotkey('ctrl', 'v')

    pt.hotkey('tab')

    pyp.copy(senha_site)

    pt.hotkey('ctrl', 'v')

    pt.hotkey('enter')

    time.sleep(10)

    pt.hotkey('enter')

    # Extrair relatorio expedicao

    pt.click(134, 313)

    pt.click(136, 381)

    pt.click(185, 427)

    time.sleep(10)

    pt.click(433, 277)

    pt.click(562, 400)

    pt.alert('Tarefa finalizada com sucesso!!!')

    again()


def rel_recebimento():
    print('')

    pt.alert("Ira iniciar a tarefa, não mexa em nada...")

    link = ''

    # Abrir o navegador
    pt.hotkey('winleft')

    pt.write('chrome')

    pt.hotkey('enter')

    pt.hotkey('ctrl', 't')

    time.sleep(2)

    # Abrir o site
    pyp.copy(link)

    pt.hotkey('ctrl', 'v')

    pt.hotkey('enter')

    time.sleep(10)

    # Entrar no sistema com "Login" e "Senha"
    pyp.copy(login_site)

    pt.hotkey('ctrl', 'v')

    pt.hotkey('tab')

    pyp.copy(senha_site)

    pt.hotkey('ctrl', 'v')

    pt.hotkey('enter')

    time.sleep(10)

    pt.hotkey('enter')

    # Entrar no relatorio recebimento

    pt.click(130, 319)

    pt.click(135, 340)

    pt.click(211, 409)

    time.sleep(10)

    pt.click(430, 279)

    pt.click(565, 361)

    pt.alert('Tarefa finalizada!!!')

    again()


def again():

    print(' ')

    resp = input("Deseja abrir o menu? (Y/N): ")

    if resp.upper() == "Y":
        return menu()
    elif resp.upper() == "N":
        print("Encerrando... \nObrigado por utilizar o meu software!!!"), time.sleep(
            3), exit()
    else:
        print(f"Digite a opção correta: "), again()


bem_vindo()
menu()
again()
