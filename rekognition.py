import boto3
import re
client = boto3.client('rekognition', region_name='us-east-1', aws_access_key_id='AKIAJUNDV4AEW3TWKQ6Q',
                      aws_secret_access_key='XUAM1Ngz8MsXHB9FS8Nc5ttPxItU6/DWLdg7YPS2')

photo="sample.jpeg"
with open(photo, "rb") as imageFile:
        response = client.detect_text(Image={'Bytes': imageFile.read()})
        textDetections = response['TextDetections']
        # print(textDetections)
        # if(text['Confidence']>85):


a=[]
for text in textDetections:
    if(text['Confidence']>85):
        if(text['Type']=='LINE' and re.search(r'\w* \w*',text['DetectedText'])):
            if('DOB' in text['DetectedText']):
                print(text['DetectedText'])


        # print ('Type:' + text['Type'])
# print(a)