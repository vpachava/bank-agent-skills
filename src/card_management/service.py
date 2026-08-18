class CardManagementService:
    def __init__(self):
        self.cards = {}

    def get_card(self, card_id: str):
        return self.cards.get(card_id)

    def create_card(self, card_id: str, holder_name: str):
        self.cards[card_id] = {"holder_name": holder_name}
        return True

    def delete_card(self, card_id: str):
        if card_id in self.cards:
            del self.cards[card_id]
            return True
        return False
