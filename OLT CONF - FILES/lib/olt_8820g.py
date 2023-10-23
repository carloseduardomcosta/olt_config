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

def provisionar_8820g():
    while True:
        print("\n\033[0;34;40mVocê selecionou a OLT Modelo 8820g.\n\033[m\n")
        time.sleep(2)
        
        # Limites para as variáveis
        limite_min_pon_8820g = 1
        limite_max_pon_8820g = 8
        limite_min_posicao_cpe_8820g = 1
        limite_max_posicao_cpe_8820g = 64
        limite_min_vlan_8820g = 1
        limite_max_vlan_8820g = 4094

        pon_selecionada_8820g = input('\033[0;32;40mEm qual porta PON a CPE está aguardando ser provisionada (1-8)?\n')
        
        if pon_selecionada_8820g.isdigit():
            pon_selecionada_8820g = int(pon_selecionada_8820g)
            if limite_min_pon_8820g <= pon_selecionada_8820g <= limite_max_pon_8820g:
                pass
            else:
                print(f'\033[0;31;40mPor favor, insira um valor entre {limite_min_pon_8820g} e {limite_max_pon_8820g}.\033[m')
                continue

        # Solicitar a entrada para "posição_cpe_g16" até que seja válida
        while True:
            posição_cpe_8820g = input(f'\033[0;32;40mEm qual posição da porta PON {pon_selecionada_8820g} a CPE irá ficar (1-64)?\n')
            if posição_cpe_8820g.isdigit():
                posição_cpe_8820g = int(posição_cpe_8820g)
                if limite_min_posicao_cpe_8820g <= posição_cpe_8820g <= limite_max_posicao_cpe_8820g:
                    break
            print(f'\033[0;31;40mPor favor, insira um valor entre {limite_min_posicao_cpe_8820g} e {limite_max_posicao_cpe_8820g}.\033[m')

        gponSN_8820g = input(f'Qual o GPON-SN do produto que deseja provisionar? - Ex.: "12345678" \n')

        while True:
            vlan_8820g = input(f'\033[0;32;40mQual a VLAN ID irá utilizar nesse provisionamento? (1-4094)\n')
            if vlan_8820g.isdigit():
                vlan_8820g = int(vlan_8820g)
                if limite_min_vlan_8820g <= vlan_8820g <= limite_max_vlan_8820g:
                    break
            print(f'\033[0;31;40mPor favor, insira um valor entre {limite_min_vlan_8820g} e {limite_max_vlan_8820g}.\033[m')

        vendorterceiro_8820g = input('Digite o vendorID da sua CPE Ex.: "ITBS" -> se for Intelbras ou Zhone. Terceiros podem ser -> "ZTEG", "HWTC"  etc ...\n')

        if vendorterceiro_8820g.upper() == 'itbs':
            print('Vendor ID da Intelbras, obrigado.\n')
            ITBS = vendorterceiro_8820g.upper()  # Atribui 'ITBS' (maiúsculas) à variável ITBS
        else:
            print('VendorID diferente de ITBS, obrigado.\n')
            vendorterceiro_8820g_itbs_noitbs = vendorterceiro_8820g
            ITBS = vendorterceiro_8820g.upper()

        print("\nO tipo de serviço será ROUTER ou BRIDGE?\n")

        while True:
            print("Escolha uma opção:\n")
            print("1. Router")
            print("2. Bridge\n")
            escolha_g = input("Digite o número correspondente à sua escolha: ")

            if escolha_g == "1":
                print("Você escolheu Router.\n")
                escolha1_g = 'intelbras-142ng'
                escolha2_g = 'router'
                escolha3_g = 'rg'
            elif escolha_g == "2":
                print("Você escolheu Bridge.\n")
                escolha1_g = 'intelbras-110g'
                escolha2_g = 'bridge'
                escolha3_g = 'eth 1'
            else:
                print("Escolha inválida. Por favor, digite 1 para Router ou 2 para Bridge e pressione Enter.")
                continue

            break

        print(f'\033[0;34;40m============================================================================\n')
        comando = f"""
onu set 1/{pon_selecionada_8820g}/{posição_cpe_8820g} meprof {escolha1_g} vendorid ZNTS serno fsan {gponSN_8820g}
create gpon-olt-onu-config 1-1-{pon_selecionada_8820g}-{posição_cpe_8820g}/gpononu
set serial-no-vendor-id = {ITBS}
commit gpon-olt-onu-config 1-1-{pon_selecionada_8820g}-{posição_cpe_8820g}/gpononu

bridge add 1-1-{pon_selecionada_8820g}-{posição_cpe_8820g}/gpononu downlink vlan {vlan_8820g} tagged {escolha3_g}

-----------------
HABILITAR CPE MGR
-----------------

cpe-mgr add local 1-1-{pon_selecionada_8820g}-{500+posição_cpe_8820g}/gponport gtp 1100000000
bridge add 1-1-{pon_selecionada_8820g}-{posição_cpe_8820g}/gpononu gem {500+posição_cpe_8820g} gtp 1100000000 downlink vlan 7 tagged rg
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

            sair_ou_ficar_8820g = input("\033[0;32;40mDigite o número correspondente à sua escolha:\n")

            if sair_ou_ficar_8820g == '1':
                print('\033[0;34;40m\nVoltando para o início do processo...\n')
                time.sleep(2)
                break
            elif sair_ou_ficar_8820g == '2':
                print('\033[0;34;40m\nVoltando ao MENU PRINCIPAL...\n')
                return
            elif sair_ou_ficar_8820g == '3':
                print("\nVocê escolheu sair ... até mais!")
                time.sleep(3)
                sys.exit()
            else:
                print('\033[0;31;40mEscolha inválida. Por favor, escolha uma opção válida!\033[m')

if __name__ == "__main__":
    provisionar_8820g()
