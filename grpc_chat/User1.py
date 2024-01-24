from threading import Thread
import grpc
import chat_pb2
import chat_pb2_grpc


class Chat:
    def __init__(self, stub, user) -> None:
        self._stub = stub
        self._chat = Thread(target=self._listen, daemon=True).start()
        self.user = user

    def _listen(self):
        while 1:
            message = self._stub.receive_message(chat_pb2.Empty())
            print(f"[{message.username}] {message.message}")

    def send_message(self, message):
        self._stub.send_message(
            chat_pb2.ChatMessage(
                username=self.user.username,
                message=message,
            )
        )

class User:
    def __init__(self, username, stub) -> None:
        self.username = username
        self._stub = stub
        self._thread = Thread(target=self._send_message, daemon=True).start()

    def _send_message(self):
        while True:
            message = input(f"[{self.username}] ")
            self._stub.send_message(
                chat_pb2.ChatMessage(
                    username=self.username,
                    message=message,
                )
            )

def run():
    username = input("Escolha um username ")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = chat_pb2_grpc.ChatStub(channel)
        response = stub.connect(chat_pb2.ChatUser(username=username))
        client = User(response.username, stub)
        chat = Chat(stub, client)

        while True:
            message = input("")
            chat.send_message(message)

if __name__ == "__main__":
    run()
