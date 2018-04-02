

class Hand:
    def __init__(self):
        self.hand = []
        # self.value = self.value()

    def draw(self, lst, number=1):
        for i in range(number):
            self.hand.append(lst.pop())
        return self.hand

    def value(self):
        sum = 0
        sum2 = 0
        for i in range(len(self.hand)):
            sum += self.hand[i].value
            if 'Ace' in self.hand[i].__str__:
                sum2 = sum + 10
        if sum == 21:
            return sum
        if sum2 == 21:
            return sum2
        elif sum2 > 21:
            return sum
        elif sum2 == 0:
            return sum
        else:
            if sum2 > sum:
                return sum2
            elif sum > sum2:
                return sum

    def display(self):
        for i in range(len(self.hand)):
            print(self.hand[i].__str__)


    def return_card(self, lst):
        for i in range(len(self.hand)):
            lst.insert(0, self.hand.pop())

