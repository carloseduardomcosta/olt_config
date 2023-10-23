import time
import sys
import pyperclip

def solicitar_entrada_mensagem(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.lower() == 's' or entrada.lower() == 'sim':
            return True
        elif entrada.lower() == 'n' or entrada.lower() == 'não':
            return False
        else:
            print("Resposta inválida. Responda 'S' para Sim ou 'N' para Não.")

def provisionar_8820i():
    while True:
        print("\n\033[0;34;40mVocê selecionou a OLT Modelo 8820i.\n\033[m\n")

        # Limites para as variáveis
        limite_min_pon_8820i = 1
        limite_max_pon_8820i = 8
        limite_min_posicao_cpe_8820i = 1
        limite_max_posicao_cpe_8820i = 128
        limite_min_vlan_8820i = 1
        limite_max_vlan_8820i = 4094

        while True:
            pon_selecionada_8820i = input('\033[0;32;40mEm qual porta PON a CPE está aguardando ser provisionada (1-8)?\n')
            if pon_selecionada_8820i.isdigit():
                pon_selecionada_8820i = int(pon_selecionada_8820i)
                if limite_min_pon_8820i <= pon_selecionada_8820i <= limite_max_pon_8820i:
                    pass
                else:
                    print(f'\033[0;31;40mPor favor, insira um valor entre {limite_min_pon_8820i} e {limite_max_pon_8820i}.\033[m')
                    continue

            # Solicitar a entrada para "posição_cpe_g16" até que seja válida
            while True:
                posição_cpe_8820i = input(f'\033[0;32;40mEm qual posição da porta PON {pon_selecionada_8820i} a CPE irá ficar (1-128)?\n')
                if posição_cpe_8820i.isdigit():
                    posição_cpe_8820i = int(posição_cpe_8820i)
                    if limite_min_posicao_cpe_8820i <= posição_cpe_8820i <= limite_max_posicao_cpe_8820i:
                        break
                print(f'\033[0;31;40mPor favor, insira um valor entre {limite_min_posicao_cpe_8820i} e {limite_max_posicao_cpe_8820i}.\033[m')

            gponSN_8820i = input(f'Qual o GPON-SN do produto que deseja provisionar? - Ex.: "ITBS12345678" \n')

            while True:
                vlan_8820i = input(f'\033[0;32;40mQual a VLAN ID irá utilizar nesse provisionamento? (1-4094)\n')
                if vlan_8820i.isdigit():
                    vlan_8820i = int(vlan_8820i)
                    if limite_min_vlan_8820i <= vlan_8820i <= limite_max_vlan_8820i:
                        break
                print(f'\033[0;31;40mPor favor, insira um valor entre {limite_min_vlan_8820i} e {limite_max_vlan_8820i}.\033[m')

            print("\nO tipo de serviço será ROUTER ou BRIDGE?\n")

            while True:
                print("Escolha uma opção:\n")
                print("1. Router")
                print("2. Bridge\n")
                escolha = input("Digite o número correspondente à sua escolha: ")

                if escolha == "1":
                    print("Você escolheu Router.\n")
                    escolha1 = 'intelbras-142ng'
                    escolha2 = 'router'
                elif escolha == "2":
                    print("Você escolheu Bridge.\n")
                    escolha1 = 'intelbras-110b'
                    escolha2 = 'bridge'
                else:
                    print("Escolha inválida. Por favor, digite 1 para Router ou 2 para Bridge e pressione Enter.")
                    continue

                break

            print(f'\033[0;34;40m============================================================================\n')
            comando = f"""
onu set noauto
onu set gpon {pon_selecionada_8820i} onu {posição_cpe_8820i} serial-number {gponSN_8820i} meprof {escolha1}
bridge add gpon {pon_selecionada_8820i} onu {posição_cpe_8820i} downlink vlan {vlan_8820i} tagged {escolha2}
onu set auto

-----------------
HABILITAR CPE MGR
-----------------

cpe-mgr add local gpon {pon_selecionada_8820i} onu {posição_cpe_8820i}

"""

            print("\033[0;34;40mComando a ser copiado:")
            print(comando)
            print(f'============================================================================\n')

            if solicitar_entrada_mensagem("\033[0;32;40mDeseja copiar o comando? S/N: "):
                pyperclip.copy(comando)
                print("Comando copiado para a área de transferência, basta colar em sua OLT.")
            else:
                print("Comando NÃO copiado.")

            print(f'\n\n======================== FIM DA EXECUÇÃO ATUAL ===============================\n')

            # Loop para perguntar se deseja provisionar outra CPE
            while True:
                print("\n\033[0;32;40mParabéns, Chegamos ao fim do processo! \nVocê deseja provisionar outra ONU/ONT, voltar ao MENU PRINCIPAL ou deseja SAIR?\n ")
                print('\033[0;34;40m1. Provisionar outra ONU/ONT')
                print('\033[0;34;40m2. Menu Principal')
                print('3. Sair do programa\n\033[m')

                sair_ou_ficar_8820i = input("\033[0;32;40mDigite o número correspondente à sua escolha:\n")

                if sair_ou_ficar_8820i == '1':
                    print('\033[0;34;40m\nVoltando para o início do processo...\n')
                    time.sleep(2)
                    break
                elif sair_ou_ficar_8820i == '2':
                    print('\033[0;34;40m\nVoltando ao MENU PRINCIPAL...\n')
                    return
                elif sair_ou_ficar_8820i == '3':
                    print("\nVocê escolheu sair ... até mais!")
                    time.sleep(3)
                    sys.exit()
                else:
                    print('\033[0;31;40mEscolha inválida. Por favor, escolha uma opção válida!\033[m')

if __name__ == "__main__":
    provisionar_8820i()
