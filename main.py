from queue import Queue
from colorama import Fore, Style, init, Back
import os

init(autoreset=True)

class Caixa:
    def __init__(self):
        self.fila_prioritaria = Queue()
        self.fila_normal = Queue()

    def entrada_clientes(self):
        while True:
            print(f"\n{Fore.CYAN}=== Cadastro de Clientes ==={Style.RESET_ALL}")
            nome_cliente = input("Nome do cliente: ").strip().title()
            if not nome_cliente:
                print(f"{Fore.RED}Nome não pode estar vazio! Tente novamente.{Style.RESET_ALL}")
                continue

            info = input("Tipo (gestante/autista/pessoa normal): ").strip().lower()
            while info not in ['gestante', 'autista', 'pessoa normal']:
                print(f"{Fore.RED}Opção inválida! Escolha: gestante, autista ou pessoa normal.{Style.RESET_ALL}")
                info = input("Tipo (gestante/autista/pessoa normal): ").strip().lower()

            try:
                idade = int(input("Idade: "))
                if idade < 0:
                    raise ValueError
            except ValueError:
                print(f"{Fore.RED}Idade inválida! Digite um número inteiro positivo.{Style.RESET_ALL}")
                continue
            
            cliente = {"nome": nome_cliente, "idade": idade, "info": info}
            
            if info in ["gestante", "autista"] or idade >= 65:
                self.fila_prioritaria.put(cliente)
                print(f"{Fore.GREEN}Cliente prioritário adicionado com sucesso!{Style.RESET_ALL}")
            else:
                self.fila_normal.put(cliente)
                print(f"{Fore.YELLOW}Cliente normal adicionado com sucesso!{Style.RESET_ALL}")
            
            op = input("\nDeseja adicionar mais clientes? (s/n): ").strip().lower()
            if op not in ['s', 'n']:
                print(f"{Fore.RED}Opção inválida! Digite 's' para sim ou 'n' para não.{Style.RESET_ALL}")
                continue
            if op == 'n':
                break

    def atende_clientes(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"\n{Fore.LIGHTRED_EX}=== Atendendo Clientes ==={Style.RESET_ALL}")
        
        while not self.fila_prioritaria.empty():
            cliente = self.fila_prioritaria.get()
            print(f"{Fore.GREEN}Atendendo prioritário: {cliente['nome']} ({cliente['info']}){Style.RESET_ALL}")
        
        while not self.fila_normal.empty():
            cliente = self.fila_normal.get()
            print(f"{Fore.CYAN}Atendendo normal: {cliente['nome']} ({cliente['info']}){Style.RESET_ALL}")
        
        print(f"\n{Fore.LIGHTGREEN_EX}Todos os clientes foram atendidos.{Style.RESET_ALL}")

    def mostrar_filas(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"\n{Fore.LIGHTYELLOW_EX}=== Fila Atual ==={Style.RESET_ALL}")
        
        if self.fila_prioritaria.empty() and self.fila_normal.empty():
            print(f"{Fore.RED}Não há clientes na fila.{Style.RESET_ALL}")
        else:
            print("\nClientes Prioritários:")
            for cliente in list(self.fila_prioritaria.queue):
                print(f"  - {cliente['nome']} ({cliente['info']})")

            print("\nClientes Normais:")
            for cliente in list(self.fila_normal.queue):
                print(f"  - {cliente['nome']} ({cliente['info']})")
        
        print(f"\n{Fore.CYAN}{'=' * 40}{Style.RESET_ALL}")

def menu():
    caixa = Caixa()
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"\n{Fore.YELLOW}=== SISTEMA DE FILA PRIORITÁRIO ==={Style.RESET_ALL}")
        print(f"[1] - {Fore.GREEN}Adicionar Clientes")
        print(f"[2] - {Fore.LIGHTYELLOW_EX}Mostrar Fila")
        print(f"[3] - {Fore.LIGHTRED_EX}Atender Clientes")
        print(f"[4] -  {Back.LIGHTWHITE_EX}{Fore.RED} Sair {Style.RESET_ALL}")
        
        opcao = input("\nEscolha uma opção: ").strip()
        if opcao not in ['1', '2', '3', '4']:
            print(f"{Fore.RED}Opção inválida! Tente novamente.{Style.RESET_ALL}")
            input("\nPressione Enter para tentar novamente...")
            continue
        
        if opcao == '1':
            caixa.entrada_clientes()
        elif opcao == '2':
            caixa.mostrar_filas()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == '3':
            caixa.atende_clientes()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == '4':
            print(f"{Fore.LIGHTRED_EX}Saindo do sistema...{Style.RESET_ALL}")
            break

menu()
        