class User:
    def __init__(self, id, name, surname, nick):
        self.id = id
        self.name = name
        self.surname = surname
        self.nick = nick
        self.cards_collection = []
        self.time = None

    def show(self):
        return f'{self.id} {self.name} {self.surname} {self.nick}'

    def add_card(self, card):
        self.cards_collection.append(card)

    def get_cards_collection_names(self):
        names_list = [card.name for card in self.cards_collection]
        res = "Ваши карточки\n"
        for i in range(len(names_list)):
            res += f"{i+1}) {names_list[i]}\n"
        return res


all_users = {}
