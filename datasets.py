'''Подключение модулей для парсинга с API'''

CEXS = ["Binance", "FTX"]
DEXS = ["1inch", "Uniswap"]
SPECIFICS = ["price", "volume", "price_max", "price_min", "num_tokens"]
DATA_CEX = [[0.75, 126000000, 0.85, 0.65, 1000000], \
    [0.76, 2600000, 0.9, 0.65, 100000]]            # переменная дата должна иметь формат: price, volume
DATA_DEX = []
TOKENS2 = ["USDT", "BTC"]
