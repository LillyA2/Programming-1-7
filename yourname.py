from stanfordkarel import *


class ktools:
  def m(self): 
    """Shorthand for Move"""
    move()

  def tl(self):
    """Turn left"""
    turn_left()

  def tr(self):
    """Turn Right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
    """Turn Around"""
    self.tl()
    self.tl()

  def put(self):
    """Put Beeper"""
    put_beeper()

  def put2(self):
    """Put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """Put 5 beepers in a line"""
    self.put2()
    self.m()        
    self.put2()
    self.m()
    self.put()

  def put10(self):
    """put 5 beepers in a line"""
    self.put5()
    self.m()
    self.put5()

  def h(self):
    """Print H using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()
    
  def fic(self):
    """Front is clear"""
    return front_is_clear()

  def fib(self):
    """Front is Blocked"""
    return not self.fic()

  def ric(self):
    """Right is Clear"""
    self.tr()
    if self.fic():
      self.tl()
      return True 
      self.tl()
      return False

  def rib(self) -> bool:
    """Right is Blocked"""
    return not self.ric()

  def mazemove(self):
    """Maze Move"""
    if self.fib():
        self.tl()
    else: #otherwise...
      self.m()
      if self.ric():
        self.tr()
        self.m()
        if self.ric():
          self.tr()
          self.m()
      pass
      
  def mm(self, num):
    """Move Multiple"""
    for number in range(0, num):
      self.m()

  def putm(self, num):
    """Put multiple"""
    for i in range(num - 1):
      self.put()
      self.m()
      self.put()
    
  def pickm(self, num):
    """Pick multiple"""
    for _ in range(num - 1):
      self.pick()
      self.m()
      self.pick()
    
def main():
  """Karel code goes here!"""
  kt = ktools()
  kt.tl()
  kt.put5()
  kt.tr()
  kt.m()
  kt.put2()
  kt.tr()
  kt.put5()
  kt.ta()
  kt.m()
  kt.m()
  kt.tl()
  kt.m()
  kt.put2()
  kt.ta()
  kt.m()
  kt.m()
  kt.m()
  kt.tl()
  kt.m()
  kt.m()
  kt.tr()
  kt.m()
  kt.tr()
  kt.put5()
  kt.tl()
  kt.m()
  kt.put2()
  kt.tl()
  kt.put5()
  kt.tr()
  kt.m()
  kt.m()
  kt.put2()
  kt.m()
  kt.put()
  kt.ta()
  kt.m()
  kt.m()
  kt.tl()
  kt.m()
  kt.put2()
  kt.tl()
  kt.m()
  kt.put2()
  kt.tr()
  kt.m()
  kt.put2()
  kt.tr()
  kt.m()
  kt.put2()
  kt.ta()
  kt.m()
  kt.m()
  kt.m()
  kt.m()
  kt.m()
  kt.tl()
  kt.put5()
  kt.tr()
  kt.m()
  kt.put()
  kt.ta()
  kt.m()
  kt.m()
  kt.put()
  kt.ta()
  kt.m()
  kt.m()
  kt.m()
  kt.m()
  kt.put()
  kt.tr()
  kt.m()
  kt.m()
  kt.put2()
  kt.m()
  kt.put()
  kt.tl()
  kt.m()
  kt.m()
  kt.tl()
  kt.put5()
  kt.tr()
  kt.m()
  kt.put2()
  kt.tr()
  kt.m()
  kt.put2()
  kt.m()
  kt.put2()
  

  pass


if __name__ == "__main__":
    run_karel_program()