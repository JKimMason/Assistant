from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

# Spoken audio is passed as argument
def talkToMe(audio):
	print(audio)
	tts = gTTS(text=audio, lang='en')
	tts.save('audio.mp3')
	os.system('mpg123 audio.mp3')


# Listen for command
def myCommand():
	r = sr.Recognitzer()

	with sr.Microphone() as sourec:
		print("Yes?")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration = 1)
		audio = r.listen(source)

	try:
		command = r.recognize_google(audio)
		print('You said: ' + command + '\n')

	# Loop to listen, if unrecognized
	except sr.UnknownValueError:
		assistant(myCommand())

	return command


# Few commands
def assistant(command):
	if 'open Reddit python' in command:
		chrome_path = "/usr/bin/google-chrome"
		url = 'https://www.reddit.com/r/python'
		webbrowser.get(chrome_path).open(url)

	if 'email' in command:
		talkToMe('To whom?')
		recipient = myCommand()

		if 'Name' in recipient:
			talkToMe('Stating?')
			content = myCommand()

			# Gmail SMTP
			mail = smtplib.SMTP('smtp.gmail.com', 587)

			# Identify to server
			mail.ehlo()

			# encrpyted sessionm
			mail.starttls()

			# Login
			mail.login('username', 'password')

			# Send
			mail.sendmail('Name', 'emailaddress@gmail.com', content)

			# End
			mail.close()

			talkToMe('Email Sent')

while True:
	assistant(myCommand())