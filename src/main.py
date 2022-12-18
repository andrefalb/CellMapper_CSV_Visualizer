import requests

url = 'https://eu1.unwiredlabs.com/v2/process.php'
myobj = {
    "token": "pk.c535698c162bcc519d6c3ae268fe605c",
    "radio": "lte",
    "mcc": 262,
    "mnc": 1,
    "cells": [{
        "lac": 3080,
        "cid": 30926087,
        "psc": 0
    }],
    "address": 1
}

x = requests.post(url, json=myobj)

#print the response text (the content of the requested file):

print(x.text)