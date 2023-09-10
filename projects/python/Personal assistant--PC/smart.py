# importing speech recognition package from google api
import speech_recognition as sr
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os # to save/open files
import webbrowser
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations
import pywhatkit
num = 1
def assistant_speaks(output):
	global num

	# num to rename every audio file
	# with different name to remove ambiguity
	num += 1
	print("PerSon : ", output)

	toSpeak = gTTS(text = output, lang ='en', slow = False)
	# saving the audio file given by google text to speech
	file = str(num)+".mp3"
	toSpeak.save(file)
	
	# playsound package is used to play the same file.
	playsound.playsound(file, True)
	os.remove(file)



def get_audio():

	rObject = sr.Recognizer()
	audio = ''

	with sr.Microphone() as source:
		print("Speak...")
		
		# recording the audio using speech recognition
		
		audio = rObject.listen(source,  phrase_time_limit = 2)
	print("Stop.") # limit 5 secs

	try:

		text = rObject.recognize_google(audio, language ='en-US')
		print("You : ", text)
		return text

	except:

		assistant_speaks("Could not understand your audio, PLease try again !")
		return 0


 
   
def process_text(input):
	try:
		if 'search' in input or 'play' in input:
			# a basic web crawler using selenium
			search_web(input)
			return

		elif "who are you" in input or "define yourself" in input:
			speak = '''Hello, I am Person. Your personal Assistant.
			I am here to make your life easier. You can command me to perform
			various tasks such as calculating sums or opening applications etcetra'''
			assistant_speaks(speak)
			return

		elif "who made you" in input or "created you" in input:
			speak = "you made me embabi."
			assistant_speaks(speak)
			return

		

		elif "calculate" in input.lower():
			
			# write your wolframalpha app_id here
			app_id = "WOLFRAMALPHA_APP_ID"
			client = wolframalpha.Client(app_id)

			indx = input.lower().split().index('calculate')
			query = input.split()[indx + 1:]
			res = client.query(' '.join(query))
			answer = next(res.results).text
			assistant_speaks("The answer is " + answer)
			return

		elif 'open' in input:
			
			# another function to open
			# different application available
			open_application(input)
			return

		else:

			assistant_speaks("I can search the web for you, Do you want to continue?")
			ans = get_audio()
			if 'yes' in str(ans) or 'yeah' in str(ans):
				search_web(input)
			else:
				return
	except :

		assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?")
		ans = get_audio()
		if 'yes' in str(ans) or 'yeah' in str(ans):
			search_web(input)
		if 'no' in str(ans):
			exit
def search_web(input):

	driver = webbrowser
	

	if 'youtube' in input.lower():

		assistant_speaks("Opening in youtube")
		indx = input.lower().split().index('youtube')
		query = input.split()[indx + 1:]
		driver.open("http://www.youtube.com/results?search_query =" + '+'.join(query))
		return

	elif 'wikipedia' in input.lower():

		assistant_speaks("Opening Wikipedia")
		indx = input.lower().split().index('wikipedia')
		query = input.split()[indx + 1:]
		driver.open("https://en.wikipedia.org/wiki/" + '_'.join(query))
		return

	else:

		if 'google' in input:

			indx = input.lower().split().index('google')
			query = input.split()[indx + 1:]
			driver.open("https://www.google.com/search?q =" + '+'.join(query))

		elif 'search' in input:

			indx = input.lower().split().index('google')
			query = input.split()[indx + 1:]
			driver.open("https://www.google.com/search?q =" + '+'.join(query))

		else:

			driver.open("https://www.google.com/search?q =" + '+'.join(input.split()))

		return


# function used to open application
# present inside the system.
def open_application(input):

	if "chrome" in input:
		assistant_speaks("Google Chrome")
		#the path of google chrome to open APP
		os.popen(' /usr/bin/google-chrome /usr/share/man/man1/google-chrome.1.gz')
		return

	elif "firefox" in input or "mozilla" in input:
		assistant_speaks("Opening Mozilla Firefox")
		#the path of Firefox to open APP
		os.popen('/usr/bin/firefox /etc/firefox /snap/bin/firefox')
		return

	elif "word" in input:
		assistant_speaks("libreoffice writer")
		#open libreoffice -writer by operating system
		os.system('libreoffice --writer') 
		return
	elif "excel" in input:
		assistant_speaks("Opening libreoffice calc")
		#open libreoffice --calc by operating system
		os.system('libreoffice --calc')
		return

	elif "whatsapp" in input:
		assistant_speaks("Opening whatsup")
		os.popen('/snap/bin/whatsdesk')
		return

	else:

		assistant_speaks("Application not available")
		return




#code to send message to a number

def Whatsapp_open():
   
    pywhatkit.sendwhatmsg_instantly(
    phone_no="+2050005500", #any phone number
    message="My voice Assistant is talk to you",
    #time_hour=1,
    #time_min=30
    )

###############################################33
# Driver Code
if __name__ == "__main__":
	assistant_speaks("What's your name, Human?")
	name ='Human'
	name = get_audio()
	assistant_speaks("Hello, " + name + '.')
	
	while(1):

		assistant_speaks("What can i do for you?")
		text = get_audio().lower()

		if text == 0:
			continue

		if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
			assistant_speaks("Ok bye, "+ name+'.')
			break

		# calling process text to process the query
		process_text(text)
############################################################
