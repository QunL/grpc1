from concurrent import futures
import grpc
import msg_pb2_grpc
import msg_pb2
import traceback

class Greeter(msg_pb2_grpc.RPCServicer):
    def MsgStream(self, request_iterator, context):
        for request in request_iterator:
            print("request:", request)
            try:
                msg = msg_pb2.Resp1(data1=str(request))
                msg2 = msg_pb2.CommonMsg(resp1=msg)
                print("send resp:", msg2)
                yield msg2
            except:
                print("except:", traceback.format_exc())

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    msg_pb2_grpc.add_RPCServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
