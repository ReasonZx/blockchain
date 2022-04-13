from brownie import FundMe
from scripts.helpfulScripts import getAccount

def deployFundMe():
    account     = getAccount()
    fund_me     = FundMe.deploy({"from": account})
    print(f"Contract deployed to {fund_me.address}")

def main():
    deployFundMe()