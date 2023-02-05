
NEW_LOGIN="INSERT INTO client VALUES(%s,%s,%s,%s,%s,%s,%s)"

NEW_LOGIN_ACCOUNT="INSERT INTO client_account_info(client_id,balance_money,balance_bitcoin) VALUES(%s,%s,%s)"

CHECK_ID="SELECT client_id FROM client"


CHECK__ACC="SELECT account_no FROM client"

CHECK__PASS="SELECT passw FROM client WHERE account_no=%s"


FETCH_CLIENT_DETAILS="SELECT * FROM client WHERE account_no=%s"



CLIENT_HOME="""OUR SERVICES

1)Check Your Balance

2)Check Your BitCoin Balance

3)Transfer Money

4)Change Password

5)EXIT"""

GET_CLIENT_ID="SELECT client_id FROM client WHERE account_no=%s"


PRINT_CURRENT_BALANCE="SELECT balance_money FROM client_account_info WHERE client_id=%s"

PRINT_CURRENT_BITCOIN_BALANCE="SELECT balance_bitcoin FROM client_account_info WHERE client_id=%s"

TRANSFER_MONEY="UPDATE client_account_infO SET balance_money=%s WHERE client_id=%s;"


GET_CLIENT_EMAIL="SELECT email FROM client WHERE client_id=%s"



GET_CLIENT_PASSWORD="UPDATE client SET  passw=%s  WHERE client_id=%s"

SUB_TRANSFER="""
------------------------------------\n\n
 1) Transfer Money\n
 2) Transfer Bitcoin\n\n\n"""

GET_BITCOIN_BALANCE="SELECT balance_bitcoin FROM client_account_info WHERE client_id=%s"


TRANSFER_BITCOIN="UPDATE client_account_infO SET balance_bitcoin=%s WHERE client_id=%s;"



#MANAGER FUNCTIONS!#
#MANAGER FUNCTIONS!#
#MANAGER FUNCTIONS!#
#MANAGER FUNCTIONS!#

CHECK_ID_MANAGER="SELECT manager_id FROM manager WHERE username=%s"
CHECK__PASS_MANAGER="SELECT manager_pass FROM manager WHERE manager_id=%s"

I="LORD PLEASE ENTER YOUR USERNAME: "
J="LORD PLEASE ENTER YOUR PASSWORD: "

LORD_MENU="""
1)Deposit Money
2)Detail correction
"""

GET_MANAGER_TRANS_PASS=""

