'''Место для импортирования модулей'''
from data import *


class Crypto_calc(object):
    '''Класс крипто-калькулятора'''

    def __init__(self, token, num_tokens, token2="BTC"):
        '''Конструктор инициализирующий все атрибуты класса.

        Класс обладает тремя атрибутами:
        token - имя токена представленного к продаже.
        num_tokens - количество токенов к продаже.
        token2 - имя токена, на котрый будет произведен обмен.
        По умолчанию мы обмениваем на биткоин.
        
        '''

        self.token = token
        self.num_tokens = num_tokens
        self.token2 = token2

    def total_order_price(self):
        '''Оптимальная общая стоимость сделки'''

        cost_cex_sale = self.sell_to_CEX()
        cost_cex_buy = self.ideal_price("CEX")

        return cost_cex_sale + ((cost_cex_buy - cost_cex_sale) / 2)
        
    def optimal_discount(self):
        '''Оптимальный размер скидки для покупателя
        
        Полученное значение опирается на оптимальную стоимость
        сделки и ту сумму, за которую в идеальном случае мы могли
        бы продать эти токены.
        
        '''

        cost_disc = self.ideal_price("CEX") - self.total_order_price()
        return (cost_disc * 100) / self.ideal_price("CEX")

    def price_token(self):
        '''Цена токена'''

        pass
    
    def ideal_price(self, type_stock):
        '''Функция идеальной цены, если бы мы продали по курсу.
        
        Определяем максимальную возможную цену, исходя из
        курса (средней цены продаж) на бирже.
        
        '''

        max_price = 0
        for stock in TOKEN[type_stock]:
            if float(TOKEN[type_stock][stock]["price"]) > max_price:
                max_price = float(TOKEN[type_stock][stock]["price"])
        
        return float(max_price) * self.num_tokens

    def sell_to_CEX(self):
        '''Конечная цена при потери в 40% на CEX.
        
        Здесь будет описан алгоритм получения сконвертированной цены
        для CEXs

        '''

        total_sum = 0.
        for stock in TOKEN["CEX"]:
            total_sum += float(TOKEN["CEX"][stock]["volume"])
        
        result_cost = 0
        for stock in TOKEN["CEX"]:
            coef_prior = (float(TOKEN["CEX"][stock]["volume"])) / total_sum
            result_cost += coef_prior * self.ideal_price("CEX")
        
        # Уменьшаем на 40%
        result_cost = (result_cost * 60) / 100.

        return result_cost
    
    def buy_to_CEX(self):
        '''Конечная цена при переплате на 40%'''

        total_sum = 0.
        for stock in TOKEN["CEX"]:
            total_sum += float(TOKEN["CEX"][stock]["volume"])
        
        result_cost = 0
        for stock in TOKEN["CEX"]:
            coef_prior = (float(TOKEN["CEX"][stock]["volume"])) / total_sum
            result_cost += coef_prior * self.ideal_price("CEX")
        
        # Уменьшаем на 40%
        result_cost = (result_cost * 140) / 100.

        return result_cost
        
    def sell_to_DEX(self):
        '''Конечная цена при продаже на DEX.
        
        Определяется с помощью готового инструмента.
        
        '''

        pass
    
    def buy_to_DEX(self):
        pass

    def __calc_end_cost(self, stock):
        '''Функция подсчитывает конечную цену проданных токенов на бирже'''
         
        pass

    def __num_tokens_to_sale(self, stock):
        '''Количество токенов к продаже на конкретной бирже'''

        pass


