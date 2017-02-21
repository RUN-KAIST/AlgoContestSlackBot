import json
import random
import datetime
from urllib2 import Request, urlopen
from bs4 import BeautifulSoup
from pytz import timezone
from app import *

targetUrl = "http://codeforces.com/contests"
hookUrl = "https://hooks.slack.com/services/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"
channelName = "@harry"
if __name__ == '__main__':
    response = urlopen(targetUrl)
    parseHtmlInfo(response, hookUrl, channelName)






