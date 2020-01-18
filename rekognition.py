import boto3
client = boto3.client('rekognition', region_name='us-east-1', aws_access_key_id='AKIAJUNDV4AEW3TWKQ6Q',
                      aws_secret_access_key='XUAM1Ngz8MsXHB9FS8Nc5ttPxItU6/DWLdg7YPS2')

photo="sample1_back.jpg"
with open(photo, "rb") as imageFile:
        response = client.detect_text(Image={'Bytes': imageFile.read()})
        textDetections = response['TextDetections']
        # print(textDetections[0][''])

a=[]
for i in textDetections:
    a.append(i['DetectedText'])

print(a)