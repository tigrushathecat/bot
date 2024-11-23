class Card:
    def __init__(self, power, element, pic_url, name, description, rarity):
        self.power = power
        self.element = element
        self.pic_url = pic_url
        self.name = name
        self.description = description
        self.rarity = rarity

    def show_card(self):
        return (f"{self.name}\n"
                f"Сила: {self.power}\n"
                f"Стихия: {self.element}\n"
                f"Описание: {self.description}\n"
                f"Редкость: {self.rarity}\n")

common_cards = []
common_cards.append(Card(10, "ТЬМА", "Models/cards_pics/Bobik.jpg",
                         "БОБИК", "бобик идет", "default"))
common_cards.append(Card(15, "ЗЕМЛЯ", "Models/cards_pics/СЭР.jpg",
                         "СВОфорд", "СЭР ДА СэР", "default"))
common_cards.append(Card(25, "ТЬМА", "Models/cards_pics/шамиль.jpg",
                         "ШАМИЛЬ", "Все его знают", "default"))

rare_cards = []
rare_cards.append(Card(40, "ТЬМА", "Models/cards_pics/яйца.jpg",
                         "БОБИК", "бобик идет", "rare"))
rare_cards.append(Card(35, "ЗЕМЛЯ", "Models/cards_pics/друг.jpg",
                         "СВОфорд", "СЭР ДА СэР", "rare"))
rare_cards.append(Card(50, "ТЬМА", "Models/cards_pics/фрэш.jpg",
                         "ШАМИЛЬ", "Все его знают", "rare"))

legendary_cards = []
legendary_cards.append(Card(100, "ТЬМА", "Models/cards_pics/дуров.jpg",
                         "Дуров", "Павла Дурова ареcтуют в 2024 году в Париже", "legendary"))

all_cards = {"default": common_cards, "rare": rare_cards, "legendary": legendary_cards}