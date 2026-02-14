]import requests

def kcolg_scanner(url_base, id_inicio, id_fim, token_auth):
    print(f"\n{'='*40}")
    print(f"🚀 KCOLG IDOR SCANNER - Módulo de Autenticação")
    print(f"{'='*40}\n")

    headers = {
        "Authorization": f"Bearer {token_auth}",
        "Content-Type": "application/json",
        "User-Agent": "Kcolg-Security-Scanner/1.0"
    }

    for target_id in range(id_inicio, id_fim + 1):
        url_teste = f"{url_base}/{target_id}"
        
        try:
            response = requests.get(url_teste, headers=headers, timeout=5)
            
            if response.status_code == 200:
                print(f"[!] ID {target_id}: ACESSO PERMITIDO (Verificar se os dados são privados!)")
            elif response.status_code == 403 or response.status_code == 401:
                print(f"[-] ID {target_id}: Bloqueado (Sistema Seguro)")
            else:
                print(f"[?] ID {target_id}: Status {response.status_code}")
                
        except Exception as e:
            print(f"[X] Erro: {e}")


MEU_TOKEN = "h23_secret_token_123"
kcolg_scanner("https://jsonplaceholder.typicode.com", 1, 5, MEU_TOKEN)