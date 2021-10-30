'''Место для импортирования модулей'''


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

    def price_p2p(self):
        '''Цена peer-to-peer сделки для продающего'''

        pass

    def discount_amount(self):
        '''Размер скидки для покупателя'''
        
        pass

    def price_token(self):
        '''Цена токена'''

        pass

    def get_converted_price(self):
        '''Функция возвращает стоимость новых токенов на CEX
        
        Функция возвращает общую стоимость токенов, на которую был
        соврешен обмен (token2)
        
        '''

        pass

    def convert_price(self, stocks=['Binance'], ):
        '''Функция возвращает стоимость токенов, на который обменяли.
        
        Количество валют, которые мы получим при продаже
        набора токенов на нескольких централизованных биржах CEX 
        (stocks) за один вечер.
        
        '''

        sum = 0
        for stock in stocks:
            # Суммируем стоимость, полученную с каждой биржи 
            sum += self.__calc_end_cost(stock)
            
        return sum

    def __calc_end_cost(self, stock):
        '''Функция подсчитывает конечную цену проданных токенов на бирже'''
        
        pass

    def __num_tokens_to_sale(self, stock):
        '''Количество токенов к продаже на конкретной бирже'''

        pass


