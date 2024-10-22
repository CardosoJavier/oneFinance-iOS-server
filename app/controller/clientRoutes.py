import logging
from flask import Blueprint, request
from app.service.tellerService import TellerService

tellerRoutes = Blueprint('tellerRoutes', __name__)

tellerService: TellerService = TellerService()

# Fetch accounts
@tellerRoutes.route('/api/accounts', methods=['GET'])
def fetchAccounts():
    return tellerService.fetchAccounts()

# Fetch balances
@tellerRoutes.route('/api/balances', methods=['GET'])
def fetchAccountBalances():
    account_id = request.args.get("account_id")

    if account_id:
        return tellerService.fetchAccountBalance(account_id)
    else:
        logging.error("user id missing in request")
        return {"error": "user id missing in request"}
        

# Fetch access token
@tellerRoutes.route('/api/storeAccessToken', methods=['POST'])
def storeAccessToken():
    requestData = request.json
    
    if requestData.get("access_token"):
        tellerService.storeAccessToken(requestData.get("access_token"))
        logging.info("Token saved succesfully")
        return {"status": "success getting token"}
    
    else:
        logging.error("Token was not in request")
        return {"status": "failed getting token"}

@tellerRoutes.route("/healthz")
def healthz():
    return {'health': "healthy"}