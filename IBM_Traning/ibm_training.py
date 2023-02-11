# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 14:28:44 2022

@author: k Sai Shashank
"""

import requests
import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "T09HVN4NjF3RrHSRWywQgxiqQ71MzKXYE3e72cZT0AHl"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["X1 transaction date","X2 house age","X3 distance to the nearest MRT station","X4 number of convenience stores","X5 latitude","X6 longitude"]], 
                                   "values": [[2012.09789,15.7,34.78866,4,123.67897,124.89768]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/65d18cac-b868-4cbb-875e-cfea26a46eea/predictions?version=2022-07-14', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions = response_scoring.json()
print(predictions['predictions'][0]['values'][0][0])