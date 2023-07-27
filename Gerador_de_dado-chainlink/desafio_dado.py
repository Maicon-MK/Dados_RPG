from web3 import Web3

# Conecte-se à rede Ethereum usando a biblioteca web3.py
w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/your-infura-project-id'))  # Substitua pela URL do nó da rede Ethereum que você está usando

# Endereço do contrato inteligente VRFD20
contract_address = "0xf0b5fdd3683eae12554942133301dd1285dbfc10"  # Substitua pelo endereço real do contrato

# Converta o endereço para o formato checksum
contract_address_checksum = w3.to_checksum_address(contract_address)

# Abra um contrato com o ABI do contrato inteligente
abi = [
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "vrfCoordinator",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "linkToken",
				"type": "address"
			},
			{
				"internalType": "bytes32",
				"name": "keyHash",
				"type": "bytes32"
			},
			{
				"internalType": "uint256",
				"name": "fee",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "subscriptionId",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "bytes32",
				"name": "requestId",
				"type": "bytes32"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "roller",
				"type": "address"
			}
		],
		"name": "DiceRolled",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "getDiceResult",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "requestId",
				"type": "bytes32"
			},
			{
				"internalType": "uint256",
				"name": "randomness",
				"type": "uint256"
			}
		],
		"name": "rawFulfillRandomness",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "rollDice",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "requestId",
				"type": "bytes32"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]  # Substitua pelo ABI real do contrato
contract = w3.eth.contract(address=contract_address_checksum, abi=abi)

# Chave da API do Chainlink
chainlink_api_key = "0x474e34a077df58807dbe9c96d3c009b23b3c6d0cce433e59bbf5b34f823bc56c"  # Substitua pela chave da API do Chainlink real

# Taxa de LINK necessária para fazer a solicitação de número aleatório
fee = 0  # Substitua pelo valor real em Wei

# Faça a transação para a função rollDice do contrato
transaction = contract.functions.rollDice().transact({'from': '0x0F1589E46Fd376385A0DfDd8B0843f6C8Ab0EE3f', 'value': fee, 'gas': 200000})

# Aguarde a mineração da transação
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction)

# Obtenha o resultado do número aleatório após a mineração
random_result = contract.functions.getDiceResult().call({'from': '0x0F1589E46Fd376385A0DfDd8B0843f6C8Ab0EE3f'})
print(f"Resultado do dado: {random_result}")
