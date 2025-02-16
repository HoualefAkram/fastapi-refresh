from .ui import Ui

class Html:
    def __init__(self, content):
        self.content = content

    
    @staticmethod
    def home():
        return Ui.home()