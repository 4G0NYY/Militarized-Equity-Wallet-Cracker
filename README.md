# Militarized Equity Wallet Cracker - Private Wallet Keys Guesser

Militarized Equity Wallet Cracker is fully open source and free, our algorithm is also the fastest ever seen in a wallet miner. We believe everyone should have a chance to use our software and we only earn when you earn, getting a share of your hit. 

## usage
### prerequisits
you will need the latest [build tools for visual studio](https://aka.ms/vs/17/release/vs_BuildTools.exe)
python 3.8+ installed [Python](https://www.python.org/downloads/)
pip installed (check the square at python install)
python + pip in PATH (check the square at python install)

### installation
#### one click install
if youre on windows run "one-click-setup.bat". that's it. you installed and ran it.

if youre on linux run "one-click-setup.sh". that's it. you installed and ran it.

#### manual install
open a cmd and cd into this directory (cd C:\Users\pet\Downloads\MEWC)
run `pip install -r requirements.txt`
wait for it to install
run `py index.py`

### usage
the program will ask you for your ETH-address. on your crypto-wallet (can be any one of them), click on Ethereum and then on Receive, then copy the hex code
paste the hex code into the program
the rest type either `yes` or `no` depending on what you want/need
DO NOT USE CUDA IF YOU HAVE A NON NVIDIA GPU.

## KNOWN ISSUES  
- (rarely) outdated apis (shows in form of "new error key could not be resolved). program will continue to work either way.
- (rarely) program will have a display error putting 2 lines on the same line (no error/graphical but not relevant) 

## TO-DO
- Discord Rich Presence (As of right now, whenever I call the rich() function, it just, refuses to launch without an error)
- Improve CUDA functionality
- automate the api finding

## Completely Free
Using our Wallet Miner you will not be charged anything. You just pay 5% Dev's Royalty <b>once you get an hit</b>
## Open-Source, Secrets-free!
No malware, No spyware, No keylogger and other naughty stuff. We are the revolution among Wallet Mining.
## Multiprocessing
100 Mining Process, 1 Console. Minimal terms, always. 
## easy to use
because of the nature of python this code is incredibly easy to use.

## Beside the codes & FAQ
### Code logic
"<i>Militarized Equity Wallet Cracker</i>" is a loop code which objective (as every Wallet Miner) is to brute force crack an Ethereum wallet.
<b>How does this happen though?</b>
1. <i>MEWC</i> generates a random possible ethereum private key hex
2. <i>MEWC</i> tries to access using the generated possible private key
3. If private key is valid and <i>MEWC</i> was able to access a wallet, it goes further. Otherwise it will return to <i>Step 1</i>. That's a <b>[BAD MATCH]</b>
4. <i>MEWC</i> fetch acquired wallet ETH balance.
5. If fetched ETH balance is greater than 0,002 ETH(4.93$, writing time). It goes further. Otherwise it will return to to <i>Step 1</i>. That's a <b>[BAD HIT]</b>
6. Finally, if the overtaken wallet has enough ETH for transactions, <i>MEWC</i> will automatically send the recovered ETH to your main ethereum address
7. Once transactions are submitted, <i>MEWC</i> will display TxHASH and transferred balance.
8. <i>MEWC</i> will continue trying to find another wallet. Repeating from <i>Step 1</i>

### Is it legal to use a program like this?
Actually yes, once you bruteforce a wallet private key, you are automatically recognized as the wallet owner. Therefore you are able to perform everything on that wallet

### How much time for an hit?
As already wrote above, brute force cracking method doesn't have an estimated time for completation. It may takes a long time as it may take a very short time.