from flask import Flask, render_template, request, redirect, g, url_for
from flask_bootstrap import Bootstrap
from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider
import pprint

url = "https://ropsten.infura.io/v3/8db3e633846f4c7e8d02c53a00253acc"
w3 =  Web3(HTTPProvider(url))

print(f"connection : {w3.isConnected()}")

app = Flask(__name__)
bootstrap = Bootstrap(app)

contract_address = w3.toChecksumAddress("0xEb15CAB674809874E1982EC7919D38747Cc1d22e")
contract_abi = [
                {
                    "inputs": [
                        {
                            "internalType": "string",
                            "name": "firstName",
                            "type": "string"
                        },
                        {
                            "internalType": "string",
                            "name": "lastName",
                            "type": "string"
                        },
                        {
                            "internalType": "string",
                            "name": "contactNumber",
                            "type": "string"
                        },
                        {
                            "internalType": "string",
                            "name": "mailID",
                            "type": "string"
                        },
                        {
                            "internalType": "string",
                            "name": "dateOfBirth",
                            "type": "string"
                        },
                        {
                            "internalType": "string",
                            "name": "residentAddress",
                            "type": "string"
                        }
                    ],
                    "name": "addAccount",
                    "outputs": [],
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "inputs": [
                        {
                            "internalType": "string",
                            "name": "enterSkill",
                            "type": "string"
                        }
                    ],
                    "name": "addSkill",
                    "outputs": [],
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "changeStatus",
                    "outputs": [],
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "stateMutability": "nonpayable",
                    "type": "constructor"
                },
                {
                    "inputs": [],
                    "name": "numberOfRegistrations",
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
                            "internalType": "address",
                            "name": "",
                            "type": "address"
                        }
                    ],
                    "name": "numberOfSkills",
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
                    "inputs": [],
                    "name": "owner",
                    "outputs": [
                        {
                            "internalType": "address",
                            "name": "",
                            "type": "address"
                        }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [
                        {
                            "internalType": "address",
                            "name": "",
                            "type": "address"
                        },
                        {
                            "internalType": "uint256",
                            "name": "",
                            "type": "uint256"
                        }
                    ],
                    "name": "skills",
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
                    "name": "status",
                    "outputs": [
                        {
                            "internalType": "bool",
                            "name": "",
                            "type": "bool"
                        }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [
                        {
                            "internalType": "address",
                            "name": "",
                            "type": "address"
                        }
                    ],
                    "name": "userDataExists",
                    "outputs": [
                        {
                            "internalType": "bool",
                            "name": "",
                            "type": "bool"
                        }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [
                        {
                            "internalType": "address",
                            "name": "",
                            "type": "address"
                        }
                    ],
                    "name": "userDataIndex",
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
                            "internalType": "uint256",
                            "name": "",
                            "type": "uint256"
                        }
                    ],
                    "name": "userDataList",
                    "outputs": [
                        {
                            "internalType": "address",
                            "name": "user_address",
                            "type": "address"
                        },
                        {
                            "internalType": "string",
                            "name": "first_name",
                            "type": "string"
                        },
                        {
                            "internalType": "string",
                            "name": "last_name",
                            "type": "string"
                        },
                        {
                            "internalType": "string",
                            "name": "contact_number",
                            "type": "string"
                        },
                        {
                            "internalType": "string",
                            "name": "mail_id",
                            "type": "string"
                        },
                        {
                            "internalType": "string",
                            "name": "DOB",
                            "type": "string"
                        },
                        {
                            "internalType": "string",
                            "name": "resident_address",
                            "type": "string"
                        },
                        {
                            "internalType": "uint256",
                            "name": "registeration_date",
                            "type": "uint256"
                        }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                }
            ]

contract = w3.eth.contract(address = contract_address, abi = contract_abi)

print(contract.all_functions())
print("Owner Account : "+contract.functions.owner().call())

owner_pub_key = "0xbAE6e58D470195BeE55b22872d76B342d0e6BF25"
owner_pri_key = "C59C333E99DDEDB9C8E46653B9A8D606A110074678DB2C8206B08A29E0F39944"

'''numOfRegisteredUsers = contract.functions.numberOfRegistrations().call()
print(f"\nNo. of registered users : {numOfRegisteredUsers}")

userDataList = []
for i in range(numOfRegisteredUsers):
    userDataList.append(contract.functions.userDataList(i).call())

print("\nUser Data List.... :")
print(userDataList)
'''

@app.route("/")
def homePage():

    return redirect(url_for("home_page"))


@app.route("/homePage")
def home_page():
#options to log in
#button to see userData page 

    return render_template("homePage.html")

@app.route("/addDataForm",  methods=["GET", "POST"])
def add_data_form():#get and post methods to get the login details

    return render_template("addDataForm.html")

@app.route("/transact", methods=["GET", "POST"])
def transact():
    publicKey = request.form["publicKey"]
    privateKey = request.form["privateKey"]
    print(privateKey)
    firstName = request.form["firstName"]
    lastName = request.form["lastName"]
    contactNumber = request.form["contactNumber"]
    mailId = request.form["mailID"]
    DOB = request.form["DOB"]
    residentAddress = request.form["residentAddress"]
    skillSetString = request.form["skillString"]

    print("skill set entered  : ")
    print(skillSetString)

    transaction = contract.functions.addAccount(firstName, lastName, contactNumber, mailId, DOB, residentAddress).buildTransaction({
        'gas': 1000000,
        'gasPrice': Web3.toWei('1', 'gwei'),
        'from': publicKey,
        'nonce': w3.eth.getTransactionCount(publicKey)
    })

    ###############################EXECUTED################################
    signed_txn = w3.eth.account.signTransaction(transaction, private_key=privateKey)
    tx = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    #############################################################
    tx_hash = w3.toHex(tx)
    print("tx_hash = "+tx_hash)
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    print("\n\nTransaction receipt mined:")
    pprint.pprint(dict(receipt))
    print("\n\nWas transaction successful?")
    status = receipt['status']
    pprint.pprint(status)



    #############################################################################
    transaction_hashes = []
    transaction_hashes.append(tx_hash)

    #############################################################################

    print("########################## Now Transacting the skill sets ###################################")

    skillList = skillSetString.split('$')

    for skill in skillList:

        transaction = contract.functions.addSkill(skill).buildTransaction({
            'gas': 1000000,
            'gasPrice': Web3.toWei('1', 'gwei'),
            'from': publicKey,
            'nonce': w3.eth.getTransactionCount(publicKey)
        })

        ###############################EXECUTED################################
        signed_txn = w3.eth.account.signTransaction(transaction, private_key=privateKey)
        tx = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        #############################################################
        tx_hash = w3.toHex(tx)
        print("tx_hash = "+tx_hash)
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        print("\n\nTransaction receipt mined:")
        pprint.pprint(dict(receipt))
        print("\n\nWas transaction successful?")
        status = receipt['status']
        pprint.pprint(status)

        transaction_hashes.append(tx_hash)



    balance_remaining = w3.eth.getBalance(publicKey)
    #return redirect(url_for("home_page"))
    return render_template("personalData.html", publicKey = publicKey, firstName = firstName, lastName = lastName, contactNumber = contactNumber, mailId = mailId, DOB = DOB, residentAddress = residentAddress, status = (status), txn_hashes = transaction_hashes, balance_remaining = balance_remaining, skillList = skillList)


@app.route("/userData")
def userData():
    numOfRegisteredUsers = contract.functions.numberOfRegistrations().call()
    print(f"\nNo. of registered users : {numOfRegisteredUsers}")

    userDataList = []
    for i in range(numOfRegisteredUsers):
        userData = contract.functions.userDataList(i).call()
        userAddress = userData[0]
        
        numOfskills = contract.functions.numberOfSkills(userAddress).call()
        userSkills = []
        for j in range(numOfskills):
            userSkills.append(contract.functions.skills(userAddress,j).call())

        userData.append(userSkills)
        userDataList.append(userData)
        

    print("\nUser Data List.... :")
    print(userDataList)
    #require number of users
    #then we'll fetch the details of each user

    return render_template("userData.html", numOfRegisteredUsers = numOfRegisteredUsers, userDataList  = userDataList)#we'll pass the user list along with it...