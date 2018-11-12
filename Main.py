import speech_recognition as sr

# aktiveerib mikrofoni ja kuulab kuni on vaikus
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
print("Stopped listening.")


credentials = r"""{
  "type": "service_account",
  "project_id": "omega-jet-222316",
  "private_key_id": "1fad3e579f56f867bcbd2af1e36b2a4d66c3e5c9",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDp+PboYSHKqvIs\nlkDJZ2CbvNvCme1/QuevkmP52twx7ngvLzc1m7sc+yZ52swxWrypMJFDeE2Ij693\n+VH59E6kkpMx5bqWq7LNOivb7yHp3vjqM0Jvgdi//yDT7e4HXXpqS3AY4UMQZStN\nTIHynstkJYtui5M8/4a1j9QcVPjX1We0ElPUrdv5WoJXT4nLgv7nDk7b6BX1/fgy\n6bea26ZfKTi/w6mNTIv3M6bFDWurMZVVJkAuHjFgiFelvzIerrma6pgmEPF8Movy\nTRMVbbq/7iHM8ErkZ0pAx6bIox9SC04uDNIXMNgPkCNp925dv2Q2OyFVsWiKl34/\nULbomnFVAgMBAAECggEAGaJACZFME/nATaKVQjD0HyvvrHWT1SEIjtj24MgZ3tNA\nfJ7rfrvrTKS21ZvjSjb65ih0NH7+M6DWZHUUMP0+Dn7L51LC1hYaoVcnDfy4QPi/\nrwe4VszUPqNzk8naDcQv5hcSFs+7Or/IIOW/HkydKQGKB1hTDy2fCHj+ZVo+kdrR\n0a0IisfgwZIfNgs9d4HxZ6/WgS7mV0TXJ71ZeATx4SVAh0jy13a+KfYr0BwCpXYz\np6JMcQ1Jfd8ssEcMqlTcJa8oaB6bKFnPMwXhfDDpjCO3lFsxxwrHGuNvoYqeyd2Q\naA23hf01tuDm22cBDlPuuJaJWGjCtIjSCkM2T3sqwwKBgQD6+ENzP3vmZEzBHDU5\ngVn5Ia7g2ntmvO435hGMRzgyBQ7wuEDXeEENkE2mZF0f7G+6yPPUIM/G3qPCjXOo\nsIIUPZZxg7QUYKm025U3e7cO2JUpM01ikOOXx5SfjcPX5rB4SFp96/c4I39cTmjb\n18SAaZRp8oCscU3GompJTBdLSwKBgQDuqXzCRZbN/xqxaZpdH0WgPH7Hxmo/TLlb\n3dkeV27JHZZr7Oh+pkoV2I6A1xDCid7LYgCcbvvJcRgTgEhdnbrMXL3Ov+tVDGIC\n7lfoRFCG3pXJ4pkUhD7HdKhvdu2NcBukNB5c5xIPQPoO04R6Vpi6Mlmx2GFqeIk8\n2qAobiOx3wKBgAGtYxYEGJnjlbe8roZh3O4TUY3jJ+v520W4XemoGDINYpotQRGv\nlg+3JS21ggHSnLSM30RNq9XSaxnDxEAeXeAwwS6lCLESLFAvH4Ita33H6MdLtnqw\nKTU8ejvOwL5Spl9HbINm7lILurAtPfoqKQAKtJk4q697Wl+3eipfPdCdAoGBALZj\nSDifPdRHdHrInXM1Btyh3rGFbITbeXw/WkHZx4xi1CW+cx72rf9r89t6gBBrlJwR\nVS43kqwrhZ7BlowUkkDDTzrFaG8ie3SJ+RxDuNaZHBeg2CPZvLBo8p/cX0aLulQO\nkHWnESIfIfpaow9rRmRlPi6vkiLv4tFisqqzIQw5AoGBAKG66lipr7u7hef4r0oq\nJglVJgmZ4ud0z73b+Rw0xB9P4lrMOUqmngPntUTzpsaBNYm+asKDSXJpxanBykwV\nY1pnSR5sQpKQ5F4JgIGSmSfhp+S3oAZblk6Z16UsPF8SfilSFv7DSWz9KvMR63h1\nGVJxeyojTyETgAjLLiRbJVbW\n-----END PRIVATE KEY-----\n",
  "client_email": "sr-user@omega-jet-222316.iam.gserviceaccount.com",
  "client_id": "105961696768699281514",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/sr-user%40omega-jet-222316.iam.gserviceaccount.com"
}"""
try:
    print("You said: " + r.recognize_google_cloud(audio, credentials_json=credentials))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
