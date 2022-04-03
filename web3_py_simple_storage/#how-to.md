1. 
Run:
>$ganache-cli -d 

More info in here: https://docs.nethereum.com/en/latest/ethereum-and-clients/ganache-cli/


\
\
2. 
Edit the following variables for deployment:

>w3 = Web3(Web3.HTTPProvider("HTTP://MY_PROVIDER")) \
chain_id = 1337 \
myAdress = "0xMY_ADDRESS" \
privateKey = "0xPVT_KEY" 

\
\
3.
On another terminal run:
>python deploy.py