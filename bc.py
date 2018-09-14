genesis_block = {
        'previous_hash': 'XZY',
        'index': 0,
        'transactions': []
        }

blockchain = [genesis_block]
open_transaction = []
owner = 'Mennu'



def get_last_blockchain_value():
    if len(blockchain) < 1:
        return [1]
    return blockchain[-1]

def add_transaction(recipient, sender=owner, amount = 1.00):
    ''' Adds a transaction to the blockchain 

        Arguments:
            Sender: Person who is sending the coins
            Recipient: The Recipients of coins
            Amount: The amount of coins sent with the transaction(default: 1.00)
    '''
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transaction.append(transaction)

def mine_block():
    last_block = blockchain[-1]
    hashed_block = ''

    for key in last_block:
         value = last_block[key]
         hashed_block += str(value)

    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transaction
        }
    
    blockchain.append(block)


def get_user_choice():
    ''' Prompts the user for input '''
    return input('Enter your choice: ')
    
def get_transaction_data():
    ''' Prompts User for transaction amount '''
    tx_recipient = input('Enter Recipients Name: ')
    tx_amount = float(input('Enter transaction amount: '))
    return (tx_recipient, tx_amount)

def print_blockchain():
    for block in blockchain:
        print(block)

def update_blockchain():
    if len(blockchain) > 0:
        blockchain[0] = [2]

def verify_blockchain():
    blockchain_index = 0
    is_valid = True
    for blockchain_index in range(len(blockchain)):
        if blockchain_index == 0:
            continue
        if blockchain[blockchain_index] != blockchain[blockchain_index-1]:
            is_valid = False
            break
    return is_valid

terminate_flag = True

while terminate_flag:
    print('Please Choose')
    print('1. Add a new transaction value')
    print('2. Mine a block')
    print('3. Output the blockchain')
    print('4. Update the blockchain')
    print('5. Verify Blockchain')

    user_choice = get_user_choice()
    if user_choice is '1':
        tx_data = get_transaction_data()
        recipient, amount = tx_data
        add_transaction(recipient=recipient, amount=amount)
    elif user_choice is '2':
        mine_block()
    elif user_choice is '3':
        print_blockchain()
    elif user_choice is '4':
        update_blockchain()
    elif user_choice is '5':
        if verify_blockchain():
            print('Blockchain is valid!')
        else:
            print('Red Alert - Blockchain is no more valid!!!')
    elif user_choice is 'q':
        terminate_flag = False
        break
    else:
        print('Invalid Input')
