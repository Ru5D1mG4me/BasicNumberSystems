# BasicNumberSystems
This module will allow you to easily work with basic number systems such as binary, octal and hexadecimal.
## Usage
```Python
import basicnumbersystems as bns


# Creating classes
bns.Bin(8)  # Creates a binary class
bns.Oct(10) # Creates an octal class
bns.Hex(22) # Creates a hex class

# Methods
print(bns.Bin(8).get_num())  # prints -> '1000'
print((bns.Hex(16) + bns.Hex(22)).get_num())  # prints -> '26'
print((bns.Oct(5) * bns.Oct(20)).to_dec())  # prints -> 100

# Used //
print((bns.Bin(2) / bns.Bin(10)).to_dec())  # prints -> 0
print((bns.Bin(2) / bns.Bin(10)).get_num())  # prints -> '0'
print((bns.Oct(9) / bns.Oct(2)).get_num())  # prints -> 4
```
