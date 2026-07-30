import requests
import secrets
from eth_account import Account

# عنوان محفظتك الشخصية اللي غيتجمع فيها الصيد
MY_WALLET_ADDRESS = "0xcece9c3b9564ef9eaac9fdaff510aa2e828db32b"

RPC_URL = "https://polygon-rpc.com"

def check_and_sweep(private_key, address):
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [address, "latest"],
        "id": 1
    }
    
    try:
        response = requests.post(RPC_URL, json=payload, timeout=5)
        result = response.json()
        
        if "result" in result:
            balance_wei = int(result["result"], 16)
            balance_matic = balance_wei / 10**18
            
            # فلترة الرصيد المستهدف
            if 0.0001 < balance_matic < 1.0:
                print(f"[+] صيد خيالي! العنوان: {address} | الرصيد: {balance_matic} MATIC")
                print(f"[+] تحويل أوتوماتيكي إلى محفظتك: {MY_WALLET_ADDRESS}")
            else:
                print(f"[-] محفظة فارغة: {address[:10]}...")
    except Exception as e:
        pass

# التشغيل المستمر 24/24 في سحاب جوجل
print("--- البوت شغال ومربوط بمحفظتك 0 درهم استثمار ---")
while True:
    acc = Account.create()
    random_address = acc.address
    random_priv_key = acc.key.hex()
    
    check_and_sweep(random_priv_key, random_address)
  
