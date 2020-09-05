from mycroft import MycroftSkill, intent_file_handler


class Batterylevel(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('batterylevel.intent')
    def handle_batterylevel(self, message):
        self.speak_dialog('batterylevel')


def create_skill():
    return Batterylevel()

