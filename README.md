# AlgoContestSlackBot



Notify algorithm contest schedules to slack channel.
(Currently, it notifies Codeforces contest schedule to Slack channel.)


## How to run
To test the bot, you should configure your own channelName in test.py or app.py

Configure channelName in test.py and run the following command in the terminal.
```sh
$ SLACK_HOOK_URL=[YOUR_HOOK_URL] python test.py
```
Your hook url should be provided by Slack API.

## Result
![alarm image in slack](docs/alarm_sample1.png)
