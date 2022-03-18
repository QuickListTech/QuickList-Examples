#!/usr/bin/python

import asyncio
import pathlib
import ssl
import websockets

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.load_default_certs()
ssl_context.load_cert_chain(
    pathlib.Path("crypto/client/clientC.cert.pem"),
    pathlib.Path("crypto/client/clientC.key.pem"))

async def testClient():
    uri = "wss://192.168.1.242:8080"
    async with websockets.connect(uri, ssl=ssl_context) as websocket:
        await websocket.send('{"Event" : "SubscribeStream", "ReqID" : 1}')

        while True:
            r = await websocket.recv()
            print(f"response {r}")



if __name__ == "__main__":
    asyncio.run(testClient())
