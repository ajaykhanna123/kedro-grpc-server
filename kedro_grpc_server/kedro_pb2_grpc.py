# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from kedro_grpc_server import kedro_pb2 as kedro__grpc__server_dot_kedro__pb2


class KedroStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListPipelines = channel.unary_unary(
                '/kedro.Kedro/ListPipelines',
                request_serializer=kedro__grpc__server_dot_kedro__pb2.PipelineParams.SerializeToString,
                response_deserializer=kedro__grpc__server_dot_kedro__pb2.PipelineSummary.FromString,
                )
        self.Run = channel.unary_unary(
                '/kedro.Kedro/Run',
                request_serializer=kedro__grpc__server_dot_kedro__pb2.RunParams.SerializeToString,
                response_deserializer=kedro__grpc__server_dot_kedro__pb2.RunSummary.FromString,
                )
        self.Status = channel.unary_stream(
                '/kedro.Kedro/Status',
                request_serializer=kedro__grpc__server_dot_kedro__pb2.RunId.SerializeToString,
                response_deserializer=kedro__grpc__server_dot_kedro__pb2.RunStatus.FromString,
                )


class KedroServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListPipelines(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Run(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KedroServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListPipelines': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPipelines,
                    request_deserializer=kedro__grpc__server_dot_kedro__pb2.PipelineParams.FromString,
                    response_serializer=kedro__grpc__server_dot_kedro__pb2.PipelineSummary.SerializeToString,
            ),
            'Run': grpc.unary_unary_rpc_method_handler(
                    servicer.Run,
                    request_deserializer=kedro__grpc__server_dot_kedro__pb2.RunParams.FromString,
                    response_serializer=kedro__grpc__server_dot_kedro__pb2.RunSummary.SerializeToString,
            ),
            'Status': grpc.unary_stream_rpc_method_handler(
                    servicer.Status,
                    request_deserializer=kedro__grpc__server_dot_kedro__pb2.RunId.FromString,
                    response_serializer=kedro__grpc__server_dot_kedro__pb2.RunStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kedro.Kedro', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Kedro(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListPipelines(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kedro.Kedro/ListPipelines',
            kedro__grpc__server_dot_kedro__pb2.PipelineParams.SerializeToString,
            kedro__grpc__server_dot_kedro__pb2.PipelineSummary.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Run(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kedro.Kedro/Run',
            kedro__grpc__server_dot_kedro__pb2.RunParams.SerializeToString,
            kedro__grpc__server_dot_kedro__pb2.RunSummary.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/kedro.Kedro/Status',
            kedro__grpc__server_dot_kedro__pb2.RunId.SerializeToString,
            kedro__grpc__server_dot_kedro__pb2.RunStatus.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
