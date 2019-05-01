#!/usr/bin/env python3
"""This is an example of a Snips app using the Hermes protocol with the
SnipsKit library.
This app listens for an intent and answers the user.
You can find the documentation of this library in:
https://snipskit.readthedocs.io/
"""
from snipskit.hermes.apps import HermesSnipsApp
from snipskit.hermes.decorators import intent
from snipskit.config import AppConfig
import requests


class Spotify(HermesSnipsApp):

    @intent('MasX:NextSong')
    def next_song(self, hermes, intent_message):
        headers = {
        "Authorization": "Bearer %s" % (self.config['secret']['oauth_key'])}
        results = requests.post('https://api.spotify.com/v1/me/player/next', headers=headers).json
        print(results)
        hermes.publish_end_session(intent_message.session_id, results)


if __name__ == "__main__":
    Spotify(config=AppConfig())
