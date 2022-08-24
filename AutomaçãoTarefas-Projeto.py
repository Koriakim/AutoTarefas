import pyperclip as pyp
import pyautogui as pt
import time


pt.PAUSE = 1


def bem_vindo():
    print("""===================================BEM VINDO A AUTOMAÇÃO PYTHON====================================
===============================================================================================
=================================Desenvolvido por: Tiago Nascimento Moreira====================""")


def menu():  # Acessa o menu principal das funções

    print('')

    pt.alert("Extremamente recomendado configurar os logins antes de executar as tarefas!!!")

    print("""Lista de tarefas:
    1- Configurar Logins;
    2- Login WMS;
    3- Extração de relatorio;
    9- Sair;
    """)

    print('')

    esc = input("""insira a tarefa a ser executada:  """)
    if esc == "1":
        return conf_login()
    elif esc == "2":
        return menu_wms()
    elif esc == "3":
        return extrac()
    elif esc == "9":
        print("Encerrando..."), time.sleep(2), exit()
    elif esc:
        print("Escolha a opção correta"), menu()


def conf_login():  # Menu para configurar o login para acessar o WMS e o Site PWA
    global login_WMS
    global senha_WMS
    global login_SITE
    global senha_SITE

    print("""Configurar Login:
    1- WMS;
    2- Site;
    3- Voltar;
    """)

    esc_login = input("Insira a opção de configuração: ")
    if esc_login == "1":
        login_WMS = input("Insira Login: ")
        senha_WMS = input("Insira a senha: ")
        time.sleep(1.5), print("Login e Senha salvos com sucesso!!!")
    elif esc_login == "2":
        login_SITE = input("Insira Login: ")
        senha_SITE = input("Insira senha: ")
        time.sleep(1.5), print("Login e Senha salvos com sucesso!!!")
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


def menu_wms():

    print('')

    print(""" Escolha o sistema WMS que deseja entrar:
    1- Configurar atalho WMS 
    2- Homologado ( Versão teste );
    3- Produção ( Versão não teste );
    4- Voltar.
    """)

    esc = input("Insira a tarefa a ser executada: ")
    if esc == "1":
        return config_wms()
    elif esc == "2":
        return wms_homologado()
    elif esc == "3":
        return wms_produ()
    elif esc == "4":
        return menu()
    elif esc:
        print("Escolha a opção correta"), menu_wms()


def config_wms():
    global sis_homolog
    global sis_produ

    print('')

    pt.alert("""Importante colocar o atalho do WMS na area de trabalho e renomear para facil identificação. Exemplo:
    Para o sistema homologado: WMS-Homologação.jnlp
    Para o sistema de produção: WMS-Produção.jnlp""")

    print("""Escolha qual sistema deseja configurar o atalho: 
    1- Homologação;
    2- Produção;
    3- Voltar.
    """)

    esc = input("Insira a tarefa a executar: ")
    if esc == "1":
        sis_homolog = input("Insira o nome do atalho do WMS homologado: ")
        time.sleep(1.5), print("Salvo com sucesso!!!")
    elif esc == "2":
        sis_produ = input("Insira o nome do atalho do WMS produção:")
        time.sleep(1.5), print("Salvo com sucesso!!!")
    elif esc == "3":
        return menu_wms()
    elif esc:
        print("Insira a opção correta."), time.sleep(1.5), conf_login()

    config_wms()


def wms_homologado():

    print('')

    site = input("Insira a filial: ")

    print('')

    pt.alert("Ira iniciar a tarefa, não mexa em nada...")

    # Abrir o sistema
    pt.hotkey('winleft')

    pyp.copy(sis_homolog)

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

    menu_wms()


def wms_produ():

    print('')

    site = input("Insira a filial: ")

    print('')

    pt.alert("Ira iniciar a tarefa, não mexa em nada...")

    # Abrir o sistema
    pt.hotkey('winleft')

    pyp.copy(sis_produ)

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

    menu_wms()


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
    pyp.copy(login_SITE)

    pt.hotkey('ctrl', 'v')

    pt.hotkey('tab')

    pyp.copy(senha_SITE)

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

    extrac()


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
    pyp.copy(login_SITE)

    pt.hotkey('ctrl', 'v')

    pt.hotkey('tab')

    pyp.copy(senha_SITE)

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

    extrac()


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
    pyp.copy(login_SITE)

    pt.hotkey('ctrl', 'v')

    pt.hotkey('tab')

    pyp.copy(senha_SITE)

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

    extrac()


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
