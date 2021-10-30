'''docstrings'''
import asyncio
import json
import time
import matplotlib.pyplot as plt
import websockets

X_DATA = []
Y_DATA = []
X_STEPS = 0

'''Строим график'''
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

def update_graph():
    '''Функция обновления графика'''
    global X_STEPS
    X_STEPS += 1
    if X_STEPS > 6:
        ax.set_xlim((X_STEPS-6), 5 + (X_STEPS-6))
    ax.plot(X_DATA, Y_DATA, color='g')
    fig.canvas.draw()
    plt.pause(0.1)

async def main():
    '''Главная ассинхронная функция.

    Благодаря модулю websockets мы один раз подключаемся
    к сайту по api и парсим с помощью json время и цену
    биткоина каждую секунду.

    '''

    url = "wss://stream.binance.com:9443/stream?streams=btcusdt@miniTicker"
    async with websockets.connect(url) as client:
        while True:
            data = json.loads(await client.recv())['data']
            event_time = time.localtime(data['E'] // 1000)
            event_time = f"{event_time.tm_hour}:{event_time.tm_min}:{event_time.tm_sec}"

            print(event_time, "->", data['c'])

            X_DATA.append(event_time)
            Y_DATA.append(int(float(data['c'])))
            update_graph()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())