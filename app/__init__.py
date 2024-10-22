import os
import logging
import argparse
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from app.controller.clientRoutes import tellerRoutes
from app.controller.healthRoutes import healthRoutes
load_dotenv()

def _parse_args():
    parse = argparse.ArgumentParser(description="Teller environment config")

    # add arguments
    parse.add_argument('--environment', default='sandbox', choices=['sandbox', 'dev', 'prod'], help="Entern environment")
    parse.add_argument('--cert', type=str, help="mTLS Certificate path")
    parse.add_argument('--key', type=str, help="mTLS private key")

    args = parse.parse_args()

    # check if cert and key are needed
    need_cert = args.environment in ['dev', 'prod']
    has_cer = args.cert and args.key

    if need_cert and not has_cer:
        parse.error("--cert and --key are requiered when --environment is not sandbox")

    return args

def create_app():

    # get args from command line
    #args = _parse_args()
    #cert = (args.cert, args.key)

    # app instance
    app = Flask(__name__)

    # CORS configuration. Origins will be modified later on
    CORS(app, origins='*')

    # loggin settings
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # routes
    app.register_blueprint(tellerRoutes)
    app.register_blueprint(healthRoutes)

    # Set up app environment
    logging.info("starting oneFinance server...")
    
    return app