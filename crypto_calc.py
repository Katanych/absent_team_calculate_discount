'''Место для импортирования модулей'''
from datasets import *


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
        self.token_info = self.__get_token_info(CEXS, DEXS, SPECIFICS, DATA_CEX)
        self.end_price_token = None
    
    def get_token(self):
        return self.token
    
    def get_num_tokens(self):
        return self.num_tokens

    def get_token2(self):
        return self.token2
    
    def get_token_info(self):
        return self.token_info
    
    def get_end_price_token(self):
        return self.token_end_price

    def __get_token_info(self, cexs, dexs, specifics, data):
        '''Функция составляет полную информацию о токене'''

        token = dict()
        token["CEX"] = dict()
        for i, CEX in enumerate(cexs):
            token["CEX"][CEX] = dict()
            for j, spec in enumerate(specifics):
                token["CEX"][CEX][spec] = data[i][j]
        # token["DEX"] = dict()
        # for DEX in dexs:
        #     token["DEX"][DEX] = dict()
        #     for spec in specifics:
        #         token["DEX"][DEX][spec] = data[i]
        #         i += 1
        return token

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
    
    def ideal_price(self, type_stock):
        '''Функция идеальной цены, если бы мы продали по курсу.
        
        Определяем максимальную возможную цену, исходя из
        курса (средней цены продаж) на бирже.
        
        '''

        max_price = 0
        for stock in self.token_info[type_stock]:
            if float(self.token_info[type_stock][stock]["price"]) > max_price:
                max_price = float(self.token_info[type_stock][stock]["price"])
        
        return float(max_price) * self.num_tokens

    def sell_to_CEX(self, procent_lose=None):
        '''Конечная цена при потери в 40% на CEX.
        
        Здесь будет описан алгоритм получения сконвертированной цены
        для CEXs

        '''

        total_sum = 0.
        for stock in self.token_info["CEX"]:
            total_sum += float(self.token_info["CEX"][stock]["volume"])
        
        result_cost = 0
        coefs_prior = []
        for stock in self.token_info["CEX"]:
            coef_prior = (float(self.token_info["CEX"][stock]["volume"])) / total_sum
            coefs_prior.append(coef_prior)
            result_cost += coef_prior * self.ideal_price("CEX")
        
        if procent_lose is None:
            result_cost = 0
            for coef, stock in enumerate(self.token_info["CEX"]):
                cost = 0
                num_to_sale = self.num_tokens * coefs_prior[coef]
                num_cup = int(num_to_sale // self.token_info["CEX"][stock]["num_tokens"] + 1)
                num_offer_on_cup = num_to_sale / num_cup
                print(self.token_info["CEX"][stock]["price_max"])
                price_max = float(self.token_info["CEX"][stock]["price_max"])
                price_min = float(self.token_info["CEX"][stock]["price_min"])
                mid_price = (price_max + price_min) / 2
                delta = price_max - price_min
                for i in range(num_cup):
                    cost += mid_price * num_offer_on_cup
                    mid_price -= delta
                self.token_end_price = mid_price
                result_cost += cost * coefs_prior[coef]
        else:
            # Уменьшаем на 40%
            result_cost = (result_cost * 140) / 100.

        return result_cost
    
    def buy_to_CEX(self, procent_lose=None):
        '''Конечная цена при переплате на 40%'''

        total_sum = 0.
        for stock in self.token_info["CEX"]:
            total_sum += float(self.token_info["CEX"][stock]["volume"])
        
        result_cost = 0
        for stock in self.token_info["CEX"]:
            coef_prior = (float(self.token_info["CEX"][stock]["volume"])) / total_sum
            result_cost += coef_prior * self.ideal_price("CEX")
        


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


