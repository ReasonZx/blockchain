from brownie import FundMe
from scripts.helpfulScripts import getAccount

def deployFundMe():
    account = getAccount()
    print(account)

def main():
    deployFundMe()