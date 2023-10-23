import sys
import time
import pyperclip

def provisionar_g8():
    while True:
        print("\n\033[0;34;40mVocê selecionou a OLT Modelo G8.\n\033[m\n")
        time.sleep(2)  # Espera por 2 segundos
        print("\033[0;32;40mSelecione uma opção:\n")
        print("1 - PROVISIONAMENTO MANUAL")
#        print("2 - PROVISIONAMENTO AUTOMÁTICO")
        print("2 - VERIFICAR DEVICE-TYPEs DAs CPE INTELBRAS ACEITOS")
        print("3 - COMANDOS GERAIS DE VERIFICAÇÃO DA OLT")
        print("\n0 - VOLTAR AO MENU DE OLT's")

        escolha_opção = input("\nDigite o número da opção ou 0 para voltar ao MENU PRINCIPAL:")
        if escolha_opção == "1":
            print("\n\033[0;34;40mVocê selecionou PROVISIONAMENTO MANUAL\033[m\n")
            time.sleep(1)
         
            limite_min_pon_g8 = 1
            limite_max_pon_g8 = 8
            limite_min_posicao_cpe_g8 = 1
            limite_max_posicao_cpe_g8 = 128
            limite_min_line_cpe_g8 = 0
            limite_max_line_cpe_g8 = 2047

        # Adicione aqui as opções específicas para a OLT Modelo G8.
            while True:
                pon_selecionada_g8 = input('\033[0;32;40mEm qual porta PON a CPE está aguardando ser provisionada (1-8)?\n')
                if pon_selecionada_g8.isdigit():
                    pon_selecionada_g8 = int(pon_selecionada_g8)
                    if limite_min_pon_g8 <= pon_selecionada_g8 <= limite_max_pon_g8:
                        break
                print(f'\033[0;31;40mPor favor, insira um valor entre {limite_min_pon_g8} e {limite_max_pon_g8}.\033[m')

            # Solicitar a entrada para "posição_cpe_g08" até que seja válida
            while True:
                posição_cpe_g8 = input(f'\033[0;32;40mEm qual posição da porta PON {pon_selecionada_g8} a CPE irá ficar (1-128)?\n')
                if posição_cpe_g8.isdigit():
                    posição_cpe_g8 = int(posição_cpe_g8)
                    if limite_min_posicao_cpe_g8 <= posição_cpe_g8 <= limite_max_posicao_cpe_g8:
                        break
                print(f'\033[0;31;40mPor favor, insira um valor entre {limite_min_posicao_cpe_g8} e {limite_max_posicao_cpe_g8}.\033[m')
            gponSN_g8 = input(f'Qual o GPON-SN do produto que deseja provisionar? - Ex.: "ITBS-12345678" \n')
                
            while True:
                line_g8 = input('\033[0;32;40mQual o número da line que irá usar para esse provisionamento? (0 - 2047)\n')
                if line_g8.isdigit():
                    line_g8 = int(line_g8)
                    if limite_min_line_cpe_g8 <= line_g8 <= limite_max_line_cpe_g8:
                        break
                print(f'\033[0;31;40mPor favor, insira um valor entre {limite_min_line_cpe_g8} e {limite_max_line_cpe_g8}.\033[m') 
                
                
            print(f'\033[0;34;40m============================================================================\n')
            
            comando11 = f"""
en
conf t
no ont auto-config
deploy profile rule
aim 0/{pon_selecionada_g8}/{posição_cpe_g8}
permit sn string-hex {gponSN_g8} line {line_g8} default line {line_g8}
active
exit
end
c r s
y

"""
            
            print("\033[0;34;40mComando a ser copiado:")
            print(comando11)
            print(f'============================================================================\n')
            if input("\033[0;32;40mDeseja copiar o comando? S/N").strip().lower() == "s":
                pyperclip.copy(comando11)
                
                print("Comando copiado para area de transferência, basta colar em sua OLT.")
            else:
                print("Comando NÃO copiado.")
            
            print(f'\n\n======================== FIM DA EXECUÇÃO ATUAL ===============================\n')
            
            while True:
                print("\n\033[0;32;40mParabéns, Chegamos ao fim do processo! \nVocê deseja voltar ao MENU PRINCIPAL ou deseja SAIR?\n ")
                print('\033[0;34;40m1.MENU da OLTG8')
                print('\033[0;34;40m2.MENU PRINCIPAL')
                print('3.Sair do programa\n\033[m')

                
                sair_ou_ficar_g8 = input("\033[0;32;40mDigite o número correspondente à sua escolha:\n")
                
                if sair_ou_ficar_g8 == '1':
                    print('Voltando ao MENU da OLTG8...')
                    time.sleep(2)
                    break
                elif sair_ou_ficar_g8 == '2':
                    print('Voltando ao MENU PRINCIPAL...')
                    time.sleep(2)
                    return
                elif sair_ou_ficar_g8 == '3':
                    print("Você escolheu sair ... até mais!")
                    time.sleep(3)
                    sys.exit()  # Encerra o programa
                else:
                    print('\033[0;31;40mEscolha inválida. Por favor, escolha uma opção válida!\033[m')

            
#        elif escolha_opção == "2":
#            print("\n\033[0;34;40mVocê selecionou PROVISIONAMENTO AUTOMÁTICO\033[m\n")
#            time.sleep(1)
            # Resto do código de provisionamento automático
        elif escolha_opção == "2":
            print("\n\033[0;34;40mVocê selecionou DEVICE-TYPE's DA OLT\033[m\n")
            time.sleep(1)
            print("=============================================")
            
            comando10 = f"""
i10-100     2301,1ETH (SFU)
i10-420     1420G,4ETH+2POTS (SFU+HGU)
i30-100     110Gi,1ETH (SFU)
i40-100     R1,1ETH (SFU+HGU)
i40-100-v2  R1v2,1ETH (SFU+HGU)
i40-201     120AC,2ETH+WIFI(SFU+HGU)
i40-211     121W,2ETH(LAN-1-FE+LAN-2-GE)+1POTS+WIFI (SFU+HGU)
i40-400-1   140PoE,4ETH+PoE (SFU+HGU)
i40-401     AX1800,4ETH+WIFI (SFU+HGU)
i40-411     AX1800V,4ETH+1POTS+WIFI (SFU+HGU)
i40-421     142NW,4ETH+2POTS+WIFI (SFU+HGU)
i41-100     110Gb,1ETH (SFU)
i41-201     1200R,2ETH+WIFI(SFU+HGU)
i41-211     121AC,2ETH+1POTS+WIFI (SFU+HGU)
i41-421     142NG,4ETH+2POTS+WIFI (SFU+HGU)
                    
                    """
            print("=============================================")
            print("\033[0;34;40mComando a ser copiado:")
            print(comando10)
            print(f'============================================================================\n')
            if input("\033[0;32;40mDeseja copiar o comando? S/N\n").strip().lower() == "s":
                pyperclip.copy(comando10)
                
                print("Comando copiado para area de transferência, basta colar em sua OLT.")
            else:
                print("Comando NÃO copiado.")
            
            print(f'\n\n======================== FIM DA EXECUÇÃO ATUAL ===============================\n')
            while True:
                print("\n\033[0;32;40mParabéns, chegamos ao fim do processo!\n")
                print("Voltar ao MENU da OLT G8, voltar ao MENU PRINCIPAL ou deseja SAIR?\n")
                print('\033[0;34;40m1. MENU da OLT G8')
                print('2. MENU PRINCIPAL')
                print('3. SAIR do programa\n\033[m')

                sair_ou_ficar_g8 = input("\033[0;32;40mDigite o número correspondente à sua escolha:\n")
                if sair_ou_ficar_g8 == '1':
                    print('\nVoltando ao MENU da OLT G8...\n')
                    time.sleep(2)
                    break
                elif sair_ou_ficar_g8 == '2':
                    print('\nVoltando ao MENU PRINCIPAL...\n')
                    time.sleep(2)
                    return
                elif sair_ou_ficar_g8 == '3':
                    print("\nVocê escolheu sair... até mais!")
                    time.sleep(3)
                    sys.exit()
                else:
                    # Tratar escolhas inválidas
                    print('\033[0;31;40mEscolha inválida. Por favor, escolha uma opção válida!\033[m')
        elif escolha_opção == "3":
            print("\n\033[0;34;40mVocê selecionou COMANDOS GERAIS DA OLT\033[m\n")
            time.sleep(1)
            # Resto do código de comandos gerais de verificação
            comando3 = """
Comandos OLT - G08

-------------------------------------------------XXXXXX--------------------------------------------------XXXXXX--------------------------------------------------XXXXX-------------------------
ATUALIZAÇÃO DE FIRMWARE E BOOTLOADER

Senha de descompactação nova Firmware   ---> Senha para descompactação: 121cc1c58b8d4af2978879d2db2a37cc
http://backend.intelbras.com/sites/default/files/2023-02/V100R001B01D002P003SP2_1.rar

Antes de realizar o procedimento de atualização de firmware, é fortemente recomendado atualizar a versão da sua bootrom em conjunto com o firmware.

Exemplo do procedimento de atualização :

1 - #load whole-bootrom tftp inet 10.10.10.1 V100R001B01D002P003SP2_bootrom_flash_oem_intelbras.bin

2 - #load application tftp inet 192.168.10.2 V100R001B01D002P003SP2_host.arj

3 - reboot

4 - y

Senha para descompactar arquivo de firmware -> 121cc1c58b8d4af2978879d2db2a37cc

-------------------------------------------------XXXXXX--------------------------------------------------XXXXXX--------------------------------------------------XXXXX-------------------------								

====================================
INFOS:
VEIP = modo router
ETH = modo bridge

é importante lembrar que na G8 e G16 fazemos o provisionamento automático por modelo de device. Então só daria se tem apenas 1 VLAN criada


Passos para lembrar:

1: Criar as VLANs
2: Acessar porta desejada e definir o modo da porta, após isso atrelar a vlan na porta
3: Criar interface IN BAND, ou seja, acessar interface interface-vlan X e atribuir um ip e máscara para ela
4: Criar a rota default apontando para o gateway (PTP com minha interface)
5: Criar os profiles / provisionamentos
5: Salvar tudo. copy running ...

=====================================

Gerenciamento da OLT
=====================================

Dados de fábrica para acesso
IP padrão: 192.168.10.1
Usuário: admin
Senha: admin

Modo Privilegiado
	\\enable

Configurações globais
	\\configure terminal

Salvar configuração
	\\copy running-config startup-config (dentro de Enable)


Enviar configuração para servidor externo
	\\upload configuration {tftp | ftp} {inet | inet6 } <server-ip> <file-name>



----------------------------------
IPv6 na OLT
G8(config-if-vlanInterface-400)#ipv6 address 2804:7a3c:ef00::2/126G8(config)
#ipv6 route ::/0 2804:7a3c:ef00::1

----------------------------------
COMUNICAÇÃO ENTRE ONUs (PON Switch)
	
	
Habilitar TLS:

OLTG16(config)#vlan 200 (habilita somente na Vlan)

OLTG16(config-if-vlan)#pon-switch

Config vlan pon-switch successfully.

OLTG16(config-if-vlan)#

OLTG16(config-if-vlan)#exit

OLTG16(config)#interface vlan-interface 200 (precisa configurar a interface)

Create vlan-interface successfully!

é feito na VLAN

e é obrigatorio criar uma interface vlan na vlan que queres comunicação

-----------------------------------------------------------------------------------------------------------

Criando a UPLINK

	\\en
	\\conf t
	\\vlan "111"
	\\exit
	\\interface ethernet "1/1"
	\\switchport mode "hybrid"
	\\switchport hybrid tagged vlan "111"
	\\exit
	\\exit

========================================================

PROFILES

=========================================================

Profile DBA

	\\deploy profile dba
	\\aim X name [name "qualquer"]
	\\type 4 max 1200000
 	\\active

Visualizar 
	\\show running-config deploy-profile-dba
	\\show deploy dba brief all

Deletar
	\\deploy profile dba
	\\delete aim {<index_num> [ name <name> ] | name <name>}

-------------------------------------

Profile VLAN

	\\deploy profile vlan
	\\aim {<index_num> | [ name <name> ] }
	\\translate old-vlan <vid> [ <priority> ] new-vlan <vid> [ <priority> ]
	\\active

Visualizar
	\\show running-config deploy-profile-vlan
	\\show deploy vlan brief all

Deletar
	\\delete aim {<index_num> | [ name <name> ] }


-------------------------------------


Profile LINE

	\\deploy profile line
	\\aim {<index_num> | [ name <name> ] }
	\\device type <type>
	\\tcont <tcont_id> profile dba { <index_num> | name <name> }
	\\gemport <gem_index> tcont <tcont_id>  vlan-profile { <index_num>| name <name>}
	\\mapping mode port-vlan
	\\mapping <index_num> port {veip | eth <port_index> | iphost} vlan <vid> gemport <gem_index>
	\\flow <flow_id> port {veip | eth <port_index> | iphost} {vlan <vid> keep | default vlan <vid>}
	\\active

Visualizar 
	\\show deploy line {index_num | all}
	\\show deploy line brief {<index_num> | all }


Deletar
	\\deploy profile line
	\\delete aim {<index_num> | [ name <name> ] }
	
------------------------------------

Profile Rule

deploy profile rule
aim 0/x/y name 121w-Cliente-Z
permit sn string-hex ITBS-2ca3cf60 line X default line Z
active
exit
exit



====================================================================

Descoberta de CPEs Automática

Sintaxe:
	\\ont-find interface gpon {<interface_list> | show }     

Desfazer:
	\\no ont-find interface gpon {<interface_list> | all }

Visualizar:
	\\show ont-find config interface gpon {<interface_list> | all }

----------------------------------------

	
=============================================

Provisionamento 

=============================================

Ver posições lógicas configuradas na OLT
	\\show deploy rule brief interface gpon all
	
	
CPEs Descobertas
	\\show ont-find list interface gpon all	

	
CPEs aguardando provisionamento
	\\show ont-find list interface gpon all	
	
	
	
	
	

	
	
================================================
Comando de  Verificação ONU/ONT
================================================

Procurar ONU especifica dentro da OLT
	\\show deploy rule brief inused sn string-hex [ITBS-1790032e] 



Comando para verificar os detalhes das ONUs para provisionar
	\\show ont-find list interface gpon 0/x index x 


Verificar configuração de auto-config feita
	\\show running-config gpon-device 



Mostra as ONU´s/ONT´s provisionadas informando modelo, serial numnber, status e posição)
	\\show ont brief interface gpon all 


Verificar sinal da ONU
	\\show ont optical-info 0/x/x 


Mostra diversas informações como: description, status, distancia, vendor Id, Equip ID, software/firmware version, SN...)
	\\show ont info 0/x/x (


Verificado sinal de todas as PONs)
	\\show ont optical-info interface gpon all (


Mostra os MACs aprendidos por determinada ONU
	\\show ont mac-address-table 0/x/x



Mostra tudo que esta associado a ONU: dba, vlan, unique e line)
	\\show ont profile 0/x/x 


Rebootar a ONU
	\\ont reboot <ont_id> 



show ont wan-status pppoe 0/x/x



show ont statistics 0/x/x traffic



Verificar Módulo SFP
	\\show interface sfp
	
	
Ativação da porta específica após configurar
	\\no shutdown


===========================
Alterar PVID da porta
============================
	\\switchport default vlan X

=========================================================
Atualização de Firmware
=========================================================
Atualização de firmware da OLT


	\\load application {tftp | ftp} {inet | inet6 } <server-ip> <file-name>
	\\reboot


Atualização da ONT por meio da OLT
	\\load ont-image {tftp | ftp} {inet | inet6 } <server-ip> <file-name>
Visualizar andamento
	\\\show ont-image
	
	
	
===================================================
Provisionamento Automático
===================================================
Criar
	\\ont auto-config { <index_num> [ name <name> ] } { all-ont | device-type
	<device_type>} line <line_profile>

Desfazer
	\\no ont auto-config { <index_num> [ name <name> ] }
	
Visualizar
	\\show running-config gpon-device
	
	
==============================================
Meth Interface - Out Of Band

Verificar as interfaces de gerência da OLT (meth-interface)

	\\show running-config if 
	\\ show ip interface meth interface 0
	
Acessar a Interface de Gerência Out Of Band (meth 0)
	\\interface meth-interface 0
		
Alterar IP da meth interface
	\\ip address {IP} {MASK}
	
	
	
==============================================
	
	
show deploy dba brief all (Comando para verificar o DBA criado)

show deploy vlan brief all (comando para mostrar as vlans

show deploy line brief all (mostra as lines configuradas e informa index, name, device type e interfaces referenced by rule)

show running-config deploy-profile-vlan (Comando para verificar a VLAN criada)

show running-config deploy-profile-line (Comando para verificar o LINE criado)

show deploy rule brief interface gpon all (Comando para verificar as ONUs provisionadas)

show deploy rule brief inused interface gpon all (É possível verificar as ativas com o comando)

show deploy rule brief inused sn string-hex [ITBS-1790032e] (Procurar ONU especifica dentro da OLT)

show ont-find list interface gpon all (Comando para verificar as ONUs disponíveis para provisionar)

show ont-find list interface gpon 0/x index x (Comando para verificar os detalhes das ONUs para provisionar)

show running-config gpon-device (Verificar configuração de auto-config feita)

show ont brief interface gpon all (mostra as ONU´s/ONT´s provisionadas informando modelo, serial numnber, status e posição)

show ont optical-info 0/x/x (Verificar sinal da ONU)

show ont info 0/x/x (mostra diversas informações como: description, status, distancia, vendor Id, Equip ID, software/firmware version, SN...)

show ont optical-info interface gpon all (Verificado sinal de todas as PONs)

show ont mac-address-table 0/x/x

show ont profile 0/x/x (mostra tudo que esta associado a ONU: dba, vlan, unique e line)

ont reboot (rebootar a ONU)

show ont wan-status pppoe 0/x/x
Provisionar ONU:
deploy profile rule
aim 0/x/x name [nome do profile rule]
permit sn string-hex [ITBS-e68f3201] line [aim LINE] default line [aim LINE]
active
----Para excluir:
delete aim 0/x/x


"Altera a distância" logicamente falando, em que as ONUS podem ser alcançadas, de 20KM padrão do gbic para 60 aqui no exemplo. pode resolver em casos em que não encontram alguma ONU
ont-find distance min 0 max 60 interface gpon all
(reinicia as PONs)


 
Reset OLT /formatar / zerar

	clear startup-config
	
	
	
-------------------------
	
alterar o nome da OLT
	hostname {name}
	
--------------------------

Permissão / Criar Usuário

	\\username Macedo privilege 2 password 0
	
	
	privilege
	0= nao altero nada
	2= administrador
	
	
	password
	0 = sem criptografia
	7 = com criptografia


Modificar senha de usuário admin
	
	adminname change-password
	Need to authenticate your login password: <current-password>
	Please input associated username: <user-to-change-password>
	Please input user new password: <new-password>
	Please input user confirm password: <new-password>
	
Visualizar

	show username

	
-------------------------


#Habilite o ssh 
GPON(config)# ssh
GPON(config)# exit

#Configure a chave padrão
GPON# crypto key generate rsa

#Ative a chave padrão
GPON# crypto key refresh

Verificar limite de conexões
	show ssh limit

Aumentar o limite de conexões SSH
	ssh limit (0-15)   - padrão é 10


======================================



Backup da OLT
	\\upload configuration tftp inet X.X.X.X  (filename)


Restaurar o Backup
	\\load configuration tftp inet X.X.X.X (filename)
	
========================================

Limitar sessão (telnet/ssh)

	ssh limit <session_limit>

Visualizar
	
	show ssh limit
	
	
	
Restaurar configuração com base em arquivo de backup enviado

Sintaxe:

Carregar o arquivo de configuração
	load configuration {tftp | ftp} {inet | inet6 } <server-ip> <file-name>

Confirmar substituição do arquivo de configuração de inicialização
	Startup config will be updated, are you sure(y/n)? y

Aplicar configuração inicialização substituindo a configuração corrente
	copy startup-config running-config


Parâmetros obrigatórios:

tftp: Download via TFTP;
ftp: Download via FTP;
inet: Protocolo de rede IPv4;
inet6: Protocolo de rede IPv6;
server-ip: Endereço IP do servidor;
file-name: Nome do arquivo;
Nota: Após a substituição do arquivo de configuração de inicialização o mesmo pode ser aplicado reiniciando o sistema ou substituindo a configuração corrente;

==================================================

Ver o tempo de aprendizagem MAC
	show mac-address-table age-time
	
	
	----------------------------------
	
	
validação de loop e criticidade por porta
	show alarm ont register-record 
	
=================================
CRIAÇAO DE "P2P" na G8 e G16 -  a ideia aqui é fazer com que CPEs se comuniquem e nessas OLTs esse fluxo se baseia em VLANs com os comandos abaixo:



vlan 33
description CLIENTE_CORPORATIVO
pon-switch
exit
interface vlan-interface 33
exit

A sintaxe exibida acima é com base na comunicação em VLAN, onde as ONUs que participarem desse segmento de VLAN poderão se enxergar. Com isso, as ONUs que não pertencem a essa VLAN não poderão enxergar a comunicação, dessa forma ficando isoladas. Contudo, além da VLAN 33 e sua descrição criada, há também dentro da configuração o comando pon-switch, que ativa a comunicação para ambos os lados das ONUs, as quais pertencem essa VLAN. Em seguida, é necessário apenas criar a interface dessa VLAN dentro da OLT para que ela possa coexistir com o comando interface vlan-interface 33, nada mais.

Feito isso a configuração está completa.


                    """
            print("=============================================")
            print("\033[0;34;40mComando a ser copiado:")
            print(comando3)
            print(f'============================================================================\n')
            if input("\033[0;32;40mDeseja copiar o comando? S/N\n").strip().lower() == "s":
                pyperclip.copy(comando3)
                
                print("Comando copiado para area de transferência, basta colar em sua OLT.")
            else:
                print("Comando NÃO copiado.")
        elif escolha_opção == "0":
            # Sair do programa
            print("\n\033[0;34;40mVoltando ao MENU PRINCIPAL...\033[m")
            time.sleep(2)
            return
        else:
            # Tratar escolhas inválidas
            print('\033[0;31;40mEscolha inválida. Por favor, escolha uma opção válida!\033[m')
            time.sleep(1)
            
pass