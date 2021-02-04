#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 18:42:43 2021

@author: javierbrionesgomez
"""

### WAKE_TEAM: DATAPROJECT 2 
### POST A TWEET 

#INSTALL
pip install tweepy

#IMPORT
import tweepy
import json

#AUTHENTICATION

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

tweet = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


#PUBLISH A TWEET

#tweet.update_status("Hello World!")


#REPLY A TWEET
#We need the ID of tweet you want to reply.

tweet_id=''

tweet.update_status("WakeText", in_reply_to_status_id=tweet_id)