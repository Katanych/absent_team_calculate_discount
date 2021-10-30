'''Место для импортирования модулей'''


class Crypto_calc(object):
    '''Класс крипто-калькулятора'''

    def __init__(self, token, num_tokens, token_to_exch):
        self.token = token
        self.num_tokens = num_tokens
        self.token_to_exch = token_to_exch

    def price_p2p(self):
        '''Цена peer-to-peer сделки для продающего'''

        pass

    def discount_amount(self):
        '''Размер скидки для покупателя'''
        
        pass

    def price_token(self):
        '''Цена токена'''

        pass

    def get_price_new_tokens_after_exch_on_CEX(self):
        '''Функция возвращает стоимость новых токенов'''
        pass


    def __convert_on_CEX(self, stocks=['Binance'], ):
        '''Функция возвращает стоимость токена, на который обменяли.
        
        Количество валют, которые мы получим при продаже
        набора токенов на одной централизованной бирже CEX
        за один вечер.
        
        '''

        sum = 0
        for stock in stocks:
            sum += self.__calc_end_cost(stock)
            
        return sum

    def __calc_end_cost(self, stock):
        '''Функция подсчитывает конечную цену проданных токенов.

        Функция подсчитывает, сколько валюты мы получим, если
        продадим N токенов на бирже B. 
        
        '''

        pass

    def __num_tokens_to_sale_on_CEX(self, stock):
        '''Количество токенов к продаже на бирже'''

        pass


