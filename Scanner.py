import cv2
import numpy as np
#import mapper
#import Adhar
import os
import re
import boto3

class AdharExtract:
        def getData(self,img1):
                
                image=cv2.imread(img1)   #read in the image
                image=cv2.resize(image,(1000,800)) #resizing because opencv does not work well with bigger images
                orig=image.copy()
                gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)  #RGB To Gray Scale
                
                blurred=cv2.GaussianBlur(gray,(5,5),0)  #(5,5) is the kernel size and 0 is sigma that determines the amount of blur
                
                 #storing processed image temporarily
                cv2.imwrite('processed_image.png',blurred)

                client=boto3.client('rekognition',region_name='your_region',aws_access_key_id='your_aws_access_key_id',
                aws_secret_access_key='your_aws_secret_access_key')
                 
                with open("processed_image.png", "rb") as imageFile:	
                        response=client.detect_text(Image={'Bytes': imageFile.read()})
                                                                        
                        textDetections=response['TextDetections']
                        print ('Detected text')
                        name,gender,aadhar_no,mobile_no,DoB="","","","",""
                        for text in textDetections:
                                print('Detected text:' + text['DetectedText'])
                                
                                #following is logic to extract details

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
                                        if(re.match(r'\d{4} \d{4} \d{4}',text['DetectedText'])and text['Type']=='LINE'):
                                                print('AADhar number:' + text['DetectedText'])
                                                aadhar_no=text['DetectedText']
                                        if(re.search(r'[A-z][a-z]{1,} [A-Z][a-z]{1,}\s*[a-zA-Z]*',text['DetectedText']) and 'GOV' not in text['DetectedText'] and 'Gov' not in text['DetectedText'] and ":" not in text['DetectedText'] and text['Type']=='LINE'):
                                                print("Name:",text['DetectedText'])
                                                name=text['DetectedText']
                                        if(re.match('\d{10}',text['DetectedText'])):
                                                print("Mobile_no:",text['DetectedText'])
                                                mobile_no=text['DetectedText']
                                        
                                        print ('Type:' + text['Type'])
                return (name,gender,aadhar_no,mobile_no,DoB)

if __name__=='__main__':
        s=sc()
        print(s.getData('pp.jpeg'))