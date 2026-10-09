#!/usr/bin/env python3
import os
import django
import sys
import requests
import json
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()
from portal.dev_settings import T14_ID, T14_SECRET
from portal.models import WaitingdropshipTurn14 as Turn14Orders


order_api = "https://apitest.turn14.com/v1/orders/po/"  # + po_number


##
##    function to obtain a new OAuth 2.0 token from the authentication server
##
def get_new_token():

    auth_server_url = "https://apitest.turn14.com/v1/token"
    client_id = T14_ID
    client_secret = T14_SECRET
    token_req_payload = {"grant_type": "client_credentials"}

    token_response = requests.post(
        auth_server_url,
        data=token_req_payload,
        verify=False,
        allow_redirects=False,
        auth=(client_id, client_secret),
    )

    if token_response.status_code != 200:
        print("Failed to obtain token from the OAuth 2.0 server", file=sys.stderr)
        sys.exit(1)

    print("Successfuly obtained a new token")
    tokens = json.loads(token_response.text)
    return tokens["access_token"]


def request_order(po_no, token=None):
    if not token:
        token = get_new_token()

    api_call_headers = {"Authorization": "Bearer " + token}
    api_call_response = requests.get(
        order_api + po_no, headers=api_call_headers, verify=False
    )

    ##
    ##
    if api_call_response.status_code == 401:
        print("token error")
        token = get_new_token()
        raise Exception("fukc you")
    else:
        print("-- response --")
        obj = json.loads(api_call_response.text)
        return obj
        """print(
            json.dumps( obj, indent=2)
        )"""


"""

    token = get_new_token()
    for order in Turn14Orders.objects.all():
        data = request_order( order.ponumber, token )
        print( "Order %s, tracking info\n\t::\t%s" % (order.ordernumber, data['data'][0]['attributes']['tracking']) )

"""
if __name__ == "__main__":
    pass
