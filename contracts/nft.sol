//SPDX-License-Identifier:MIT
pragma solidity ^0.8.0;
import '@openzeppelin/contracts/token/ERC721/ERC721.sol';
import '@chainlink/contracts/src/v0.6/VRFConsumerBase.sol';

contract Dutch is ERC721 {
    uint256 tokenCounter;
    uint256 public keyhash;
    uint256 public fee;
    enum Breed{'PUG', 'SHIBA_INU', 'ST_BERNARD'}
    mapping(uint256 => Breed ) public tokenIdToBreed;
    mapping (bytes32 => address) public requestIdToSender;

    constructor(address _vrfCoordinator, address _linkToken, bytes32 _keyhash, uint256 _fee) public
        VRFConsumerBase(_vrfCoordinator, _linkToken)
        ERC721 ('Dutchman Token', DUTCH)
        {
        tokenCounter =0
        keyhash = _keyhash;
        fee = _fee
        }
    
        function Dutch(string memory tokenURI)public returns (bytes32){
            bytes32 requestId = requestRandomness(keyhash, fee);
            requestIdToSender[requestId] = msg.sender;

        }

        function fufillRandomness(bytes32 requestId, uint256 randomNumber) internal override{
            Breed breed = Breed(randomNumber % 3);
            uint256 newTokenID = tokenCounter;

            tokenIdToBreed[newTokenID]= breed;
            address owner = requestIdToSender[requestId]
            _safeMint(owner, newTokenId);
            tokenCounter =tokenCounter + 1;
        }

