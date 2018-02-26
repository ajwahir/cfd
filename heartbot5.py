#!python2
from flask import Blueprint,Response, jsonify,request,session,flash,redirect,url_for, Flask, render_template, current_app as app
from azure.storage.blob import ContentSettings
from azure.storage.blob import BlockBlobService
import httplib, urllib, base64
from azure.storage.blob import PublicAccess
import time
import operator
import os
import cognitive_face as CF
import requests
import random
global cname
cname = "a"+str(random.randrange(1,10000))
block_blob_service = BlockBlobService(account_name="spstorageone", account_key="khLKjd9wd2xX+aUcvsDV70n1c8/r3rBRuxxZDarqlHK4JDUDpqax/tGpY0VJJxroplz8H+dXNV0iOJ0b5u4iAQ==")
block_blob_service.create_container(cname, public_access=PublicAccess.Container)
i=1
j=1
while i==1:
    try:
        tt="a"+str(j)
        j=j+1
        _url = block_blob_service.create_blob_from_path(cname,tt,"image.jpg", content_settings=ContentSettings(content_type="image/jpg"))
        headers = { "Ocp-Apim-Subscription-Key": "f9f8861a83094587ad61843d5c0ebe78" }
        face_api_url = "https://westus.api.cognitive.microsoft.com/face/v1.0/detect"
        params = {
            "returnFaceId": "false",
            "returnFaceLandmarks": "false",
            "returnFaceAttributes": "smile,emotion",
        }
        k = "https://spstorageone.blob.core.windows.net/{}/{}".format(cname,tt)
        print k
        response = requests.post(face_api_url, params=params, headers=headers, json={"url": k})
        faces = response.json()
        print max(faces[0]["faceAttributes"]["emotion"],key=faces[0]["faceAttributes"]["emotion"].get)
        time.sleep(1)
    except Exception as e:
        pass