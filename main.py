from calculate_discount import *
from crypto_calc import Crypto_calc


TOKEN = "BAT"           # Токен, которые планируется продать
NUM_TOKENS = 5000000    # 5 млн токенов к продаже
TOKEN_TO_EXCH = "BTC"   # Токен, на который будем менять

def main():
    calc = Crypto_calc(TOKEN, NUM_TOKENS, TOKEN_TO_EXCH)
    discont = calc.discount_amount()
    end_price_p2p = calc.price_p2p()
    end_price_token = calc.price_token()
    print("Размер скидки для покупателя:", discont, \
        "\nКонечная цена peer-to-peer сделки:", end_price_p2p, \
            "\nКонечная цена токена:", end_price_token)

if __name__ == '__main__':
    main()