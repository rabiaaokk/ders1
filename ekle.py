import requests

reqUrl = "http://127.0.0.1:6767/users?name=rabia&age=23&city=erzurum"

headersList = {
         "Accept": "*/*",
          "User-Agent": "Thunder Client (https://www.thunderclient.com)"
          }

payload = ""

response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

print(response.text)
                   