class Student:
    def __init__(self,name,chinese,english,math) -> None:
        #實體的ATTRIBUTE
        self.name =name
        self.chinese =chinese
        self.english = english
        self.math = math
    #實體方法
    def total(self)->int:
        return self.chinese + self.english +self.math 
    
    #建立property->類似參數，一定要傳出一個值
    @property
    def averge(self)-> float:
        return self.total()/3.0
    
    def __repr__(self):
        return f"我是stuudent實體，我的name{self.name}"
        