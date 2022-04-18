from ctypes import addressof
from brownie import FundMe
from scripts.helpfulScripts import getAccount, getPriceFeedAddress

def deployFundMe():
    account             = getAccount()
    priceFeedAddress    = getPriceFeedAddress(account)
    fund_me             = FundMe.deploy( priceFeedAddress , {"from": account})
    print(f"Contract deployed to {fund_me.address}")

def main():
    deployFundMe()