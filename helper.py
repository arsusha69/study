from attr.setters import convert


class schoolClass:
    def __init__(self):
        self.name = ""

    # Метод для установки имени школы
    def set_name(self, name):
        self.name = name

    # Метод для вывода информации о школе
    def print_info(self):
        print(f"School Name: {self.name}")

class Rim:
    def __init__(self):
        self.rim=""

    def convert(self,roman):
        self.rim=roman
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0

        for char in reversed(self.rim):
            value = roman_dict[char]
            total += value

        return total

    def printIntNumber(self):
        total=self.convert(self.rim)
        print("Converted to integer:", total)
class valid_parentheses():
    def __init__(self):
        self.mass=""

    def mass(self,mass):
        self.mass=mass
        # Словарь для подсчета количества вхождений элементов
        count_dict = {}

        # Подсчет вхождений
        for element in self.mass:
            if element in count_dict:
                count_dict[element] += 1
            else:
                count_dict[element] = 1

        # Проверка на четность количества повторений
        has_even_count = False
        for count in count_dict.values():
            if count % 2 == 0:
                has_even_count = True
                break

        if has_even_count:
            print("true")
        else:
            print("false")