import json
import random
import datetime
import requests
from bs4 import BeautifulSoup
import dateutil.tz
import os

targetUrl = "http://codeforces.com/contests"  # Codeforces contest page
hookUrl = os.environ.get('SLACK_HOOK_URL')
channelName = "contest_alarm"
botName = "Codeforces Bot"
hourDifference = 6  # Korea is UTC + 9 and Codeforces system is UTC + 9
timeFormat = "%Y/%m/%d %I:%M %p"


def index(): # This function is main function.
    response = requests.get(targetUrl)
    if response.status_code == 200:
        if not parseHtmlInfo(response, hookUrl, channelName):
            print('Failed to send via the slack message')
            return False
    else:
        print('Failed to fetch the contest list')
        return False

    return True


def generateAttachPayload(title, text):
    attachPayload = {
        'title': title,
        'text': text,
        'color': '#%06X' % random.randint(0, 0xFFFFFF)
    }
    return attachPayload


def generateAndSendPayload(titleText, attachments, targetChannelUrl, targetChannelName):
    payload = {
        'channel': targetChannelName,
        'username': botName,
        'text': titleText,
        'attachments': attachments
    }
    return requests.post(targetChannelUrl, data=json.dumps(payload)) == 200


def parseHtmlInfo(response, targetChannelUrl, targetChannelName):
    bsObj = BeautifulSoup(response.text, "html.parser")
    contestInfo = bsObj.find_all("div", {"class": "datatable"})[0]

    allRows = contestInfo.find_all("tr")
    numRows = len(allRows) - 1

    headRow = allRows[0].find_all("th")

    attachments = []
    titleText = "*<%s|Go to Codeforces contests list>*\n" % (targetUrl)
    currentTime = datetime.datetime.now(dateutil.tz.gettz('Asia/Seoul')).strftime(timeFormat)
    titleText += "Current time: %s" % (currentTime)
    for contNum in range(numRows):
        if contNum >= 3:
            break
        attachText = ""
        attachTitle = ""
        dataRow = allRows[contNum + 1].findAll("td")
        for i in range(len(headRow)):
            headText = headRow[i].text.strip()
            dataText = dataRow[i].text.strip()
            if len(headText) == 0:
                if len(dataText) == 0:  # Check exception case
                    continue
                else:  # Attributes with no headTexts
                    newDataList = []
                    dataList = dataText.split(" ")
                    for i in range(len(dataList)):
                        if len(dataList[i]) != 0:
                            newDataList.append(dataList[i])
                    newDataText = " ".join(newDataList)
                    attachText += "%s\n" % (newDataText)
            else:
                if len(dataText) == 0:
                    dataText = "Unknown"
                if headText == "Name":  # Contest name
                    attachTitle += "%s : %s\n" % (headText, dataText)
                elif headText == "Start":  # Contest start time
                    startTime = datetime.datetime.strptime(dataText, "%b/%d/%Y %H:%M")
                    startTime += datetime.timedelta(hours=hourDifference)
                    adjustedDate = startTime.strftime(timeFormat)
                    attachText += "%s : %s\n" % (headText, adjustedDate)
                elif headText == "Writers":
                    continue
                else:  # Other attributes
                    attachText += "%s : %s\n" % (headText, dataText)
        attachPayload = generateAttachPayload(attachTitle, attachText)
        attachments.append(attachPayload)

    return generateAndSendPayload(titleText, attachments, targetChannelUrl, targetChannelName)

