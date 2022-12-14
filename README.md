<div>
<h1 align="center">Bank Application</h1>
</div>

➔ A Command Line Bank Application that can execute operations where the user can create an account, deposit amount into the account, withdraw amount from the account and check the account balance.

### ➔ Assumptions

1. It is assumed that the user has python (version 3 or higher) installed in his/her device.
2. It is assumed that the user enters the operation commands in all uppercase.
3. It is assumed that the user knows that the user must enter the account code in the format ACCXXX.

### ➔ How to Put Commands

```
SAMPLE: python bank_application.py <COMMAND> <ACCOUNT_CODE> <ACCOUNT_NAME>

Example Commands:
python bank_application.py CREATE ACC001 ABC
python bank_application.py WITHDRAW ACC001 1000
python bank_application.py DEPOSIT ACC001 1000
python bank_application.py BALANCE ACC001
```

### ➔ Technical Details

- **Language:** `Python3`
- **Imports:** `Typer, JSON, Regex`

### ➔ Project setup

`Fork` the repository, this will make a copy of this project in your account.

1. Clone the repository by running below command -

```
git clone https://github.com/<username>/Bank-Application-Submission.git
```

2. Open the folder by running below command -

```
cd Bank-Application-Submission
```

3.  Install all the requirements by running below command -

```
pip install -r requirements.txt
```

This will install all the required libraries to run this project.

4. Run bank_application.py using below command to start

```
python bank_application.py <command>
```
