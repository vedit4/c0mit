class Human:
	def __init__(self, str_: str, int_: int, bool_: bool) -> None:
		self.str_ = str_
		self.int_ = int_
		self.bool_ = bool_


    
def main_loop():
   person = Human("abcdefg", 12345, True)

   if person.bool_ == True:
       return(person.str_)
   elif person.bool_ == False:
        return(person.int_)

         

	




if __name__ == '__main__':
    main_loop()