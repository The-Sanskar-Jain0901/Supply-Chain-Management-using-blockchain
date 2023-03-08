from datetime import datetime
import json
from web3 import Web3
from datetime import datetime
from hexbytes import HexBytes

abi_edi = '''[
	{
		"inputs": [],
		"name": "generateQrCode",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "date",
				"type": "string"
			}
		],
		"name": "setExpiryDate",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "date",
				"type": "string"
			}
		],
		"name": "setMfgDate",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "time",
				"type": "string"
			}
		],
		"name": "setTimeStamp",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "signDigitally",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "verifyForDistributor",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "verifyForPharmacist",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "expiryDate",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getExpiryDate",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getMfgDate",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getName",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getTimeStamp",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "itemName",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "mfgDate",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "timestamp",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]'''


abi_signature = '''[
	{
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "_messageHash",
				"type": "bytes32"
			}
		],
		"name": "getEthSignedMessageHash",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_amount",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_message",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_nonce",
				"type": "uint256"
			}
		],
		"name": "getMessageHash",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "_ethSignedMessageHash",
				"type": "bytes32"
			},
			{
				"internalType": "bytes",
				"name": "_signature",
				"type": "bytes"
			}
		],
		"name": "recoverSigner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes",
				"name": "sig",
				"type": "bytes"
			}
		],
		"name": "splitSignature",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "r",
				"type": "bytes32"
			},
			{
				"internalType": "bytes32",
				"name": "s",
				"type": "bytes32"
			},
			{
				"internalType": "uint8",
				"name": "v",
				"type": "uint8"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_signer",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_amount",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_message",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_nonce",
				"type": "uint256"
			},
			{
				"internalType": "bytes",
				"name": "signature",
				"type": "bytes"
			}
		],
		"name": "verify",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	}
]'''

bytecode = {
	"functionDebugData": {},
	"generatedSources": [],
	"linkReferences": {},
	"object": "608060405234801561001057600080fd5b50610c89806100206000396000f3fe608060405234801561001057600080fd5b50600436106100f55760003560e01c80636c6526aa11610097578063da235b2211610066578063da235b2214610218578063ddab370514610236578063ddd5787214610240578063f2225a0f1461025c576100f5565b80636c6526aa146101a457806398727a0e146101c05780639e650a49146101de578063b80777ea146101fa576100f5565b80633497a50c116100d35780633497a50c1461015457806340401fea1461015e578063516dde431461017c5780636adecdb51461019a576100f5565b806311a08d01146100fa57806317d7de7c146101185780632d8ed84a14610136575b600080fd5b610102610266565b60405161010f91906107b7565b60405180910390f35b6101206102f8565b60405161012d91906107b7565b60405180910390f35b61013e61038a565b60405161014b91906107b7565b60405180910390f35b61015c61041c565b005b61016661041e565b60405161017391906107b7565b60405180910390f35b6101846104ac565b60405161019191906107b7565b60405180910390f35b6101a261053a565b005b6101be60048036038101906101b99190610922565b61053c565b005b6101c861054f565b6040516101d591906107b7565b60405180910390f35b6101f860048036038101906101f39190610922565b6105dd565b005b6102026105f0565b60405161020f91906107b7565b60405180910390f35b61022061067e565b60405161022d91906107b7565b60405180910390f35b61023e610710565b005b61025a60048036038101906102559190610922565b610712565b005b610264610725565b005b6060600280546102759061099a565b80601f01602080910402602001604051908101604052809291908181526020018280546102a19061099a565b80156102ee5780601f106102c3576101008083540402835291602001916102ee565b820191906000526020600020905b8154815290600101906020018083116102d157829003601f168201915b5050505050905090565b6060600180546103079061099a565b80601f01602080910402602001604051908101604052809291908181526020018280546103339061099a565b80156103805780601f1061035557610100808354040283529160200191610380565b820191906000526020600020905b81548152906001019060200180831161036357829003601f168201915b5050505050905090565b6060600380546103999061099a565b80601f01602080910402602001604051908101604052809291908181526020018280546103c59061099a565b80156104125780601f106103e757610100808354040283529160200191610412565b820191906000526020600020905b8154815290600101906020018083116103f557829003601f168201915b5050505050905090565b565b6001805461042b9061099a565b80601f01602080910402602001604051908101604052809291908181526020018280546104579061099a565b80156104a45780601f10610479576101008083540402835291602001916104a4565b820191906000526020600020905b81548152906001019060200180831161048757829003601f168201915b505050505081565b600380546104b99061099a565b80601f01602080910402602001604051908101604052809291908181526020018280546104e59061099a565b80156105325780601f1061050757610100808354040283529160200191610532565b820191906000526020600020905b81548152906001019060200180831161051557829003601f168201915b505050505081565b565b806002908161054b9190610b81565b5050565b6002805461055c9061099a565b80601f01602080910402602001604051908101604052809291908181526020018280546105889061099a565b80156105d55780601f106105aa576101008083540402835291602001916105d5565b820191906000526020600020905b8154815290600101906020018083116105b857829003601f168201915b505050505081565b80600390816105ec9190610b81565b5050565b600080546105fd9061099a565b80601f01602080910402602001604051908101604052809291908181526020018280546106299061099a565b80156106765780601f1061064b57610100808354040283529160200191610676565b820191906000526020600020905b81548152906001019060200180831161065957829003601f168201915b505050505081565b60606000805461068d9061099a565b80601f01602080910402602001604051908101604052809291908181526020018280546106b99061099a565b80156107065780601f106106db57610100808354040283529160200191610706565b820191906000526020600020905b8154815290600101906020018083116106e957829003601f168201915b5050505050905090565b565b80600090816107219190610b81565b5050565b565b600081519050919050565b600082825260208201905092915050565b60005b83811015610761578082015181840152602081019050610746565b60008484015250505050565b6000601f19601f8301169050919050565b600061078982610727565b6107938185610732565b93506107a3818560208601610743565b6107ac8161076d565b840191505092915050565b600060208201905081810360008301526107d1818461077e565b905092915050565b6000604051905090565b600080fd5b600080fd5b600080fd5b600080fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b61082f8261076d565b810181811067ffffffffffffffff8211171561084e5761084d6107f7565b5b80604052505050565b60006108616107d9565b905061086d8282610826565b919050565b600067ffffffffffffffff82111561088d5761088c6107f7565b5b6108968261076d565b9050602081019050919050565b82818337600083830152505050565b60006108c56108c084610872565b610857565b9050828152602081018484840111156108e1576108e06107f2565b5b6108ec8482856108a3565b509392505050565b600082601f830112610909576109086107ed565b5b81356109198482602086016108b2565b91505092915050565b600060208284031215610938576109376107e3565b5b600082013567ffffffffffffffff811115610956576109556107e8565b5b610962848285016108f4565b91505092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b600060028204905060018216806109b257607f821691505b6020821081036109c5576109c461096b565b5b50919050565b60008190508160005260206000209050919050565b60006020601f8301049050919050565b600082821b905092915050565b600060088302610a2d7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff826109f0565b610a3786836109f0565b95508019841693508086168417925050509392505050565b6000819050919050565b6000819050919050565b6000610a7e610a79610a7484610a4f565b610a59565b610a4f565b9050919050565b6000819050919050565b610a9883610a63565b610aac610aa482610a85565b8484546109fd565b825550505050565b600090565b610ac1610ab4565b610acc818484610a8f565b505050565b5b81811015610af057610ae5600082610ab9565b600181019050610ad2565b5050565b601f821115610b3557610b06816109cb565b610b0f846109e0565b81016020851015610b1e578190505b610b32610b2a856109e0565b830182610ad1565b50505b505050565b600082821c905092915050565b6000610b5860001984600802610b3a565b1980831691505092915050565b6000610b718383610b47565b9150826002028217905092915050565b610b8a82610727565b67ffffffffffffffff811115610ba357610ba26107f7565b5b610bad825461099a565b610bb8828285610af4565b600060209050601f831160018114610beb5760008415610bd9578287015190505b610be38582610b65565b865550610c4b565b601f198416610bf9866109cb565b60005b82811015610c2157848901518255600182019150602085019450602081019050610bfc565b86831015610c3e5784890151610c3a601f891682610b47565b8355505b6001600288020188555050505b50505050505056fea264697066735822122026886ee2d24f23813114d5b29a38961ccddb6e1c94f7b7d0fff763c0f63cf5a264736f6c63430008130033",
	"opcodes": "PUSH1 0x80 PUSH1 0x40 MSTORE CALLVALUE DUP1 ISZERO PUSH2 0x10 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH2 0xC89 DUP1 PUSH2 0x20 PUSH1 0x0 CODECOPY PUSH1 0x0 RETURN INVALID PUSH1 0x80 PUSH1 0x40 MSTORE CALLVALUE DUP1 ISZERO PUSH2 0x10 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH1 0x4 CALLDATASIZE LT PUSH2 0xF5 JUMPI PUSH1 0x0 CALLDATALOAD PUSH1 0xE0 SHR DUP1 PUSH4 0x6C6526AA GT PUSH2 0x97 JUMPI DUP1 PUSH4 0xDA235B22 GT PUSH2 0x66 JUMPI DUP1 PUSH4 0xDA235B22 EQ PUSH2 0x218 JUMPI DUP1 PUSH4 0xDDAB3705 EQ PUSH2 0x236 JUMPI DUP1 PUSH4 0xDDD57872 EQ PUSH2 0x240 JUMPI DUP1 PUSH4 0xF2225A0F EQ PUSH2 0x25C JUMPI PUSH2 0xF5 JUMP JUMPDEST DUP1 PUSH4 0x6C6526AA EQ PUSH2 0x1A4 JUMPI DUP1 PUSH4 0x98727A0E EQ PUSH2 0x1C0 JUMPI DUP1 PUSH4 0x9E650A49 EQ PUSH2 0x1DE JUMPI DUP1 PUSH4 0xB80777EA EQ PUSH2 0x1FA JUMPI PUSH2 0xF5 JUMP JUMPDEST DUP1 PUSH4 0x3497A50C GT PUSH2 0xD3 JUMPI DUP1 PUSH4 0x3497A50C EQ PUSH2 0x154 JUMPI DUP1 PUSH4 0x40401FEA EQ PUSH2 0x15E JUMPI DUP1 PUSH4 0x516DDE43 EQ PUSH2 0x17C JUMPI DUP1 PUSH4 0x6ADECDB5 EQ PUSH2 0x19A JUMPI PUSH2 0xF5 JUMP JUMPDEST DUP1 PUSH4 0x11A08D01 EQ PUSH2 0xFA JUMPI DUP1 PUSH4 0x17D7DE7C EQ PUSH2 0x118 JUMPI DUP1 PUSH4 0x2D8ED84A EQ PUSH2 0x136 JUMPI JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH2 0x102 PUSH2 0x266 JUMP JUMPDEST PUSH1 0x40 MLOAD PUSH2 0x10F SWAP2 SWAP1 PUSH2 0x7B7 JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH2 0x120 PUSH2 0x2F8 JUMP JUMPDEST PUSH1 0x40 MLOAD PUSH2 0x12D SWAP2 SWAP1 PUSH2 0x7B7 JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH2 0x13E PUSH2 0x38A JUMP JUMPDEST PUSH1 0x40 MLOAD PUSH2 0x14B SWAP2 SWAP1 PUSH2 0x7B7 JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH2 0x15C PUSH2 0x41C JUMP JUMPDEST STOP JUMPDEST PUSH2 0x166 PUSH2 0x41E JUMP JUMPDEST PUSH1 0x40 MLOAD PUSH2 0x173 SWAP2 SWAP1 PUSH2 0x7B7 JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH2 0x184 PUSH2 0x4AC JUMP JUMPDEST PUSH1 0x40 MLOAD PUSH2 0x191 SWAP2 SWAP1 PUSH2 0x7B7 JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH2 0x1A2 PUSH2 0x53A JUMP JUMPDEST STOP JUMPDEST PUSH2 0x1BE PUSH1 0x4 DUP1 CALLDATASIZE SUB DUP2 ADD SWAP1 PUSH2 0x1B9 SWAP2 SWAP1 PUSH2 0x922 JUMP JUMPDEST PUSH2 0x53C JUMP JUMPDEST STOP JUMPDEST PUSH2 0x1C8 PUSH2 0x54F JUMP JUMPDEST PUSH1 0x40 MLOAD PUSH2 0x1D5 SWAP2 SWAP1 PUSH2 0x7B7 JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH2 0x1F8 PUSH1 0x4 DUP1 CALLDATASIZE SUB DUP2 ADD SWAP1 PUSH2 0x1F3 SWAP2 SWAP1 PUSH2 0x922 JUMP JUMPDEST PUSH2 0x5DD JUMP JUMPDEST STOP JUMPDEST PUSH2 0x202 PUSH2 0x5F0 JUMP JUMPDEST PUSH1 0x40 MLOAD PUSH2 0x20F SWAP2 SWAP1 PUSH2 0x7B7 JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH2 0x220 PUSH2 0x67E JUMP JUMPDEST PUSH1 0x40 MLOAD PUSH2 0x22D SWAP2 SWAP1 PUSH2 0x7B7 JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH2 0x23E PUSH2 0x710 JUMP JUMPDEST STOP JUMPDEST PUSH2 0x25A PUSH1 0x4 DUP1 CALLDATASIZE SUB DUP2 ADD SWAP1 PUSH2 0x255 SWAP2 SWAP1 PUSH2 0x922 JUMP JUMPDEST PUSH2 0x712 JUMP JUMPDEST STOP JUMPDEST PUSH2 0x264 PUSH2 0x725 JUMP JUMPDEST STOP JUMPDEST PUSH1 0x60 PUSH1 0x2 DUP1 SLOAD PUSH2 0x275 SWAP1 PUSH2 0x99A JUMP JUMPDEST DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP1 SLOAD PUSH2 0x2A1 SWAP1 PUSH2 0x99A JUMP JUMPDEST DUP1 ISZERO PUSH2 0x2EE JUMPI DUP1 PUSH1 0x1F LT PUSH2 0x2C3 JUMPI PUSH2 0x100 DUP1 DUP4 SLOAD DIV MUL DUP4 MSTORE SWAP2 PUSH1 0x20 ADD SWAP2 PUSH2 0x2EE JUMP JUMPDEST DUP3 ADD SWAP2 SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 JUMPDEST DUP2 SLOAD DUP2 MSTORE SWAP1 PUSH1 0x1 ADD SWAP1 PUSH1 0x20 ADD DUP1 DUP4 GT PUSH2 0x2D1 JUMPI DUP3 SWAP1 SUB PUSH1 0x1F AND DUP3 ADD SWAP2 JUMPDEST POP POP POP POP POP SWAP1 POP SWAP1 JUMP JUMPDEST PUSH1 0x60 PUSH1 0x1 DUP1 SLOAD PUSH2 0x307 SWAP1 PUSH2 0x99A JUMP JUMPDEST DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP1 SLOAD PUSH2 0x333 SWAP1 PUSH2 0x99A JUMP JUMPDEST DUP1 ISZERO PUSH2 0x380 JUMPI DUP1 PUSH1 0x1F LT PUSH2 0x355 JUMPI PUSH2 0x100 DUP1 DUP4 SLOAD DIV MUL DUP4 MSTORE SWAP2 PUSH1 0x20 ADD SWAP2 PUSH2 0x380 JUMP JUMPDEST DUP3 ADD SWAP2 SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 JUMPDEST DUP2 SLOAD DUP2 MSTORE SWAP1 PUSH1 0x1 ADD SWAP1 PUSH1 0x20 ADD DUP1 DUP4 GT PUSH2 0x363 JUMPI DUP3 SWAP1 SUB PUSH1 0x1F AND DUP3 ADD SWAP2 JUMPDEST POP POP POP POP POP SWAP1 POP SWAP1 JUMP JUMPDEST PUSH1 0x60 PUSH1 0x3 DUP1 SLOAD PUSH2 0x399 SWAP1 PUSH2 0x99A JUMP JUMPDEST DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP1 SLOAD PUSH2 0x3C5 SWAP1 PUSH2 0x99A JUMP JUMPDEST DUP1 ISZERO PUSH2 0x412 JUMPI DUP1 PUSH1 0x1F LT PUSH2 0x3E7 JUMPI PUSH2 0x100 DUP1 DUP4 SLOAD DIV MUL DUP4 MSTORE SWAP2 PUSH1 0x20 ADD SWAP2 PUSH2 0x412 JUMP JUMPDEST DUP3 ADD SWAP2 SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 JUMPDEST DUP2 SLOAD DUP2 MSTORE SWAP1 PUSH1 0x1 ADD SWAP1 PUSH1 0x20 ADD DUP1 DUP4 GT PUSH2 0x3F5 JUMPI DUP3 SWAP1 SUB PUSH1 0x1F AND DUP3 ADD SWAP2 JUMPDEST POP POP POP POP POP SWAP1 POP SWAP1 JUMP JUMPDEST JUMP JUMPDEST PUSH1 0x1 DUP1 SLOAD PUSH2 0x42B SWAP1 PUSH2 0x99A JUMP JUMPDEST DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP1 SLOAD PUSH2 0x457 SWAP1 PUSH2 0x99A JUMP JUMPDEST DUP1 ISZERO PUSH2 0x4A4 JUMPI DUP1 PUSH1 0x1F LT PUSH2 0x479 JUMPI PUSH2 0x100 DUP1 DUP4 SLOAD DIV MUL DUP4 MSTORE SWAP2 PUSH1 0x20 ADD SWAP2 PUSH2 0x4A4 JUMP JUMPDEST DUP3 ADD SWAP2 SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 JUMPDEST DUP2 SLOAD DUP2 MSTORE SWAP1 PUSH1 0x1 ADD SWAP1 PUSH1 0x20 ADD DUP1 DUP4 GT PUSH2 0x487 JUMPI DUP3 SWAP1 SUB PUSH1 0x1F AND DUP3 ADD SWAP2 JUMPDEST POP POP POP POP POP DUP2 JUMP JUMPDEST PUSH1 0x3 DUP1 SLOAD PUSH2 0x4B9 SWAP1 PUSH2 0x99A JUMP JUMPDEST DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP1 SLOAD PUSH2 0x4E5 SWAP1 PUSH2 0x99A JUMP JUMPDEST DUP1 ISZERO PUSH2 0x532 JUMPI DUP1 PUSH1 0x1F LT PUSH2 0x507 JUMPI PUSH2 0x100 DUP1 DUP4 SLOAD DIV MUL DUP4 MSTORE SWAP2 PUSH1 0x20 ADD SWAP2 PUSH2 0x532 JUMP JUMPDEST DUP3 ADD SWAP2 SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 JUMPDEST DUP2 SLOAD DUP2 MSTORE SWAP1 PUSH1 0x1 ADD SWAP1 PUSH1 0x20 ADD DUP1 DUP4 GT PUSH2 0x515 JUMPI DUP3 SWAP1 SUB PUSH1 0x1F AND DUP3 ADD SWAP2 JUMPDEST POP POP POP POP POP DUP2 JUMP JUMPDEST JUMP JUMPDEST DUP1 PUSH1 0x2 SWAP1 DUP2 PUSH2 0x54B SWAP2 SWAP1 PUSH2 0xB81 JUMP JUMPDEST POP POP JUMP JUMPDEST PUSH1 0x2 DUP1 SLOAD PUSH2 0x55C SWAP1 PUSH2 0x99A JUMP JUMPDEST DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP1 SLOAD PUSH2 0x588 SWAP1 PUSH2 0x99A JUMP JUMPDEST DUP1 ISZERO PUSH2 0x5D5 JUMPI DUP1 PUSH1 0x1F LT PUSH2 0x5AA JUMPI PUSH2 0x100 DUP1 DUP4 SLOAD DIV MUL DUP4 MSTORE SWAP2 PUSH1 0x20 ADD SWAP2 PUSH2 0x5D5 JUMP JUMPDEST DUP3 ADD SWAP2 SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 JUMPDEST DUP2 SLOAD DUP2 MSTORE SWAP1 PUSH1 0x1 ADD SWAP1 PUSH1 0x20 ADD DUP1 DUP4 GT PUSH2 0x5B8 JUMPI DUP3 SWAP1 SUB PUSH1 0x1F AND DUP3 ADD SWAP2 JUMPDEST POP POP POP POP POP DUP2 JUMP JUMPDEST DUP1 PUSH1 0x3 SWAP1 DUP2 PUSH2 0x5EC SWAP2 SWAP1 PUSH2 0xB81 JUMP JUMPDEST POP POP JUMP JUMPDEST PUSH1 0x0 DUP1 SLOAD PUSH2 0x5FD SWAP1 PUSH2 0x99A JUMP JUMPDEST DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP1 SLOAD PUSH2 0x629 SWAP1 PUSH2 0x99A JUMP JUMPDEST DUP1 ISZERO PUSH2 0x676 JUMPI DUP1 PUSH1 0x1F LT PUSH2 0x64B JUMPI PUSH2 0x100 DUP1 DUP4 SLOAD DIV MUL DUP4 MSTORE SWAP2 PUSH1 0x20 ADD SWAP2 PUSH2 0x676 JUMP JUMPDEST DUP3 ADD SWAP2 SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 JUMPDEST DUP2 SLOAD DUP2 MSTORE SWAP1 PUSH1 0x1 ADD SWAP1 PUSH1 0x20 ADD DUP1 DUP4 GT PUSH2 0x659 JUMPI DUP3 SWAP1 SUB PUSH1 0x1F AND DUP3 ADD SWAP2 JUMPDEST POP POP POP POP POP DUP2 JUMP JUMPDEST PUSH1 0x60 PUSH1 0x0 DUP1 SLOAD PUSH2 0x68D SWAP1 PUSH2 0x99A JUMP JUMPDEST DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP1 SLOAD PUSH2 0x6B9 SWAP1 PUSH2 0x99A JUMP JUMPDEST DUP1 ISZERO PUSH2 0x706 JUMPI DUP1 PUSH1 0x1F LT PUSH2 0x6DB JUMPI PUSH2 0x100 DUP1 DUP4 SLOAD DIV MUL DUP4 MSTORE SWAP2 PUSH1 0x20 ADD SWAP2 PUSH2 0x706 JUMP JUMPDEST DUP3 ADD SWAP2 SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 JUMPDEST DUP2 SLOAD DUP2 MSTORE SWAP1 PUSH1 0x1 ADD SWAP1 PUSH1 0x20 ADD DUP1 DUP4 GT PUSH2 0x6E9 JUMPI DUP3 SWAP1 SUB PUSH1 0x1F AND DUP3 ADD SWAP2 JUMPDEST POP POP POP POP POP SWAP1 POP SWAP1 JUMP JUMPDEST JUMP JUMPDEST DUP1 PUSH1 0x0 SWAP1 DUP2 PUSH2 0x721 SWAP2 SWAP1 PUSH2 0xB81 JUMP JUMPDEST POP POP JUMP JUMPDEST JUMP JUMPDEST PUSH1 0x0 DUP2 MLOAD SWAP1 POP SWAP2 SWAP1 POP JUMP JUMPDEST PUSH1 0x0 DUP3 DUP3 MSTORE PUSH1 0x20 DUP3 ADD SWAP1 POP SWAP3 SWAP2 POP POP JUMP JUMPDEST PUSH1 0x0 JUMPDEST DUP4 DUP2 LT ISZERO PUSH2 0x761 JUMPI DUP1 DUP3 ADD MLOAD DUP2 DUP5 ADD MSTORE PUSH1 0x20 DUP2 ADD SWAP1 POP PUSH2 0x746 JUMP JUMPDEST PUSH1 0x0 DUP5 DUP5 ADD MSTORE POP POP POP POP JUMP JUMPDEST PUSH1 0x0 PUSH1 0x1F NOT PUSH1 0x1F DUP4 ADD AND SWAP1 POP SWAP2 SWAP1 POP JUMP JUMPDEST PUSH1 0x0 PUSH2 0x789 DUP3 PUSH2 0x727 JUMP JUMPDEST PUSH2 0x793 DUP2 DUP6 PUSH2 0x732 JUMP JUMPDEST SWAP4 POP PUSH2 0x7A3 DUP2 DUP6 PUSH1 0x20 DUP7 ADD PUSH2 0x743 JUMP JUMPDEST PUSH2 0x7AC DUP2 PUSH2 0x76D JUMP JUMPDEST DUP5 ADD SWAP2 POP POP SWAP3 SWAP2 POP POP JUMP JUMPDEST PUSH1 0x0 PUSH1 0x20 DUP3 ADD SWAP1 POP DUP2 DUP2 SUB PUSH1 0x0 DUP4 ADD MSTORE PUSH2 0x7D1 DUP2 DUP5 PUSH2 0x77E JUMP JUMPDEST SWAP1 POP SWAP3 SWAP2 POP POP JUMP JUMPDEST PUSH1 0x0 PUSH1 0x40 MLOAD SWAP1 POP SWAP1 JUMP JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH32 0x4E487B7100000000000000000000000000000000000000000000000000000000 PUSH1 0x0 MSTORE PUSH1 0x41 PUSH1 0x4 MSTORE PUSH1 0x24 PUSH1 0x0 REVERT JUMPDEST PUSH2 0x82F DUP3 PUSH2 0x76D JUMP JUMPDEST DUP2 ADD DUP2 DUP2 LT PUSH8 0xFFFFFFFFFFFFFFFF DUP3 GT OR ISZERO PUSH2 0x84E JUMPI PUSH2 0x84D PUSH2 0x7F7 JUMP JUMPDEST JUMPDEST DUP1 PUSH1 0x40 MSTORE POP POP POP JUMP JUMPDEST PUSH1 0x0 PUSH2 0x861 PUSH2 0x7D9 JUMP JUMPDEST SWAP1 POP PUSH2 0x86D DUP3 DUP3 PUSH2 0x826 JUMP JUMPDEST SWAP2 SWAP1 POP JUMP JUMPDEST PUSH1 0x0 PUSH8 0xFFFFFFFFFFFFFFFF DUP3 GT ISZERO PUSH2 0x88D JUMPI PUSH2 0x88C PUSH2 0x7F7 JUMP JUMPDEST JUMPDEST PUSH2 0x896 DUP3 PUSH2 0x76D JUMP JUMPDEST SWAP1 POP PUSH1 0x20 DUP2 ADD SWAP1 POP SWAP2 SWAP1 POP JUMP JUMPDEST DUP3 DUP2 DUP4 CALLDATACOPY PUSH1 0x0 DUP4 DUP4 ADD MSTORE POP POP POP JUMP JUMPDEST PUSH1 0x0 PUSH2 0x8C5 PUSH2 0x8C0 DUP5 PUSH2 0x872 JUMP JUMPDEST PUSH2 0x857 JUMP JUMPDEST SWAP1 POP DUP3 DUP2 MSTORE PUSH1 0x20 DUP2 ADD DUP5 DUP5 DUP5 ADD GT ISZERO PUSH2 0x8E1 JUMPI PUSH2 0x8E0 PUSH2 0x7F2 JUMP JUMPDEST JUMPDEST PUSH2 0x8EC DUP5 DUP3 DUP6 PUSH2 0x8A3 JUMP JUMPDEST POP SWAP4 SWAP3 POP POP POP JUMP JUMPDEST PUSH1 0x0 DUP3 PUSH1 0x1F DUP4 ADD SLT PUSH2 0x909 JUMPI PUSH2 0x908 PUSH2 0x7ED JUMP JUMPDEST JUMPDEST DUP2 CALLDATALOAD PUSH2 0x919 DUP5 DUP3 PUSH1 0x20 DUP7 ADD PUSH2 0x8B2 JUMP JUMPDEST SWAP2 POP POP SWAP3 SWAP2 POP POP JUMP JUMPDEST PUSH1 0x0 PUSH1 0x20 DUP3 DUP5 SUB SLT ISZERO PUSH2 0x938 JUMPI PUSH2 0x937 PUSH2 0x7E3 JUMP JUMPDEST JUMPDEST PUSH1 0x0 DUP3 ADD CALLDATALOAD PUSH8 0xFFFFFFFFFFFFFFFF DUP2 GT ISZERO PUSH2 0x956 JUMPI PUSH2 0x955 PUSH2 0x7E8 JUMP JUMPDEST JUMPDEST PUSH2 0x962 DUP5 DUP3 DUP6 ADD PUSH2 0x8F4 JUMP JUMPDEST SWAP2 POP POP SWAP3 SWAP2 POP POP JUMP JUMPDEST PUSH32 0x4E487B7100000000000000000000000000000000000000000000000000000000 PUSH1 0x0 MSTORE PUSH1 0x22 PUSH1 0x4 MSTORE PUSH1 0x24 PUSH1 0x0 REVERT JUMPDEST PUSH1 0x0 PUSH1 0x2 DUP3 DIV SWAP1 POP PUSH1 0x1 DUP3 AND DUP1 PUSH2 0x9B2 JUMPI PUSH1 0x7F DUP3 AND SWAP2 POP JUMPDEST PUSH1 0x20 DUP3 LT DUP2 SUB PUSH2 0x9C5 JUMPI PUSH2 0x9C4 PUSH2 0x96B JUMP JUMPDEST JUMPDEST POP SWAP2 SWAP1 POP JUMP JUMPDEST PUSH1 0x0 DUP2 SWAP1 POP DUP2 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 POP SWAP2 SWAP1 POP JUMP JUMPDEST PUSH1 0x0 PUSH1 0x20 PUSH1 0x1F DUP4 ADD DIV SWAP1 POP SWAP2 SWAP1 POP JUMP JUMPDEST PUSH1 0x0 DUP3 DUP3 SHL SWAP1 POP SWAP3 SWAP2 POP POP JUMP JUMPDEST PUSH1 0x0 PUSH1 0x8 DUP4 MUL PUSH2 0xA2D PUSH32 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF DUP3 PUSH2 0x9F0 JUMP JUMPDEST PUSH2 0xA37 DUP7 DUP4 PUSH2 0x9F0 JUMP JUMPDEST SWAP6 POP DUP1 NOT DUP5 AND SWAP4 POP DUP1 DUP7 AND DUP5 OR SWAP3 POP POP POP SWAP4 SWAP3 POP POP POP JUMP JUMPDEST PUSH1 0x0 DUP2 SWAP1 POP SWAP2 SWAP1 POP JUMP JUMPDEST PUSH1 0x0 DUP2 SWAP1 POP SWAP2 SWAP1 POP JUMP JUMPDEST PUSH1 0x0 PUSH2 0xA7E PUSH2 0xA79 PUSH2 0xA74 DUP5 PUSH2 0xA4F JUMP JUMPDEST PUSH2 0xA59 JUMP JUMPDEST PUSH2 0xA4F JUMP JUMPDEST SWAP1 POP SWAP2 SWAP1 POP JUMP JUMPDEST PUSH1 0x0 DUP2 SWAP1 POP SWAP2 SWAP1 POP JUMP JUMPDEST PUSH2 0xA98 DUP4 PUSH2 0xA63 JUMP JUMPDEST PUSH2 0xAAC PUSH2 0xAA4 DUP3 PUSH2 0xA85 JUMP JUMPDEST DUP5 DUP5 SLOAD PUSH2 0x9FD JUMP JUMPDEST DUP3 SSTORE POP POP POP POP JUMP JUMPDEST PUSH1 0x0 SWAP1 JUMP JUMPDEST PUSH2 0xAC1 PUSH2 0xAB4 JUMP JUMPDEST PUSH2 0xACC DUP2 DUP5 DUP5 PUSH2 0xA8F JUMP JUMPDEST POP POP POP JUMP JUMPDEST JUMPDEST DUP2 DUP2 LT ISZERO PUSH2 0xAF0 JUMPI PUSH2 0xAE5 PUSH1 0x0 DUP3 PUSH2 0xAB9 JUMP JUMPDEST PUSH1 0x1 DUP2 ADD SWAP1 POP PUSH2 0xAD2 JUMP JUMPDEST POP POP JUMP JUMPDEST PUSH1 0x1F DUP3 GT ISZERO PUSH2 0xB35 JUMPI PUSH2 0xB06 DUP2 PUSH2 0x9CB JUMP JUMPDEST PUSH2 0xB0F DUP5 PUSH2 0x9E0 JUMP JUMPDEST DUP2 ADD PUSH1 0x20 DUP6 LT ISZERO PUSH2 0xB1E JUMPI DUP2 SWAP1 POP JUMPDEST PUSH2 0xB32 PUSH2 0xB2A DUP6 PUSH2 0x9E0 JUMP JUMPDEST DUP4 ADD DUP3 PUSH2 0xAD1 JUMP JUMPDEST POP POP JUMPDEST POP POP POP JUMP JUMPDEST PUSH1 0x0 DUP3 DUP3 SHR SWAP1 POP SWAP3 SWAP2 POP POP JUMP JUMPDEST PUSH1 0x0 PUSH2 0xB58 PUSH1 0x0 NOT DUP5 PUSH1 0x8 MUL PUSH2 0xB3A JUMP JUMPDEST NOT DUP1 DUP4 AND SWAP2 POP POP SWAP3 SWAP2 POP POP JUMP JUMPDEST PUSH1 0x0 PUSH2 0xB71 DUP4 DUP4 PUSH2 0xB47 JUMP JUMPDEST SWAP2 POP DUP3 PUSH1 0x2 MUL DUP3 OR SWAP1 POP SWAP3 SWAP2 POP POP JUMP JUMPDEST PUSH2 0xB8A DUP3 PUSH2 0x727 JUMP JUMPDEST PUSH8 0xFFFFFFFFFFFFFFFF DUP2 GT ISZERO PUSH2 0xBA3 JUMPI PUSH2 0xBA2 PUSH2 0x7F7 JUMP JUMPDEST JUMPDEST PUSH2 0xBAD DUP3 SLOAD PUSH2 0x99A JUMP JUMPDEST PUSH2 0xBB8 DUP3 DUP3 DUP6 PUSH2 0xAF4 JUMP JUMPDEST PUSH1 0x0 PUSH1 0x20 SWAP1 POP PUSH1 0x1F DUP4 GT PUSH1 0x1 DUP2 EQ PUSH2 0xBEB JUMPI PUSH1 0x0 DUP5 ISZERO PUSH2 0xBD9 JUMPI DUP3 DUP8 ADD MLOAD SWAP1 POP JUMPDEST PUSH2 0xBE3 DUP6 DUP3 PUSH2 0xB65 JUMP JUMPDEST DUP7 SSTORE POP PUSH2 0xC4B JUMP JUMPDEST PUSH1 0x1F NOT DUP5 AND PUSH2 0xBF9 DUP7 PUSH2 0x9CB JUMP JUMPDEST PUSH1 0x0 JUMPDEST DUP3 DUP2 LT ISZERO PUSH2 0xC21 JUMPI DUP5 DUP10 ADD MLOAD DUP3 SSTORE PUSH1 0x1 DUP3 ADD SWAP2 POP PUSH1 0x20 DUP6 ADD SWAP5 POP PUSH1 0x20 DUP2 ADD SWAP1 POP PUSH2 0xBFC JUMP JUMPDEST DUP7 DUP4 LT ISZERO PUSH2 0xC3E JUMPI DUP5 DUP10 ADD MLOAD PUSH2 0xC3A PUSH1 0x1F DUP10 AND DUP3 PUSH2 0xB47 JUMP JUMPDEST DUP4 SSTORE POP JUMPDEST PUSH1 0x1 PUSH1 0x2 DUP9 MUL ADD DUP9 SSTORE POP POP POP JUMPDEST POP POP POP POP POP POP JUMP INVALID LOG2 PUSH5 0x6970667358 0x22 SLT KECCAK256 0x26 DUP9 PUSH15 0xE2D24F23813114D5B29A38961CCDDB PUSH15 0x1C94F7B7D0FFF763C0F63CF5A26473 PUSH16 0x6C634300081300330000000000000000 ",
	"sourceMap": "74:1078:0:-:0;;;;;;;;;;;;;;;;;;;"
}

ganach_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganach_url))
# web3 = Web3(Web3.EthereumTesterProvider)
web3.eth.defaultAccount = web3.eth.accounts[0]
#address = web3.toChecksumAddress("0xd9145CCE52D386f254917e481eB44e9943F39138")
contract = web3.eth.contract(address="0xd9145CCE52D386f254917e481eB44e9943F39138", abi=abi_signature)
# contract = web3.eth.contract(abi = abi, bytecode = bytecode )
# print(web3.eth.get_block('latest'))




# print(msg_hash)
# print(type(msg_hash))

# web3.utils.padLeft(web3.utils.hexToBytes(msg_hash), 32)
# msg_hashbytes = HexBytes(msg_hash)
# print(msg_hash.hex())


signer_account = web3.eth.accounts[0]
signer_private = '0x6727e3c0a0187676c78ff449e9ce460ae1b3479b10e71e59a94414865c8033bc'
nonce = web3.eth.getTransactionCount(signer_account)
tx = {
    'nonce': nonce+1,
    'to': web3.eth.accounts[1],
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}
msg_hash = contract.functions.getMessageHash(web3.eth.accounts[1],web3.toWei(1,'ether'),"first transaction",nonce).transact()

# #
#sign the transaction
signed_tx = web3.eth.account.sign_transaction(tx, signer_private )

#send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

#get transaction hash
# print(web3.toHex(tx_hash))


# verifyer_acc = web3.eth.accounts[1]
# print(web3.eth.accounts[0].verify(signed_tx, msg_hash))




from ecdsa import SigningKey
private_key = SigningKey.generate() # uses NIST192p
signature = private_key.sign(b"Educative authorizes this shot")
# print(signature)
public_key = private_key.verifying_key
print(type(private_key))
print(type(public_key))

print("Verified:", public_key.verify(signature, b"Educative authorizes this shot"))



def settime():
        now="prateek"
    #  print(now)
        tx_hash = contract.functions.setTimeStamp(now).transact()
        return tx_hash


def gettime():
    time = contract.functions.getTimeStamp().call()
    # time = contract.caller().getTimeStamp()
    return time












# hash = settime()
# time = gettime()

# tx_receipt = web3.eth.wait_for_transaction_receipt(hash)
# print(tx_receipt.contractAddress)
# time = gettime()
#print(hash)
# print(time)






