import asyncio
import websockets

async def client():
    uri = 'ws://localhost:8000'
    async with websockets.connect(uri) as websocket:
        message = 'Hello server!'
        print(f'Send message {message}')
        await websocket.send(message)
        
        response = await websocket.recv()
        print(f'Server get message {response}')
        
        
asyncio.run(client())