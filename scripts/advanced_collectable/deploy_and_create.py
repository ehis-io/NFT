
from scripts.helpful_scripts import get_account, OPENSEA_URL
from brownie import AdvancedCollectable

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deploy_and_create():
    account = get_account()
    advanced_collectable = AdvancedCollectable.deploy({"from": account})
    tx = advanced_collectable.createCollectable(sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        f"Awesome, you can view your NFT at {OPENSEA_URL.format(advanced_collectible.address, advanced_collectible.tokenCounter() - 1)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button. ")
    return advanced_collectable


def main():
    deploy_and_create()
