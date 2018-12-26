# AlgoContestSlackBot



Notify algorithm contest schedules to slack channel.
(Currently, it notifies Codeforces contest schedule to Slack channel.)


## How to run
Using [Python 3.7](https://www.python.org/downloads/release/python-371/) and
[Pipenv](https://pipenv.readthedocs.io/en/latest/) is highly recommended.
If you already have them, run the following to install dependencies.

```sh
$ pipenv install
```

To test the bot, you should configure your own channelName in test.py or app.py.

Configure channelName in test.py and run the following command in the terminal.
```sh
$ SLACK_HOOK_URL=[YOUR_HOOK_URL] pipenv run python test.py
```
Your hook url should be provided by Slack API.

## Result
![alarm image in slack](docs/alarm_sample1.png)
