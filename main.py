from crypto_calc import Crypto_calc


TOKEN = "BAT"           # Токен, которые планируется продать
NUM_TOKENS = 5000000    # 5 млн токенов к продаже
TOKEN_TO_EXCH = "USDT"   # Токен, на который будем менять

def main():
    calc = Crypto_calc(TOKEN, NUM_TOKENS, TOKEN_TO_EXCH)
    discont, end_price_p2p, end_price_token = calc.calculate_result()
    calc.show_analitic()

if __name__ == '__main__':
    main()