import requests
import sys
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

VERDE = '\033[92m'
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
CIANO = '\033[96m'
RESET = '\033[0m'

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/119.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
]

def exibir_banner():
    banner = f"""
{CIANO}########################################
#       🛡️  KCOLG IDOR SCANNER         #
#            Versão: 0.5               #
#     Foco: Multithread Attack         #
########################################{RESET}
    """
    print(banner)

def limpar_url(url):
    url = url.strip()
    return url[:-1] if url.endswith('/') else url

def obter_input_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print(f"{VERMELHO}[!] Erro: Digite apenas números.{RESET}")

def scan_task(target_id, target_url, headers):
    """ Função que cada 'thread' executa individualmente """
    time.sleep(random.uniform(0.1, 0.4))
    
    current_headers = headers.copy()
    current_headers["User-Agent"] = random.choice(USER_AGENTS)
    
    url_teste = f"{target_url}/{target_id}"
    
    try:
        response = requests.get(url_teste, headers=current_headers, timeout=7)
        
        if response.status_code == 200:
            preview = response.text[:50].replace('\n', '')
            return f"{VERMELHO}[!] ID {target_id}: POSSÍVEL IDOR! (200 OK)\n    > Data: {preview}...{RESET}"
        elif response.status_code in [401, 403]:
            return f"{VERDE}[+] ID {target_id}: Protegido ({response.status_code}){RESET}"
        elif response.status_code == 404:
            return f"{RESET}[- ] ID {target_id}: Não encontrado (404){RESET}"
        else:
            return f"{AMARELO}[?] ID {target_id}: Status {response.status_code}{RESET}"
            
    except Exception as e:
        return f"{VERMELHO}[X] Erro no ID {target_id}: Timeout/Conexão{RESET}"

def kcolg_scanner():
    exibir_banner()

    raw_url = input(f"{CIANO}🔗 URL Base: {RESET}")
    target_url = limpar_url(raw_url)
    
    id_start = obter_input_int(f"{CIANO}🔢 ID de Início: {RESET}")
    id_end = obter_input_int(f"{CIANO}🔢 ID de Fim: {RESET}")
    threads = obter_input_int(f"{CIANO}🚀 Número de Threads (Recomendado 5-10): {RESET}")
    
    token = input(f"{CIANO}🔑 Bearer Token (Vazio se não houver): {RESET}").strip()

    headers = {
        "Authorization": f"Bearer {token}" if token else "",
        "Accept": "application/json"
    }

    print(f"\n{AMARELO}[*] Iniciando ataque atômico em: {target_url}")
    print(f"[*] Motores ligados: {threads} threads em paralelo.{RESET}\n")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(scan_task, i, target_url, headers) for i in range(id_start, id_end + 1)]
        
        for future in as_completed(futures):
            print(future.result())

    print(f"\n{CIANO}{'='*40}\n      Varredura Finalizada!\n{'='*40}{RESET}")

if __name__ == "__main__":
    try:
        kcolg_scanner()
    except KeyboardInterrupt:
        print(f"\n\n{VERMELHO}[!] Abortar missão! Saindo...{RESET}")
        sys.exit()
