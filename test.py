from app import *

channelName = "@joon"
if __name__ == '__main__':
    response = requests.get(targetUrl)
    parseHtmlInfo(response, hookUrl, channelName)






