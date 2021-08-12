CRYPTO TRACKER
==============
A crypto coin price tracker for Raspberry PI with Sense HAT.

On Raspberry PI (with Sense HAT):
- sudo apt install libatlas-base-dev sense-hat
- ./run_sensehat.sh

Defaults to BTC, ETH and ADA. The list of coins can be changed in the init
function or call to the crypto_tracker class.

The text color changes based on the previous 24h price change. The data is updated every 60 seconds. 
