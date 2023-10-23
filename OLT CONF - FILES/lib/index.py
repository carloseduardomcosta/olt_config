import time
import colorama
import pyfiglet
from olt_g16 import provisionar_g16
from olt_g8 import provisionar_g8
from olt_8820i import provisionar_8820i
from olt_8820g import provisionar_8820g
import pyperclip


colorama.init()
print('\033[0;32;40m')

# Crie um objeto Figlet com a fonte desejada
custom_figlet = pyfiglet.Figlet(font='slant')
# Renderize seu texto em arte ASCII
banner_text = custom_figlet.renderText('OLTs INTELBRAS')
# Exiba o banner
print(banner_text)
print('\033[0;34;40m========================================================================================\n')
print('OLT CONFIG. v.1.1 - Equipe de Suporte Técnico da Intelbras, 2023 | (48) 2106 0030')
print('\n========================================================================================\033[m\n')


if __name__ == "__main__":
    while True:
        # Exibir o menu de escolha
        print("\033[0;32;40mSelecione uma OLT:\n")
        print("1 - OLT G16")
        print("2 - OLT G8")
        print("3 - OLT 8820i")
        print("4 - OLT 8820G\n")
        print("0 - Sair")
        # Obter a escolha do usuário
        escolha_olt = input("\nDigite o número da OLT ou 0 para sair:")
        if escolha_olt == "1":
            provisionar_g16()
        elif escolha_olt == "2":
            provisionar_g8()
        if escolha_olt == "3":
            provisionar_8820i()
        elif escolha_olt == "4":
            provisionar_8820g()
        elif escolha_olt == "0":
            # Sair do programa
            print("\n\033[0;34;40mSaindo do programa...até mais!\033[m")
            time.sleep(3)
            break
        else:
            # Tratar escolhas inválidas
            print('\033[1;31;40mEscolha inválida. Por favor, escolha uma opção válida!\033[m')
