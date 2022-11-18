import json
import typer
import re 

app = typer.Typer()

# read and write data into json
try:
    with open('data.json') as f:
        data = json.load(f)
except:
    print('There seems to be some issue in loading the data.json')


def writeToJSONFile(path, fileName, data):
    try:
        filePathNameWExt = './' + path + '/' + fileName + '.json'
        with open(filePathNameWExt, 'w') as fp:
            json.dump(data, fp)
    except:
        print('There are some problems with the bank data.json')


@app.command(name = "CREATE",help="Use the HELP command for any queries.")
def create(code, account_name):
    if code in data:
        print('Please select a unique account code for your account.')
    else: 
        x = re.search("^ACC(?:[0-9][0-9][0-9])$", code)
        if(x):
            data[code] = {"name": account_name, "balance": 0}
            writeToJSONFile("./", "data", data)
            print('Account Created.')
        else:
            print('Please enter the account code in the format ACCXXX.')

@app.command(name="DEPOSIT",help="Use the HELP command for any queries.")
def deposit(code, amount):
    if code in data:
        try:
            amt = int(amount)
            if(amt < 1):
                print('Please enter amount greater than 0.')
            else:
                balance = data[code]["balance"]
                data[code]["balance"] = balance + amt
                writeToJSONFile("./", "data", data)
                print('Amount Deposited.')
        except:
            print('Letters detected, please check your amount value.')
    else: 
        print('Sorry, the account with this code does not exist!')

@app.command(name="WITHDRAW",help="Use the HELP command for any queries.")
def withdraw(code, amount):
    if code in data:
        try:
            amt = int(amount)
            bal = data[code]["balance"]
            if(bal < amt):
                print('Sorry, your balance is not sufficient for this withdrawal transaction.')
            elif(amt < 1):
                print('Please enter amount greater than 0.')
            else:
                balance = data[code]["balance"]
                data[code]["balance"] = balance - amt
                writeToJSONFile("./", "data", data)
                print('Amount Withdrawn.')
        except:
            print('Letters detected, please check your amount value.')
    else:
        print('Sorry, the account with this code does not exist!')

@app.command(name="BALANCE",help="Use the HELP command for any queries.")
def balance(code):
    if code in data:
        print(str(data[code]["name"]) + " " + str(data[code]["balance"]))
    else:
        print('Sorry, the account with this code does not exist!')

@app.command(name="HELP")
def help():
    create_help = '''
    - This command will create a new account with the given account code and the account name.\n
    - The bank balance associated with the new account will initially be 0.\n
    - Usage: python bank_application.py CREATE <ACCOUNT_CODE> <ACCOUNT_NAME>\n
    - Note: The account name must be in the format ACCXXX.
    '''
    deposit_help = '''
    - This command will deposit the amount in your existing account\n
    - Usage: python bank_application.py DEPOSIT <ACCOUNT_CODE> <AMOUNT>\n
    - Note: The account name must be in the format ACCXXX and the account must already exist in the bank. 
    '''
    withdraw_help = '''
    - This command will withdraw the amount from your existing account\n
    - Usage: python bank_application.py WITHDRAW <ACCOUNT_CODE> <AMOUNT>\n
    - Note: The account name must be in the format ACCXXX and the account must already exist in the bank. 
    '''
    balance_help = '''
    - This command will return the balance of your account\n
    - Usage: python bank_application.py BALANCE <ACCOUNT_CODE>\n
    - Note: The account name must be in the format ACCXXX and the account must already exist in the bank. 
    '''
    print("CREATE COMMAND\n",create_help)
    print("DEPOSIT COMMAND\n",deposit_help)
    print("WITHDRAW COMMAND\n",withdraw_help)
    print("BALANCE COMMAND\n",balance_help)

if __name__ == "__main__":
    app()

