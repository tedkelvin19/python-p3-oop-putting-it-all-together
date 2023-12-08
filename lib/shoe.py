#!/usr/bin/env python3

class Shoe:
    pass
    def __init__(self,brand,size):
        self.brand = brand
        self.size = size

    def set_size(self,size):
        if not isinstance(size,int):
            print("size must be an integer")
        else:    
            self.size = size   
     
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"