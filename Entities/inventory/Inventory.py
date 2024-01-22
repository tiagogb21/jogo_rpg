class Inventory:
    def __init__(self):
        self._items = {}

    def add_item(self, item, quantity = 1):
        if item in self._items:
            self._items[item] += quantity
        else:
            self._items[item] = quantity

    def remove_item(self, item, quantity = 1):
        if item in self._items:
            if self._items[item] > quantity:
                self._items[item] -= quantity
            else:
                del self._items[item]
        else:
            print(f"{item} não encontrado no inventário.")
    
    def display_inventory(self):
        for item, quantity in self._items.items():
            print(f"{item.name}: {quantity}")
