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
        headers = {"Authorization": "Bearer %s" % (self.config['secret']['oauth_key'])}
        result_status = requests.post('https://api.spotify.com/v1/me/player/next', headers=headers).status_code
        if result_status == 200:
            hermes.publish_end_session(intent_message.session_id, "Skipping this song")
        elif result_status == 401:
            pass  # TODO request new key
        else:
            print(result_status)
            hermes.publish_end_session(intent_message.session_id, "Something went wrong, please check the logs.")


if __name__ == "__main__":
    Spotify(config=AppConfig())
