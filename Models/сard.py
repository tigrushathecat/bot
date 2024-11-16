class Card:
    def __init__(self, power, element, pic_url, name, description):
        self.power = power
        self.element = element
        self.pic_url = pic_url
        self.name = name
        self.description = description

    def show_card(self):
        return (f"{self.name}\n"
                f"Сила {self.power}\n"
                f"Стихия {self.element}\n"
                f"{self.description}\n")

all_cards_list = []
all_cards_list.append(Card(10, "ТЬМА", "Models/cards_pics/Bobik.jpg",
                         "БОБИК", "бобик идет"))
all_cards_list.append(Card(15, "ЗЕМЛЯ", "Models/cards_pics/СЭР.jpg",
                         "СВОфорд", "СЭР ДА СэР"))