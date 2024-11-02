import requests
import time
from colorama import init, Fore, Style
import sys
import os
init(autoreset=True)

def print_welcome_message():
    print(r"""
╔═╗╦ ╦╔═╗╔╦╗╔═╗╦ ╦  ╔═╗╔═╗╦═╗╦╔═╗╔╦╗╔═╗
╚═╗╠═╣╠═╣ ║║║ ║║║║  ╚═╗║  ╠╦╝║╠═╝ ║ ╚═╗
╚═╝╩ ╩╩ ╩═╩╝╚═╝╚╩╝  ╚═╝╚═╝╩╚═╩╩   ╩ ╚═╝
          """)
    print(Fore.GREEN + Style.BRIGHT + "Shadow Scripts BOT")
    print(Fore.GREEN + Style.BRIGHT + "Update Link: https://github.com/ShadowScripts1/TG-dotcoin")
    print(Fore.GREEN + Style.BRIGHT + "For Free Consultation Join Telegram Channel: https://t.me/shadowscripters\n")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_credentials():
    try:
        with open('tokens.txt', 'r') as file:
            credentials_list = file.readlines()
        credentials = [cred.strip() for cred in credentials_list]
        return credentials
    except FileNotFoundError:
        print("File 'tokens.txt' not found. Make sure the file exists in the same directory as the script.")
        return []

def fetch_task_ids(apikey, authorization):
    url = 'https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/get_filtered_tasks'
    headers = {
        'accept': '/',
        'accept-language': 'en-US,en;q=0.9',
        'apikey': apikey,
        'authorization': f'Bearer {authorization}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'origin': 'https://dot.dapplab.xyz',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-client-info': 'postgrest-js/1.9.2',
        'x-telegram-user-id': '6726676206'
    }
    data = {'platform': 'ios', 'locale': 'en', 'is_premium': False}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        tasks = response.json()
        task_ids = [task['id'] for task in tasks]
        return task_ids
    else:
        print(f"Failed to fetch tasks, status code: {response.status_code}")
        return []

def upgrade_dtc_miner(apikey, authorization):
    url = 'https://api.dotcoin.bot/functions/v1/upgradeDTCMiner'
    headers = {
        'accept': '/',
        'accept-language': 'en-US,en;q=0.9',
        'apikey': apikey,
        'authorization': f'Bearer {authorization}',
        'cache-control': 'no-cache',
        'content-length': '0',
        'origin': 'https://dot.dapplab.xyz',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; M2012K11AG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6422.165 Mobile',
        'x-telegram-user-id': '6577110188'
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get('success', False):
            print(f"{Fore.GREEN+Style.BRIGHT}Successfully upgraded DTC Miner")
        else:
            print(f"{Fore.RED+Style.BRIGHT}Failed to upgrade DTC Miner, code: {response_data.get('code')}")
    else:
        print(f"{Fore.RED+Style.BRIGHT}Failed to upgrade DTC Miner, status code: {response.status_code}")

def add_attempts(lvl, apikey, authorization, current_level):
    url = 'https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/add_attempts'
    headers = {
        'accept': '/',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8',
        'apikey': apikey,
        'authorization': f'Bearer {authorization}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-client-info': 'postgrest-js/1.9.2'
    }

    while True:
        print(f"\r{Fore.CYAN+Style.BRIGHT}[ Upgrade ] : Trying to upgrade to level {lvl}", end="", flush=True)
        sys.stdout.flush()
        try:
            data = {'lvl': lvl}
            response = requests.post(url, headers=headers, json=data)
            response_data = response.json()
            if lvl > current_level:
                return False
            if response_data.get('success', False):
                return True
            else:
                lvl += 1
        except Exception as e:
            sys.stdout.write(f"Error while adding attempts: {e}\n")

def auto_clear_task(apikey, authorization):
    task_ids = fetch_task_ids(apikey, authorization)
    base_url = 'https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/complete_task'
    headers = {
        'accept': '/',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8',
        'apikey': apikey,
        'authorization': f'Bearer {authorization}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-client-info': 'postgrest-js/1.9.2'
    }
    for task_id in task_ids:
        data = {'oid': str(task_id)}
        response = requests.post(base_url, headers=headers, json=data)
        if response.status_code == 200:
            print(f"{Fore.GREEN+Style.BRIGHT}[ Task {task_id} ] : Success")
        else:
            print(f"{Fore.RED+Style.BRIGHT}[ Task {task_id} ] {task_id}. Status code: {response.status_code} : Failed")

def save_coins(coins, apikey, authorization):
    url = 'https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/save_coins'
    headers = {
        'accept': '/',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8',
        'apikey': apikey,
        'authorization': f'Bearer {authorization}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-client-info': 'postgrest-js/1.9.2'
    }
    data = {'coins': coins}

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error while saving coins: {e}")
        return False

def get_user_info(apikey, authorization):
    url = 'https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/get_user_info'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8',
        'apikey': apikey,
        'authorization': f'Bearer {authorization}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-client-info': 'postgrest-js/1.9.2'
    }
    data = {}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()

def auto_upgrade_daily_attempt():
    user_input = input("Auto upgrade daily attempt? (y/n): ")
    if user_input.lower() == 'y':
        try:
            upgrade_count = int(input("How many times do you want to upgrade? "))
            return upgrade_count
        except ValueError:
            print("Invalid input, must be a number.")
            return 0
    return 0

def auto_gacha(apikey, authorization, coins):
    url = 'https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/try_your_luck'
    headers = {
        'accept': '/',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8',
        'apikey': apikey,
        'authorization': f'Bearer {authorization}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-client-info': 'postgrest-js/1.9.2'
    }
    data = {'coins': coins}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get('success', False):
            print(f"{Fore.GREEN+Style.BRIGHT}[ Gacha ] : Won")
        else:
            print(f"{Fore.RED+Style.BRIGHT}[ Gacha ] : Failed")
    else:
        print(f"{Fore.RED+Style.BRIGHT}[ Gacha ] : Failed with status code {response.status_code}")

def restore_attempts(apikey, authorization):
    url = "https://api.dotcoin.bot/rest/v1/rpc/restore_attempt"
    headers = {
        "accept": "/",
        "accept-language": "en-US,en;q=0.9",
        "apikey": apikey,
        "authorization": f"Bearer {authorization}",
        "content-profile": "public",
        "content-type": "application/json",
        "origin": "https://dot.dapplab.xyz",
        "priority": "u=1, i",
        "referer": "https://dot.dapplab.xyz/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "x-client-info": "postgrest-js/1.9.2"
    }
    data = {}
    false_count = 0
    while false_count < 1:
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()
        cek_respons = response_data.get('success', False)
        if cek_respons == True:
            print(f"{Fore.GREEN+Style.BRIGHT}[ Restore Attempt ] : Successfully restored free energy")
        else:
            false_count += 1
            print(f"{Fore.RED+Style.BRIGHT}[ Restore  Attempt ] : Failed to restore energy, reached limit!")
        time.sleep(1)

def main():
    print_welcome_message()
    clear_task = input("Auto Clear Task? (default n) (y/n): ").strip().lower()
    if clear_task in ['y', 'n', '']:
        clear_task = clear_task or 'n'
    else:
        clear_task = 'n'
    credentials = load_credentials()
    upgrade_count = auto_upgrade_daily_attempt()  # Capture upgrade count from function
    upgrade_success = {}  # Dictionary to store upgrade status

    apikey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impqdm5tb3luY21jZXdudXlreWlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg3MDE5ODIsImV4cCI6MjAyNDI3Nzk4Mn0.oZh_ECA6fA2NlwoUamf1TqF45lrMC0uIdJXvVitDbZ8'

    auto_upgrade_dtc = input("Auto upgrade DTC Miner? (y/n): ").strip().lower()
    if auto_upgrade_dtc not in ['y', 'n']:
        auto_upgrade_dtc = 'n'
    
    while True:  # External loop that keeps the program running continuously
        for index, authorization in enumerate(credentials):
            info = get_user_info(apikey, authorization)
            print(f"{Fore.CYAN+Style.BRIGHT}============== [ Account {index} | {info['first_name']} ] ==============")

            if not upgrade_success.get(authorization, False):  # Check if upgrade hasn't succeeded yet
                if upgrade_count > 0:  # Check if upgrade_count is greater than 0
                    for _ in range(upgrade_count):
                        current_level = info['daily_attempts']
                        success = add_attempts(0, apikey, authorization, current_level)
                        if success:
                            upgrade_success[authorization] = True  # Save successful upgrade status
                            print(f"{Fore.GREEN+Style.BRIGHT}\r[ Upgrade ] : Success                           ", flush=True)
                            break
                        else:
                            print(f"{Fore.RED+Style.BRIGHT}\r[ Upgrade ] : Failed                          ", flush=True)
            
            if info:
                if clear_task == 'y':
                    auto_clear_task(apikey, authorization)
                print(f"{Fore.YELLOW+Style.BRIGHT}[ Level ] : {info['level']}")
                print(f"{Fore.YELLOW+Style.BRIGHT}[ Balance ] : {info['balance']}")
                print(f"{Fore.BLUE+Style.BRIGHT}[ Energy ] : {info['daily_attempts']}")
                print(f"{Fore.BLUE+Style.BRIGHT}[ Energy Limit ] : {info['limit_attempts']}")
                print(f"{Fore.BLUE+Style.BRIGHT}[ Multiple Click Level ] : {info['multiple_clicks']}")
                auto_gacha(apikey, authorization, 150000)
                energy = info['daily_attempts']
                while energy > 0:
                    for _ in range(energy):
                        print(f"{Fore.BLUE+Style.BRIGHT}\r[ Tap ] : Tapping..", end="", flush=True)
                        time.sleep(3)
                        save_coins(20000, apikey, authorization)
                        print(f"{Fore.GREEN+Style.BRIGHT}\r[ Tap ] : Success             ", flush=True)
                    info = get_user_info(apikey, authorization)
                    energy = info['daily_attempts']
                    if energy == 0:
                        restore_attempts(apikey, authorization)
                        info = get_user_info(apikey, authorization)
                        energy = info['daily_attempts']
                else:
                    print(f"{Fore.RED+Style.BRIGHT}Your energy is depleted. Waiting for energy refill...")
                    if energy == 0:
                        restore_attempts(apikey, authorization)
                        info = get_user_info(apikey, authorization)
                        energy = info['daily_attempts']

                if auto_upgrade_dtc == 'y':
                    upgrade_dtc_miner(apikey, authorization)

            else:
                print("\r{Fore.RED+Style.BRIGHT}Access token invalid, moving to next account.")
        time.sleep(2)
        # 30-second countdown after all accounts have been processed
        print(f"{Fore.CYAN+Style.BRIGHT}==============All accounts have been processed=================")
        for i in range(300, 0, -1):
            sys.stdout.write(f"\rReprocessing all accounts in {i} seconds...")
            sys.stdout.flush()
            time.sleep(1)
        print()  # Print new line after countdown finishes

        # Clear console after countdown
        clear_console()

if __name__ == "__main__":
    main()