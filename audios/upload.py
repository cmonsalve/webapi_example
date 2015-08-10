import sys
import os
import base64
import hmac
import hashlib
import urllib
import time
import requests

access_key = "0780b60d5696d6e2"
access_secret = "8e5c66ff23918fe6c70b92d580fa38e7"

requrl = "https://api.acrcloud.com/v1/audios"
http_method = "POST"
http_uri = "/v1/audios"
signature_version = "1"
timestamp = time.time()

string_to_sign = http_method+"\n"+http_uri+"\n"+access_key+"\n"+signature_version+"\n"+str(timestamp)

sign = base64.b64encode(
        hmac.new(access_secret, string_to_sign, digestmod=hashlib.sha1)
        .digest())

f = open(sys.argv[1], "r")

files = {'audio_file':f}
headers = {'access-key': access_key, 'signature-version': signature_version, 'signature': sign, 'timestamp':timestamp}
data = {'title':"api_test", "audio_id":1234, "bucket_name":"test", "data_type":"audio", "custom_key[0]":"key1", "custom_value[0]":"key2"}

r = requests.post(requrl, files=files, data=data, headers=headers, verify=True)
r.encoding = "utf-8"
print r.text
