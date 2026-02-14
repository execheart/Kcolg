import requests

VERDE = '\033[92m'
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
RESET = '\033[0m'

def kcolg_scanner():
    print(f"{AMARELO}{'='*40}")
    print(f"   KCOLG IDOR SCANNER - v0.3")
    print(f"{'='*40}{RESET}\n")

    target_url = input("🔗 Digite a URL Base (ex: https://api.site.com): ")
    id_start = int(input("🔢 ID de Início: "))
    id_end = int(input("🔢 ID de Fim: "))
    token = input("🔑 Digite o Bearer Token (ou deixe vazio): ")

    headers = {
        "Authorization": f"Bearer {token}" if token else "",
        "User-Agent": "Kcolg-Scanner/0.3"
    }

    print(f"\n{AMARELO}[*] Iniciando varredura...{RESET}\n")

    for target_id in range(id_start, id_end + 1):
        url_teste = f"{target_url}/{target_id}"
        
        try:
            response = requests.get(url_teste, headers=headers, timeout=5)
            
            if response.status_code == 200:
                print(f"{VERMELHO}[!] ID {target_id}: POSSÍVEL IDOR! (200 OK){RESET}")
                # Mostra um pedaço da resposta para confirmar
                print(f"    > Data: {response.text[:60]}...")
            elif response.status_code == 403 or response.status_code == 401:
                print(f"{VERDE}[+] ID {target_id}: Protegido (Acesso Negado){RESET}")
            else:
                print(f"[-] ID {target_id}: Status {response.status_code}")
                
        except Exception as e:
            print(f"{VERMELHO}[X] Erro de conexão no ID {target_id}{RESET}")

if __name__ == "__main__":
    kcolg_scanner()