class Dec():
  def __init__(self, dec_num:int=0):
    self._dec_num = dec_num
    self._num = self._dec_num
    
  def __repr__(self):
    return 'Dec: ' + self._num
    
  def to_dec(self):
    return str(self._dec_num)
    
  def get_num(self):
    return self._num
    
  def __add__(self, other):
    if self.__class__.__name__ == 'Bin':
      return Bin(self._dec_num + other._dec_num)
    elif self.__class__.__name__ == 'Oct':
      return Oct(self._dec_num + other._dec_num)
    elif self.__class__.__name__ == 'Hex':
      return Hex(self._dec_num + other._dec_num)
      
  def __sub__(self, other):
    if self.__class__.__name__ == 'Bin':
      return Bin(self._dec_num - other._dec_num)
    elif self.__class__.__name__ == 'Oct':
      return Oct(self._dec_num - other._dec_num)
    elif self.__class__.__name__ == 'Hex':
      return Hex(self._dec_num - other._dec_num)

  def __mul__(self, other):
    if self.__class__.__name__ == 'Bin':
      return Bin(self._dec_num * other._dec_num)
    elif self.__class__.__name__ == 'Oct':
      return Oct(self._dec_num * other._dec_num)
    elif self.__class__.__name__ == 'Hex':
      return Hex(self._dec_num * other._dec_num)
    
  def __truediv__(self, other):
    if self.__class__.__name__ == 'Bin':
      return Bin(self._dec_num // other._dec_num)
    elif self.__class__.__name__ == 'Oct':
      return Oct(self._dec_num // other._dec_num)
    elif self.__class__.__name__ == 'Hex':
      return Hex(self._dec_num // other._dec_num)

    
class Bin(Dec):
  def __init__(self, dec_num:int=0):
    super().__init__(dec_num)
    self._num = bin(self._dec_num).replace('0b', '')
    
  def __repr__(self):
    return f'Bin: {self._num}\nDec: {self._dec_num}'



class Oct(Dec):
  def __init__(self, dec_num:int=0):
    super().__init__(dec_num)
    self._num = oct(self._dec_num).replace('0o', '')
    
  def __repr__(self):
    return f'Oct: {self._num}\nDec: {self._dec_num}'


class Hex(Dec):
  def __init__(self, dec_num:int=0):
    super().__init__(dec_num)
    self._num = hex(self._dec_num).replace('0x', '').upper()
    
  def __repr__(self):
    return f'Hex: {self._num}\nDec: {self._dec_num}'