import boto3
import re
client = boto3.client('rekognition', region_name='us-east-1', aws_access_key_id='your_access_key',
                      aws_secret_access_key='your_secret_key')

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
                print('Date of Birth:',text['DetectedText'][text['DetectedText'].find('DOB')+5:])
                DoB1=text['DetectedText'][text['DetectedText'].find('DOB')+5:]
                if(DoB1!=""):
                        DoB=DoB1
        if('MALE' in text['DetectedText']):
            print("Gender: Male")
            gender="Male"
        elif('FEMALE' in text['DetectedText']):
            print("Gender: Female")
            gender="Female"
        if(re.match(r'\d{4} \d{4} \d{4}',text['DetectedText']) and text['Type']=='LINE'):
            print('AADhar number:' + text['DetectedText'])
            aadhar_no=text['DetectedText']
        if(re.search(r'[A-Z][a-z]{1,} [A-Z][a-z]{1,}\s*[a-zA-Z]*',text['DetectedText']) and 'GOV' not in text['DetectedText'] and ":" not in text['DetectedText'] and text['Type']=='LINE'):
            print("Name:",text['DetectedText'])
            name=text['DetectedText']
        if(re.match('\d{10}',text['DetectedText'])):
            print("Mobile_no:",text['DetectedText'])
            mobile_no=text['DetectedText']
