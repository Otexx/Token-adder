from pystyle import *
import requests
import tls_client

def main(token):
    headers = {
        'authority': 'discord.com',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDExIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MjEiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTc2OTY2LCJuYXRpdmVfYnVpbGRfbnVtYmVyIjoyOTU4NCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
        'x-context-properties': 'eyJsb2NhdGlvbiI6IkNvbnRleHRNZW51In0=',
        'x-debug-options': 'bugReporterEnabled',
        'accept-language': 'en-US',
        'authorization': f'{token}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9011 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36',
        'x-discord-locale': 'en-GB',
        'accept': '*/*',
        'origin': 'https://discord.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': f'https://discord.com/channels/@me/{id_of_user}'
    }
    response = session.delete(
        f'https://discord.com/api/v9/users/@me/relationships/{id_of_user}',
        headers=headers,
        json={},
    )


    print(response.text)

    if response.status_code == 204:
        print(f"\033[32mFriend removed: {token}\033[0m")
    else:
        error_message = response.json().get('message', 'Unknown error occurred')
        print(f"Error with token {token}: {error_message}")
        print(f"API response status code: {response.status_code}")
    
    
    
if __name__ == "__main__":    
    session = tls_client.Session(client_identifier='chrome_109', random_tls_extension_order=True)
    request_url = "https://discord.com/api/v9/experiments?with_guild_experiments=true"
    r = session.get(request_url)

    token_filename = 'tokens.txt'
    id_of_user = int(input("UserID: ")) 
    num_tokens_to_add = int(input("Enter the number of tokens you want to remove: "))

    
    with open(token_filename, 'r') as f:
        tokens = f.read().splitlines()
    for token in tokens[:int(num_tokens_to_add)]:
        if ":" in token:
            token = token.split(":")[2]
        if token != "token_to_ignore":
            main(token)