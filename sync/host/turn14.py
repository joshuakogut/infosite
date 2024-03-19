import sys
import requests
import json
import logging
import time

from portal.settings import T14_ID, T14_SECRET

logging.captureWarnings(True)


class Turn14Error(Exception):
    pass


token_url = "https://apitest.turn14.com/v1/token"
inv_url = "https://apitest.turn14.com/v1/inventory"


def get_new_token():

    token_req_payload = {"grant_type": "client_credentials"}

    token_response = requests.post(
        token_url,
        data=token_req_payload,
        verify=False,
        allow_redirects=False,
        auth=(T14_ID, T14_SECRET),
    )

    if token_response.status_code != 200:
        print("Failed to obtain token from the OAuth 2.0 server", file=sys.stderr)
        sys.exit(1)

    print("Successfuly obtained a new token")
    tokens = json.loads(token_response.text)
    return tokens["access_token"]


def get_product_info(sku):
    pass


if __name__ == "__main__":
    token = get_new_token()
    print("token: %s" % token)

    testsku = "turTS-0401-1101"
    testsku = "04011101"
    query = inv_url + "/" + testsku
    api_call_headers = {"Authorization": "Bearer " + token}
    api_call_response = requests.get(query, headers=api_call_headers, verify=False)

    print(api_call_response.text)
