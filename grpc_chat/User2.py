from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import grpc
import chat_pb2
import chat_pb2_grpc


class ChatService(chat_pb2_grpc.ChatServicer):
    def __init__(self, username, client_stub) -> None:
        super().__init__()
        self.username = username
        self.client_stub = client_stub
        Thread(target=self._listen, daemon=True).start()

    def connect(self, request, context):
        return chat_pb2.ChatUser(username=request.username)

    def send_message(self, request, context):
        print(f"[{request.username}] {request.message}")
        return chat_pb2.Empty()

    def receive_message(self, request, context):
        message = input("")
        return chat_pb2.ChatMessage(
            username=self.username,
            message=message,
        )

    def _listen(self):
        while 1:
            message = self.client_stub.receive_message(chat_pb2.Empty())
            print(f"{message.username}: {message.message}")

def serve(port):
    with grpc.insecure_channel(f"localhost:{port}") as client_channel:
        client_stub = chat_pb2_grpc.ChatStub(client_channel)

        server = grpc.server(ThreadPoolExecutor(max_workers=10))
        username = input("Escolha um username ")
        chat_pb2_grpc.add_ChatServicer_to_server(ChatService(username, client_stub), server)

        server.add_insecure_port(f"[::]:{port}")
        server.start()
        server.wait_for_termination()

if __name__ == "__main__":
    port = 50051
    print(f"Server is running on [::]:{port}")
    serve(port)
