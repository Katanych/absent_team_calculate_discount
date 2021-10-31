'''Подключение модулей для парсинга с API'''

CEXS = ["Binance", "Gate.io"]
DEXS = {
    "1inch": 4551334, 
    "Uniswap": 2510763,
    }
SPECIFICS = ["price", "volume", "price_max", "price_min", "num_tokens"]
# DATA_CEX = [[0.75, 126000000, 0.85, 0.65, 1000000], \
#     [0.76, 2600000, 0.9, 0.65, 100000]]            # переменная дата должна иметь формат: price, volume
DATA_CEX = [
    [1.175, 558071574, 1.275, 1.075, 514240],
    [1.17, 9449879, 1.198, 1.143, 104425],
]
# DATA_DEX = [4551334, 2510763]

TOKENS2 = ["USDT", "BTC"]
VALUES_RATE = {
    "BTC": 0.5,
    "BUSD": 0.8,
    "USDT": 1,
}
