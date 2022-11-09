from decimal import *

import math
from solana.rpc.api import Client


def get_amount(input):
    return Decimal(input['result']['value']['amount']) / 10 ** int(input['result']['value']['decimals'])


def get_total_supply():
    client = Client("https://api.mainnet-beta.solana.com")
    return math.ceil(get_amount(client.get_token_supply('7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU')))

def get_totalsupply():
    client = Client("https://api.mainnet-beta.solana.com")
    circulating = get_total_supply()

    non_circulating_address = ['ChdRKwt6VPVTum6mnu7KW7FipTuiM1RSYNtrV1oXRdcV',
                               'E7ywW5TcnvwWWXXw1a18T59s2z4vUrGSKurGeSEAdJ7V']

    for x in non_circulating_address:
        circulating -= get_amount(client.get_token_account_balance(x))
    return math.ceil(circulating)
   
      

def get_circulating_supply():
    client = Client("https://api.mainnet-beta.solana.com")
    circulating = get_total_supply()

    non_circulating_address = ['ChdRKwt6VPVTum6mnu7KW7FipTuiM1RSYNtrV1oXRdcV',
                               'E7ywW5TcnvwWWXXw1a18T59s2z4vUrGSKurGeSEAdJ7V',
                               'HrQLfGuKviStdsNV78pL3f24VSrnzmbazRgBAxNS1dwK',
                               '6GkZyseEJyz6FXzZyiU4KmyvJKeWAf2R93QKx5BHiExK',
                               'AXR2bDHRxtVhr4LQMBmGr3c9TnxY9LTa8h3drpoo25bx',
                               'Ha2Bdjg64NjFoG7z49VUvFTHwKDx2nJttX25Kax2xnCU',
                               '651YY3Ax3qf67eYem9DoZQRbQdVnCzcHf3cz7FqsfMRh',
                               'B35TEcMxaphQx1gL9U8CfTUQqiq2HUb5nsk8nMhrvf7F',
                               'AYrSiyqc7zAaiRXsPYkjnKXoZzofMu8ho2aD1rmuoG4y']

    for x in non_circulating_address:
        circulating -= get_amount(client.get_token_account_balance(x))
    return math.ceil(circulating)
   
