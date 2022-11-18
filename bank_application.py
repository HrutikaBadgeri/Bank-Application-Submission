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


@app.command(name = "CREATE")
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

@app.command(name="DEPOSIT")
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

@app.command(name="WITHDRAW")
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

@app.command(name="BALANCE")
def balance(code):
    if code in data:
        print(str(data[code]["name"]) + " " + str(data[code]["balance"]))
    else:
        print('Sorry, the account with this code does not exist!')


if __name__ == "__main__":
    app()

