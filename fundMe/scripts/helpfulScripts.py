from brownie import accounts, network, config, MockV3Aggregator

def getAccount():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def getPriceFeedAddress(_account):
    if network.show_active() == "development":
        mockAggregator = MockV3Aggregator.deploy(18, 2000000000000000000000, {"from": _account})
        return mockAggregator.address
    else:
        return config["networks"][network.show_active()]["eth_usd_price_feed"]