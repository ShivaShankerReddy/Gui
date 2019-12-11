"""

@Author:  Shiva Shanker Reddy

"""
import pyttsx3


class Text_To_Speech():
    def __init__(self):
        self.engine = pyttsx3.init()


    def get_voice_list(self):
        voices = self.engine.getProperty('voices')
        return ({
            "male": voices[0].id,
            "female": voices[1].id
        })
    

    def set_voice(self, gender='male'):
        self.engine.setProperty('voice',
            self.get_voice_list()[gender]
        )


    def run_and_wait(self, stop= False):
        self.engine.runAndWait()
    

    def say(self, text = "Hello World..!!!"):
        self.engine.say(text, "text")
    

    def change_rate(self, rate=0):
        default_rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', default_rate + ( rate ))
    

    def change_volume(self, volume=0):
        """
        Floating point volume in the range of 0.0 to 1.0 inclusive
        """
        default_volume = self.engine.getProperty('volume')
        self.engine.setProperty('volume', default_volume + (volume))


def run(text= ''):
    tts = Text_To_Speech()
    tts.set_voice(gender='female')
    tts.say(text=text)
    tts.run_and_wait()
