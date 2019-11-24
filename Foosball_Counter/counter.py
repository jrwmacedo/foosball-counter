from display import Display


class Counter:
    def __init__(self, teamname, display: Display):
        self.teamName = teamname
        self.buttonPlus = None
        self.buttonPlusPressing = 0
        self.buttonMinus = None
        self.buttonMinusPressing = 0
        self.counter = 0
        self.last_counter = 0
        self.display = display
