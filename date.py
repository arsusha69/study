class Date:
    def __init__(self, size):
        self.day = []
        self.month = []
        self.year = []

    # Устанавливаем дату
    def setDate(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    # Выводим информацию о дате
    def printData(self):
        print(f"Day: {self.day}, Month: {self.month}, Year: {self.year}")