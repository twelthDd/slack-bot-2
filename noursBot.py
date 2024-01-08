import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ["SIGNING_SECRET"], "/slack/events", app)

client = slack.WebClient(token=os.environ["SLACK_TOKEN"])

@slack_event_adapter.on("message")
def event(payload):
    event = payload.get("event", {})
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")
    timestamp = event.get("ts")
    event_type = event.get("type")
    event_subtype = event.get("subtype")


    if event_type == "message":
        if not user_id == "U06C38LSP1Q":
            if channel_id == "C06C5Q3GF5J":
                try:
                    client.chat_delete(channel=channel_id, ts=timestamp)
                except:
                    print(f"\n------------------------\nUser: {user_id}\nChannel: {channel_id}\nType: {event_type}\nTimestamp: {timestamp}\n\nDetailed Event: {event}\n------------------------\n")

if __name__ == "__main__":
    app.run(debug=True)