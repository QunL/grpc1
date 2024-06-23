

import grpc
import msg_pb2
import msg_pb2_grpc

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = msg_pb2_grpc.RPCStub(channel)

    req1 = msg_pb2.Req1(data1="request")
    msg = msg_pb2.CommonMsg(req1=req1)
    msg_stream = [msg,]
    resp_stream = stub.MsgStream(iter(msg_stream))
    print("resp:", resp_stream)
    for resp in resp_stream:
        print("resp:", resp.data1)


if __name__ == "__main__":
    main()
