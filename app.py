from iroha import Iroha, IrohaCrypto, IrohaGrpc

net = IrohaGrpc('localhost:50051')
account_ids = ['root@sorakh', 'alice@sorakh', 'bob@sorakh']

def get_asset(acct_id, priv_key):
  iroha = Iroha(acct_id)
  get_asset_query = iroha.query(
    'GetAccountAssets',
    account_id= acct_id
  )
  try:
    IrohaCrypto.sign_query(get_asset_query, priv_key)
    response = net.send_query(get_asset_query)
    print(response)
  except:
    print("invalid transaction")  

def transfer_asset(creator_acct_id, creator_priv_key, src_acct_id, dest_acct_id, asset_id, amount): 
  iroha = Iroha(creator_acct_id)
  trx = iroha.transaction(
      [iroha.command(
          'TransferAsset', 
          src_account_id= src_acct_id, 
          dest_account_id= dest_acct_id,
          asset_id= asset_id,
          description='test',
          amount= amount
      )]
  )
  try:
    IrohaCrypto.sign_transaction(trx, creator_priv_key)
    response = net.send_tx(trx)
    print('transaction is committed')
  except:
    print("invalid transaction")

def validate_input(msg):
  input_value = input('Please input your '+msg+': ')
  while input_value is '':
    print('[Validation] ---> '+msg+' required')
    input_value = input('Please input your '+msg+': ')
  return input_value

def print_command():
  print("""
  Please Input Command Number

    1. Query Transaction
    2. Sending Asset
  """)

def command(account_id):
  while True:
    print_command()
    command_num = validate_input('command >')
    if command_num is '1':
      priv_key = input('priv key: ')
      get_asset(account_id, priv_key)
    elif command_num is '2':
      src_account_id = input('src account id: ')
      des_account_id = input('des account id: ')
      asset_id = input('asset id: ')
      amount = input('amount: ')
      priv_key = input('priv key: ')
      transfer_asset(account_id, priv_key, src_account_id, des_account_id, asset_id, amount)
    else:
      print('Not valid command number')

def init():
  account_id = validate_input('account id')
  if account_id not in account_ids:
    exit("[error] ----> : invalid account id")
  command(account_id)

init()


