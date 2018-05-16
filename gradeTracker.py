import time
import sys
from os import environ
from bs4 import BeautifulSoup
import urllib2
from twilio.rest import Client


GRADE_URL = "http://www.gradesource.com/reports/288/29963/index.html"

resourceName = ""
gradeReleased = False
secretNum = 2304

## send SMS
def sendSMS(resourceName):
    print("Sending SMS...")
    client.messages.create(to="+12132848160", from_="+18186965717",
                body = resourceName + " Grade Released" )


def findGrade(url, resourceName):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    a = soup.find_all('a')
    for item in a:
        if item.text == resourceName:
            return True
    return False




## begin

# Check if Twilio account is set up
if (environ.get('TWILIO_ACCOUNT') is None) | (environ.get('TWILIO_TOKEN') is None):
    print("Twilio Account and Token Not Found")
    exit()

## Twilio
ACCOUNT = environ.get('TWILIO_ACCOUNT')
TOKEN = environ.get('TWILIO_TOKEN')
client = Client(ACCOUNT, TOKEN)

resourceName = sys.argv[1] if len( sys.argv ) == 2 else raw_input('What grade are we tracking?')

while gradeReleased != True:
    gradeReleased = findGrade(GRADE_URL, resourceName)
    print( (resourceName + " Grade Out!") if gradeReleased else (resourceName + " No Grades") )
    time.sleep(1)

sendSMS(resourceName)

