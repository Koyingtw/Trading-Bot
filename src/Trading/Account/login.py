from fubon_neo.sdk import *
import sys 
import os
from dotenv import load_dotenv
load_dotenv()

def login():
    # 載入設定檔與登入
    sdk = FubonSDK()
    accounts = sdk.login(os.getenv("FUBON_ACCOUNT"), os.getenv("FUBON_PASSWORD"), os.getenv("FUBON_CA_PATH") , os.getenv("FUBON_CA_PASSWORD"))
    print(accounts)
    acc  = accounts.data[0]
    return acc

if __name__ == "__main__":
    login()