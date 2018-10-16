# coding: utf-8

# # Face detection using Cognitive Services
# This walkthrough shows you how to use the cognitive services [Face API](https://azure.microsoft.com/services/cognitive-services/face/) to detect faces in an image. The API also returns various attributes such as the gender and age of each person. The sample images used in this walkthrough are from the [How-Old Robot](http://www.how-old.net) that uses the same APIs.
# 
# For more information, see the [REST API Reference](https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236).
# 
# ## Prerequisites
# You must have a [Cognitive Services API account](https://docs.microsoft.com/azure/cognitive-services/cognitive-services-apis-create-account) with **Face API**. The [free trial](https://azure.microsoft.com/try/cognitive-services/?api=face-api) is sufficient for this quickstart. You need the subscription key provided when you activate your free trial, or you may use a paid subscription key from your Azure dashboard.
# 
# ## Running the walkthrough
# To continue with this walkthrough, replace `subscription_key` with a valid subscription key.
import gc
import urequests  #pylint: disable=import-error

subscription_key = '0366c4649003438ea99891d9006809bd'
assert subscription_key
# Next, verify `face_api_url` and make sure it corresponds to the region you used when generating the subscription key. If you are using a trial key, you don't need to make any changes.
face_api_url = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect'

# The next few lines of code call into the Face API to detect the faces in the image. In this instance, the image is specified via a publically visible URL. You can also pass an image directly as part of the request body. For more information, see the [API reference](https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236). 
hdr_key = { 'Ocp-Apim-Subscription-Key': subscription_key }

#Python3
#response = requests.post(face_api_url, params=params, headers=hdr_key, json=jsonbody)

#micropython Need to Add the query string parameters to the url 
def post(url,params=None, **kw):
    if params!=None:
        #micropython Need to Add the query string parameters to the url 
        #todo: urllib.urlencode the parameters 
        glue = "?"
        for k in params:
            url=url+"{}{}={}".format(glue,k,params[k])
            glue="&"
    return urequests.request("POST", url, **kw)

param_all = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
}

param_some = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'age,gender,emotion,hair'
}

param_simple = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false'
}

# Here is the URL of the image. You can experiment with different images  by changing ``image_url`` to point to a different image and rerunning this notebook.

for i in range(9):
    try:
        image_url = 'https://how-old.net/Images/faces2/main00{}.jpg'.format(i)
        jsonbody = {"url": image_url}
        print("Detecting image {}".format(image_url ))
        response = post(face_api_url, json=jsonbody, headers=hdr_key, params=param_some)
        if response.status_code >= 400  :
            print('En error has occurred : HTTP Error {}'.format(response.status_code))
        elif response.status_code == 200:
            #print(response.json())
            faces = response.json()
    finally:
        response.close()
    gc.collect()
    print("Detected {} faces in the image".format(len(faces)))
    for face in faces:
        print ("a {} year old {}".format( face['faceAttributes']['age'], face['faceAttributes']['gender']) )

# Finally, the face information can be overlaid of the original image using the `matplotlib` library in Python.

"""
#get_ipython().run_line_magic('matplotlib', 'inline')
#import matplotlib.pyplot as plt

#from PIL import Image
#from matplotlib import patches
from io import BytesIO

#Get the image - fails on re-direct :-( 
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))


# In[37]:

plt.figure(figsize=(8,8))
ax = plt.imshow(image, alpha=0.5)
for face in faces:
    fr = face["faceRectangle"]
    fa = face["faceAttributes"]
    origin = (fr["left"], fr["top"])
    p = patches.Rectangle(origin, fr["width"], fr["height"], fill=False, linewidth=2, color='b')
    ax.axes.add_patch(p)
    plt.text(origin[0], origin[1], "%s, %d"%(fa["gender"].capitalize(), fa["age"]), fontsize=20, weight="bold", va="bottom")
_ = plt.axis("off")

"""
# Here are more images that can be analyzed using the same technique.
# First, define a helper function, ``annotate_image`` to annotate an image given its URL by calling into the Face API.

# In[29]:


def annotate_image(image_url):
    response = requests.post(face_api_url, params=params, headers=hdr_key, json={"url": image_url})
    faces = response.json()

    image_file = BytesIO(requests.get(image_url).content)
    image = Image.open(image_file)

    plt.figure(figsize=(8,8))
    ax = plt.imshow(image, alpha=0.6)
    for face in faces:
        fr = face["faceRectangle"]
        fa = face["faceAttributes"]
        origin = (fr["left"], fr["top"])
        p = patches.Rectangle(origin, fr["width"],                               fr["height"], fill=False, linewidth=2, color='b')
        ax.axes.add_patch(p)
        plt.text(origin[0], origin[1], "%s, %d"%(fa["gender"].capitalize(), fa["age"]),                  fontsize=20, weight="bold", va="bottom")
    plt.axis("off")


# You can then call ``annotate_image`` on other images. A few examples samples are shown below.

# In[30]:


annotate_image("https://how-old.net/Images/faces2/main001.jpg")


# In[31]:


annotate_image("https://how-old.net/Images/faces2/main002.jpg")


# In[32]:


annotate_image("https://how-old.net/Images/faces2/main004.jpg")

""" 