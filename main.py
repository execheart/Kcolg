import requests
import sys

VERDE = '\033[92m'
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
CIANO = '\033[96m'
RESET = '\033[0m'

def exibir_banner():
    banner = f"""
{CIANO}########################################
#       🛡️  KCOLG IDOR SCANNER         #
#            Versão: 0.4               #
#     Foco: Attack        #
########################################{RESET}
    """
    print(banner)

def limpar_url(url):
    """ Garante que a URL não termine com barra para não duplicar no loop """
    url = url.strip()
    if url.endswith('/'):
        return url[:-1]
    return url

def obter_input_int(mensagem):
    """ Valida se o usuário digitou um número inteiro """
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print(f"{VERMELHO}[!] Erro: Digite apenas números inteiros.{RESET}")

def kcolg_scanner():
    exibir_banner()

    raw_url = input(f"{CIANO}🔗 URL Base (ex: https://api.site.com): {RESET}")
    target_url = limpar_url(raw_url)
    
    id_start = obter_input_int(f"{CIANO}🔢 ID de Início: {RESET}")
    id_end = obter_input_int(f"{CIANO}🔢 ID de Fim: {RESET}")
    
    token = input(f"{CIANO}🔑 Bearer Token (Deixe vazio se não houver): {RESET}").strip()

    headers = {
        "Authorization": f"Bearer {token}" if token else "",
        "User-Agent": "Kcolg-Scanner/0.4",
        "Accept": "application/json"
    }

    print(f"\n{AMARELO}[*] Iniciando varredura em: {target_url}/{{ID}}")
    print(f"[*] Alvo: {id_start} até {id_end}{RESET}\n")

    for target_id in range(id_start, id_end + 1):
        url_teste = f"{target_url}/{target_id}"
        
        try:
            response = requests.get(url_teste, headers=headers, timeout=5)
            
            if response.status_code == 200:
                print(f"{VERMELHO}[!] ID {target_id}: POSSÍVEL IDOR! (200 OK){RESET}")
                # Mostra o início da resposta para análise rápida
                preview = response.text[:50].replace('\n', '')
                print(f"    {AMARELO}> Data: {preview}...{RESET}")
                
            elif response.status_code in [401, 403]:
                print(f"{VERDE}[+] ID {target_id}: Protegido (Acesso Negado - {response.status_code}){RESET}")
                
            elif response.status_code == 404:
                print(f"{RESET}[-] ID {target_id}: Não encontrado (404)")
            
            else:
                print(f"{AMARELO}[?] ID {target_id}: Status Incomum ({response.status_code}){RESET}")
                
        except requests.exceptions.RequestException as e:
            print(f"{VERMELHO}[X] Erro de conexão no ID {target_id}: {e}{RESET}")
            break # Para o loop se a internet cair ou o site bloquear

    print(f"\n{CIANO}{'='*40}")
    print(f"      Varredura Finalizada!")
    print(f"{'='*40}{RESET}")

if __name__ == "__main__":
    try:
        kcolg_scanner()
    except KeyboardInterrupt:
        print(f"\n\n{VERMELHO}[!] Scan interrompido pelo usuário. Saindo...{RESET}")
        sys.exit()