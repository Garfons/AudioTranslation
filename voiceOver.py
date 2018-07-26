import pyttsx3 
# pip install pyttsx3
# pip install pypiwin32

voicesKeys = {
    "russian": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0",
    "femaleEn": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0",
    "maleEn" : "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
}

class VoiceOver:
    def __init__(self,lang="en"):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        if(lang == "en"):
            self.actor = "femaleEn"
        else:
            self.actor = "russian"

    def speak(self,phrase):
        self.engine.setProperty('voice', voicesKeys[self.actor])
        self.engine.say(phrase)
        self.engine.runAndWait()
