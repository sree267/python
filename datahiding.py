

class HidingDemo:
    "program for Hiding data"
    _num = 0

    def numbercount(self):
        self._num += 1
        print("Number count =", self._num)
number = HidingDemo()
number.numbercount()
print(number._num)
