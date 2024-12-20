import grpc
from concurrent import futures
from generated_code import api__pb2, api_pb2_grpc

class ApiServicer(api_pb2_grpc.ApiServicer):
    def ApiEndpoint(self, request, context):
        return api__pb2.ApiResponse(resp="Hello {}".format(request.userName));

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    api_pb2_grpc.add_ApiServicer_to_server(
        ApiServicer(), server)
    server.add_insecure_port('[::]:7073')
    server.start()
    print("server started on port 7073 ...")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()