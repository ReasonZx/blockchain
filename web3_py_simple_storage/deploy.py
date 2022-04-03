from solcx import compile_standard, install_solc
import json
from web3 import Web3


with open("./SimpleStorage.sol" , "r") as file:
    simple_storage_file = file.read();

install_solc("0.6.0")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol" : {"content": simple_storage_file}},
        "settings":{
            "outputSelection": {
                "*" : {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }

        },
    },
    solc_version = "0.6.0",
)

with open("./compiled_SimpleStorage.json", "w") as file:
    json.dump(compiled_sol, file)


#get bytecode

bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]


#get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]


w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
chain_id = 1337
myAdress = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
privateKey = "0x4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d"

#Create the contract in python
SimpleStorage = w3.eth.contract(abi = abi , bytecode=bytecode)

nonce = w3.eth.getTransactionCount(myAdress)

#Build a transaction
transaction = SimpleStorage.constructor().buildTransaction({

    "chainId" : chain_id, "gasPrice": w3.eth.gas_price, "from" : myAdress , "nonce" : nonce
})

#Sign the transaction
signedTransaction = w3.eth.account.sign_transaction(transaction, privateKey)

#Send the transaction
txHash = w3.eth.send_raw_transaction(signedTransaction.rawTransaction)
txReceipt = w3.eth.wait_for_transaction_receipt(txHash)

# working with the contract
simple_storage = w3.eth.contract(address = txReceipt.contractAddress, abi=abi)


#Interacting with the contract
print(simple_storage.functions.retrieve().call())

storeTx = simple_storage.functions.store(22).buildTransaction({

    "chainId" : chain_id, "gasPrice": w3.eth.gas_price, "from" : myAdress , "nonce" : nonce+1

})
signedStoreTx = w3.eth.account.sign_transaction(storeTx, privateKey)
storeTxHash = w3.eth.send_raw_transaction(signedStoreTx.rawTransaction)
storeTxReceipt = w3.eth.wait_for_transaction_receipt(storeTxHash)

print(simple_storage.functions.retrieve().call())