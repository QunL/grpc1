# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import msg_pb2 as msg__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in msg_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class RPCStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MsgStream = channel.stream_stream(
                '/protolq.RPC/MsgStream',
                request_serializer=msg__pb2.CommonMsg.SerializeToString,
                response_deserializer=msg__pb2.CommonMsg.FromString,
                _registered_method=True)


class RPCServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MsgStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MsgStream': grpc.stream_stream_rpc_method_handler(
                    servicer.MsgStream,
                    request_deserializer=msg__pb2.CommonMsg.FromString,
                    response_serializer=msg__pb2.CommonMsg.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protolq.RPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('protolq.RPC', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RPC(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MsgStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/protolq.RPC/MsgStream',
            msg__pb2.CommonMsg.SerializeToString,
            msg__pb2.CommonMsg.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
