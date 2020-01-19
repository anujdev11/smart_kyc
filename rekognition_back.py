import boto3
import re
client = boto3.client('rekognition', region_name='us-east-1', aws_access_key_id='AKIAJUNDV4AEW3TWKQ6Q',
                      aws_secret_access_key='XUAM1Ngz8MsXHB9FS8Nc5ttPxItU6/DWLdg7YPS2')

photo="sample1.jpg"
with open(photo, "rb") as imageFile:
        response = client.detect_text(Image={'Bytes': imageFile.read()})
        textDetections = response['TextDetections']
        # print(textDetections)
        # if(text['Confidence']>85):


a=[]
for text in textDetections:
    if(text['Confidence']>85 and text['Type']=="LINE"):
        a.append(text['DetectedText'])

    #    print(text['DetectedText'])

a1=""
for i in range(len(a)):
    a1+=a[i]
    # if((a[i]=='Address:') or (a[i]=='Address :')):
        # while(1):
        #     a1=a1+a[i+1]
        #     i=i+1

            # if(re.match(r'\d{6}$',a[i+1])):
            #     break
# print(a)
a1=re.search(r"(^Address:((?! \d+ ).)(, A-za-z0-9 ,)\d+(, \d{6}| \d{6}|\b ))",a1)
print(a1)