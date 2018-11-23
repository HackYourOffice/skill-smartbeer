from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import requests

class BeerSkill(MycroftSkill):

    def __init__(self):
        super(BeerSkill, self).__init__(name="BeerSkill")

    @intent_handler(IntentBuilder("").require("Darf").require("Bier").require("Trinken"))
    def handle_bier_intent(self, message):
        r = requests.get('https://bier.synyx.de')
        i = r.text.find('YES! Beertime!')
        if i > 0:
            self.speak_dialog("zum.wohl")
        else:
            self.speak_dialog("noch.nicht")

def create_skill():
    return BeerSkill()
