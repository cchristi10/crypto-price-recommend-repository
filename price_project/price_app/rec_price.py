'''
This class contains functions that recommeds prices based on the user selection
'''
class Price:

    def __init__(self,exchange1_sp,exchange1_bp,exchange2_sp,exchange2_bp):
        self.exchange1_sp = exchange1_sp
        self.exchange1_bp = exchange1_bp
        self.exchange2_sp = exchange2_sp
        self.exchange2_bp = exchange2_bp

    def rec_sell_price(self):
        '''
        recommeds selling price
        '''
        if  self.exchange1_sp >= self.exchange2_sp:
            return self.exchange1_sp
        else:
            return self.exchange2_sp


    def rec_buy_price(self):
        '''
        recommeds buying price
        '''
        if self.exchange1_bp>=self.exchange2_bp:
            return self.exchange2_bp
        else:
            return self.exchange1_bp




if __name__ == '__main__':
    x = 10
    y = 20
    p = Price(x,y)
    print(p.sell_price())
