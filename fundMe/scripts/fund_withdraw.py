from brownie import FundMe
from scripts.helpfulScripts import getAccount


def fund():
    fund_me = FundMe[-1]
    account = getAccount()
    print(fund_me)

def main():
    fund()