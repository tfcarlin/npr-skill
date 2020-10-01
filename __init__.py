from mycroft import MycroftSkill, intent_file_handler


class Npr(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('npr.intent')
    def handle_npr(self, message):
        self.speak_dialog('npr')


def create_skill():
    return Npr()

