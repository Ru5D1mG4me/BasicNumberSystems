class Dec():
  def __init__(self, dec_num):
    self.dec_num = dec_num
    self.num = self.dec_num
    
  def __repr__(self):
    return 'Dec: ' + self.num
    
  def to_dec(self):
    return str(self.dec_num)
    
  def get_num(self):
    return self.num
    
  def __add__(self, other):
    if self.__class__.__name__ == 'Bin':
      return Bin(self.dec_num + other.dec_num)
    elif self.__class__.__name__ == 'Oct':
      return Oct(self.dec_num + other.dec_num)
    elif self.__class__.__name__ == 'Hex':
      return Hex(self.dec_num + other.dec_num)
      
  def __sub__(self, other):
    if self.__class__.__name__ == 'Bin':
      return Bin(self.dec_num - other.dec_num)
    elif self.__class__.__name__ == 'Oct':
      return Oct(self.dec_num - other.dec_num)
    elif self.__class__.__name__ == 'Hex':
      return Hex(self.dec_num - other.dec_num)

  def __mul__(self, other):
    if self.__class__.__name__ == 'Bin':
      return Bin(self.dec_num * other.dec_num)
    elif self.__class__.__name__ == 'Oct':
      return Oct(self.dec_num * other.dec_num)
    elif self.__class__.__name__ == 'Hex':
      return Hex(self.dec_num * other.dec_num)
    
  def __truediv__(self, other):
    if self.__class__.__name__ == 'Bin':
      return Bin(self.dec_num // other.dec_num)
    elif self.__class__.__name__ == 'Oct':
      return Oct(self.dec_num // other.dec_num)
    elif self.__class__.__name__ == 'Hex':
      return Hex(self.dec_num // other.dec_num)

    
class Bin(Dec):
  def __init__(self, dec_num):
    super().__init__(dec_num)
    self.num = bin(self.dec_num).replace('0b', '')
    
  def __repr__(self):
    return f'Bin: {self.num}\nDec: {self.dec_num}'



class Oct(Dec):
  def __init__(self, dec_num):
    super().__init__(dec_num)
    self.num = oct(self.dec_num).replace('0o', '')
    
  def __repr__(self):
    return f'Oct: {self.num}\nDec: {self.dec_num}'


class Hex(Dec):
  def __init__(self, dec_num):
    super().__init__(dec_num)
    self.num = hex(self.dec_num).replace('0x', '').upper()
    
  def __repr__(self):
    return f'Hex: {self.num}\nDec: {self.dec_num}'