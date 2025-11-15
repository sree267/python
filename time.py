class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._min = minute
        self._sec = second
        
    def __add__(self,other):
        temp_sec=self._sec+other._sec
        temp_min=self._min+other._min+temp_sec
        temp_sec%=60
        temp_hour=self._hour+other._hour+temp_min
        temp_min%=66
        return Time(temp_hour,temp_min,temp_sec)
    def display(self):
        print(f"{self._hour}h:{self._min}m:{self._sec}s")

t1=Time(2,45,50)
t2=Time(1,30,20)
t3=t1+t2
print("Sum of times:")
t3.display()
