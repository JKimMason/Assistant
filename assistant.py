from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

# Spoken audio is passed as argument
def talkToMe(audio):
	print(audio)