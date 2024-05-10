import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class TicTacToeConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'room_' + self.room_name

        # join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        print("Disconnected")
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None):
        """
        Receive message from WebSocket.
        Get the event and send the appropriate event
        """
        response = json.loads(text_data)
        event = response.get("event")
        message = response.get("message")
        if event == "MOVE":
            # send message to room group
            await self.channel_layer.group_send(
                self.room_group_name, {
                    "type": "send_message",
                    "message": message,
                    "event": "MOVE",
                }
            )
        elif event == "START":
            # send message to room group
            await self.channel_layer.group_send(
                self.room_group_name, {
                    "type": "send_message",
                    "message": message,
                    "event": "START",
                }
            )
        elif event == "END":
            # send message to room group
            await self.channel_layer.group_send(
                self.room_group_name, {
                    "type": "send_message",
                    "message": message,
                    "event": "END",
                }
            )
    async def send_message(self, res):
        """Receive message from room group"""
        # send message to websocket
        await self.send(text_data=json.dumps({
            "payload": res,
        }))
