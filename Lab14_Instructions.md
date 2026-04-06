# Welcome to Lab14 and Exam 2 Review!

### Classes & Dictionaries

In this lab, you will use classes and dictionaries together in Python.

---

## Notes

#### What is a class?
A class is a blueprint for creating objects. Each object created from a class can have its own data (called **attributes**) and actions (called **methods**). You define a class using the `class` keyword.

#### What is `__init__`?
`__init__` is a special method that runs automatically when you create a new object. It sets up the object's starting attributes.

```python
class GearItem:
    def __init__(self, name, gear_type, power):
        self.name = name        # stores the name on this object
        self.gear_type = gear_type
        self.power = power
```

#### What is `__str__`?
`__str__` is a special method that controls what gets printed when you `print()` an object. It should return a string.

```python
def __str__(self):
    return f"{self.name} ({self.gear_type}) — {self.power} PWR"

item = GearItem("Plasma Rifle", "weapon", 85)
print(item)  # prints: Plasma Rifle (weapon) — 85 PWR
```

#### Accessing another object's attributes
If you have two objects, you can access one object's attributes from within another using dot notation:

```python
bot7.unit_id         # accesses unit_id on bot7
squadmate.inventory  # accesses inventory on the squadmate object
```

---

## Overview

Cashier-Bot is a decommissioned retail unit who has been pressed into service as a crew member aboard the starship *Endless Clearance*. Your job: build the gear management system Cashier-Bot uses to track weapons, mods, and supplies during missions.

You'll build two classes that work together — `GearItem` and `CashierBot` — and by the end, Cashier-Bot will be able to trade gear with a squadmate mid-mission.

---

## Starter Code

Copy the code below into a new Python file to get started.

```python
class GearItem:
    def __init__(self, name, gear_type, power):
        self.name = name
        self.gear_type = gear_type  # e.g. "weapon", "mod", "consumable"
        self.power = power

    def __str__(self):
        return f"{self.name} ({self.gear_type}) — {self.power} PWR"


class CashierBot:
    def __init__(self, unit_id):
        self.unit_id = unit_id
        self.inventory = {}   # item_name (str) -> GearItem object

    #Exercise 1
    def equip(self, item):
        # TODO: add item to inventory
        pass

    #Exercise 2
    def unequip(self, item_name):
        # TODO: remove and return item from inventory
        pass

    #Exercise 3
    def scan_inventory(self):
        # TODO: print all items currently in inventory
        pass

    #Exercise 4
    def trade_gear(self, item_name, squadmate):
        # TODO: Trade an item to the chosen squadmate
        pass
```

---

## Your Lab

| Part | Topic |
| --- | --- |
| 1 | Equipping items |
| 2 | Unequipping items |
| 3 | Scanning inventory |
| 4 | Trading gear between bots |

---

### Exercise 1 — `equip(self, item)`

Add the given `GearItem` to Cashier-Bot's `inventory` dictionary, using the item's **name** as the key.

**Some Tips**
- To print a variable inside a string, research f-strings!

Print a confirmation like:
```
[CASHIER-BOT-7] Equipped: Plasma Rifle.
```

---

### Exercise 2 — `unequip(self, item_name)`

Remove the item with that name from the inventory and return it.

**Some Tips**
- Use the `in` operator to check if a key exists in a dictionary: `if item_name in self.inventory`

If the item isn't found, print a message and return `None`:
```
[CASHIER-BOT-7] Item not found in inventory. Have you checked aisle 4?
```

---

### Exercise 3 — `scan_inventory(self)`

Loop over the inventory dictionary and print each item using its `__str__` method.

**Some Tips**
- Refer to previous code which uses f-strings in order to complete this problem.

Expected output:
```
[CASHIER-BOT-7] Current inventory:
  Plasma Rifle (weapon) — 85 PWR
  Stim Pack (consumable) — 30 PWR
```

---

### Exercise 4 — `trade_gear(self, item_name, squadmate)`

Add a new method to `CashierBot`. Unequip the item from `self`'s inventory and have `squadmate` equip it. Handle the case where `self` doesn't have the item.

**Some Tips**
- `squadmate` is just another `CashierBot` object — you can call its methods the same way: `squadmate.equip(item)`
- You already wrote `unequip` and `equip` — reuse them here!

Print something like:
```
[CASHIER-BOT-7] Transferring Stim Pack to CASHIER-BOT-12. Please retain your receipt.
```

---

## Bonus Challenge

Give each `CashierBot` an `energy` attribute (an integer). Trading gear costs the *sending* bot energy equal to the item's `power` value — Cashier-Bot wasn't built for this, after all.

Only complete the trade if the sending bot has enough energy. Print the remaining energy after each trade.