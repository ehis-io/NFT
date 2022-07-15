
from scripts.helpful_scripts import get_account, OPENSEA_URL, get_contract, fund_with_link
from brownie import AdvancedCollectable, network, config
from web3 import Web3
sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
#w3 = Web3(Web3.EthereumTesterProvider())

def deploy_and_create():
    account =get_account()
    
    advanced_collectable = AdvancedCollectable.deploy(
        get_contract('vrf_coordinator'),
        get_contract('link_token'),
        config['networks'][network.show_active()]['keyhash'],
        config['networks'][network.show_active()]['fee'],
        {'from': account}
    )
    fund_with_link(advanced_collectable.address)
    tx = advanced_collectable.CreateCollectable(
            {"from":account}
            )
    tx.wait(1)
    print(
        f"Awesome, you can view your NFT at {OPENSEA_URL.format(advanced_collectable.address, advanced_collectable.tokenCounter() - 1)}"
    )
    print("Please wait up to 20 minutes and hit the refresh metadata button. ")
    return advanced_collectable


def main():
    deploy_and_create()
