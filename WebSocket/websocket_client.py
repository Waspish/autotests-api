import websockets

import asyncio

async def client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        message = "Привет сервер"
        print(f'Отправка {message}')
        await websocket.send(message)

        for _ in range(5):
            response = await websocket.recv()
            print(f'Ответ от сервера: {response}')

asyncio.run(client())