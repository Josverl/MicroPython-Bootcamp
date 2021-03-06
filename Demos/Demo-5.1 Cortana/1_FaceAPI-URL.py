# coding: utf-8
# # Face detection using Cognitive Services
# This walkthrough shows you how to use the cognitive services 
# [Face API](https://azure.microsoft.com/services/cognitive-services/face/) 
# to detect faces in an image. 
# The API also returns various attributes such as the gender and age of each person. 
# The sample images used in this walkthrough are from the [How-Old Robot](http://www.how-old.net) 
# that uses the same APIs.
# 
# For more information, see the 
# [REST API Reference](https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236).
# 
# ## Prerequisites
# You must have a [Cognitive Services API account]
# (https://docs.microsoft.com/azure/cognitive-services/cognitive-services-apis-create-account) 
# with **Face API**. 
# The [free trial](https://azure.microsoft.com/try/cognitive-services/?api=face-api) 
# is sufficient for this quickstart. 
# You need the subscription key provided when you activate your free trial,
#  or you may use a paid subscription key from your Azure dashboard.
# 

#  Running the walkthrough
# To continue with this walkthrough, replace `subscription_key` with a valid subscription key.
import gc
import urequests  #pylint: disable=import-error

subscription_key = '0366c4649003438ea99891d9006809bd'
assert subscription_key
# Next, verify `face_api_url` and make sure it corresponds to the region you used when generating the subscription key. If you are using a trial key, you don't need to make any changes.
face_api_url = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect'

# The next few lines of code call into the Face API to detect the faces in the image. In this instance, the image is specified via a publically visible URL. You can also pass an image directly as part of the request body. For more information, see the [API reference](https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236). 
hdr_key = { 'Ocp-Apim-Subscription-Key': subscription_key }

#for Micropython must add the query string parameters to the url 
def post(url,params=None, **kw):
    if params!=None:
        #todo: urllib.urlencode the parameters 
        glue = "?"
        for k in params:
            url=url+"{}{}={}".format(glue,k,params[k])
            glue="&"
    return urequests.request("POST", url, **kw)

#set up a few different sets of parameters to the API 
param_all = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
}
param_some = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,emotion,hair'
}
param_simple = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false'
}

#The core functionality is in processing an image, and all faces in it 
def detect_faces(image_url= None):
    if image_url == None:
        return None
    jsonbody = {"url": image_url}
    try:
        response = post(face_api_url, json=jsonbody, headers=hdr_key, params=param_some)
        if response.status_code >= 400  :
            print('En error has occurred : HTTP Error {}'.format(response.status_code))
        elif response.status_code == 200:
            #print(response.json())
            faces = response.json()
    finally:
        response.close()
    gc.collect()
    return faces

def process_faces(faces):
    print("Detected {} faces in the image".format(len(faces)))
    for face in faces:
        print ("a {} year old {}".format( face['faceAttributes']['age'], face['faceAttributes']['gender']) )



# You can experiment with different images  by changing ``image_url`` to point 
# to a different image and rerunning this code.
for i in range(9):
    image_url = 'https://how-old.net/Images/faces2/main00{}.jpg'.format(i)
    print("Detecting image {}".format(image_url ))
    faces = detect_faces( image_url )
    process_faces ( faces)
    print('---------------------------------------------------------------')



# 
image_url = 'http://photonshouse.com/photo/c6/c60bfd79e990878486374b7d833ccd8e.jpg'
faces = detect_faces( image_url )
process_faces ( faces)

image_url = 'https://secure.i.telegraph.co.uk/multimedia/archive/01827/Lakshmi-Mittal_1827147b.jpg'
faces = detect_faces( image_url )
process_faces ( faces)

image_url = 'https://pix.avaxnews.com/avaxnews/4a/42/0004424a.jpeg'
faces = detect_faces( image_url )
process_faces ( faces)
