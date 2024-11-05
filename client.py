import grpc
from generated_code import api_pb2_grpc, api__pb2

def main():
    channel = grpc.insecure_channel('localhost:7073')
    stub = api_pb2_grpc.ApiStub(channel)
    response = stub.ApiEndpoint(api__pb2.ApiRequest(userName="Arman"))
    print(response)

if __name__ == "__main__":
    main()