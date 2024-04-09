# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: gateway.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from datetime import datetime
from typing import (
    TYPE_CHECKING,
    AsyncIterable,
    AsyncIterator,
    Dict,
    Iterable,
    List,
    Optional,
    Union,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class AuthorizeRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class AuthorizeResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    workspace_id: str = betterproto.string_field(2)
    new_token: str = betterproto.string_field(3)
    error_msg: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class ObjectMetadata(betterproto.Message):
    name: str = betterproto.string_field(1)
    size: int = betterproto.int64_field(2)


@dataclass(eq=False, repr=False)
class HeadObjectRequest(betterproto.Message):
    hash: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class HeadObjectResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    exists: bool = betterproto.bool_field(2)
    object_id: str = betterproto.string_field(3)
    object_metadata: "ObjectMetadata" = betterproto.message_field(4)
    error_msg: str = betterproto.string_field(5)


@dataclass(eq=False, repr=False)
class PutObjectRequest(betterproto.Message):
    object_content: bytes = betterproto.bytes_field(1)
    object_metadata: "ObjectMetadata" = betterproto.message_field(2)
    hash: str = betterproto.string_field(3)
    overwrite: bool = betterproto.bool_field(4)


@dataclass(eq=False, repr=False)
class PutObjectResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    object_id: str = betterproto.string_field(2)
    error_msg: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class StartTaskRequest(betterproto.Message):
    """Task queue messages"""

    task_id: str = betterproto.string_field(1)
    container_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class StartTaskResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)


@dataclass(eq=False, repr=False)
class EndTaskRequest(betterproto.Message):
    task_id: str = betterproto.string_field(1)
    task_duration: float = betterproto.float_field(2)
    task_status: str = betterproto.string_field(3)
    container_id: str = betterproto.string_field(4)
    container_hostname: str = betterproto.string_field(5)
    keep_warm_seconds: float = betterproto.float_field(6)


@dataclass(eq=False, repr=False)
class EndTaskResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)


@dataclass(eq=False, repr=False)
class StringList(betterproto.Message):
    values: List[str] = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ListTasksRequest(betterproto.Message):
    filters: Dict[str, "StringList"] = betterproto.map_field(
        1, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )
    limit: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class Task(betterproto.Message):
    id: str = betterproto.string_field(2)
    status: str = betterproto.string_field(3)
    container_id: str = betterproto.string_field(4)
    started_at: datetime = betterproto.message_field(5)
    ended_at: datetime = betterproto.message_field(6)
    stub_id: str = betterproto.string_field(7)
    stub_name: str = betterproto.string_field(8)
    workspace_id: str = betterproto.string_field(9)
    workspace_name: str = betterproto.string_field(10)
    created_at: datetime = betterproto.message_field(11)
    updated_at: datetime = betterproto.message_field(12)


@dataclass(eq=False, repr=False)
class ListTasksResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    err_msg: str = betterproto.string_field(2)
    tasks: List["Task"] = betterproto.message_field(3)
    total: int = betterproto.int32_field(4)


@dataclass(eq=False, repr=False)
class StopTaskRequest(betterproto.Message):
    task_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class StopTaskResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    err_msg: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class Volume(betterproto.Message):
    id: str = betterproto.string_field(1)
    mount_path: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class GetOrCreateStubRequest(betterproto.Message):
    object_id: str = betterproto.string_field(1)
    image_id: str = betterproto.string_field(2)
    stub_type: str = betterproto.string_field(3)
    name: str = betterproto.string_field(4)
    python_version: str = betterproto.string_field(5)
    cpu: int = betterproto.int64_field(6)
    memory: int = betterproto.int64_field(7)
    gpu: str = betterproto.string_field(8)
    handler: str = betterproto.string_field(9)
    retries: int = betterproto.uint32_field(10)
    timeout: int = betterproto.int64_field(11)
    keep_warm_seconds: float = betterproto.float_field(12)
    concurrency: int = betterproto.uint32_field(13)
    max_containers: int = betterproto.uint32_field(14)
    max_pending_tasks: int = betterproto.uint32_field(15)
    volumes: List["Volume"] = betterproto.message_field(16)
    force_create: bool = betterproto.bool_field(17)


@dataclass(eq=False, repr=False)
class GetOrCreateStubResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    stub_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class DeployStubRequest(betterproto.Message):
    stub_id: str = betterproto.string_field(1)
    name: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class DeployStubResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    deployment_id: str = betterproto.string_field(2)
    version: int = betterproto.uint32_field(3)


class GatewayServiceStub(betterproto.ServiceStub):
    async def authorize(
        self,
        authorize_request: "AuthorizeRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "AuthorizeResponse":
        return await self._unary_unary(
            "/gateway.GatewayService/Authorize",
            authorize_request,
            AuthorizeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def head_object(
        self,
        head_object_request: "HeadObjectRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "HeadObjectResponse":
        return await self._unary_unary(
            "/gateway.GatewayService/HeadObject",
            head_object_request,
            HeadObjectResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def put_object(
        self,
        put_object_request: "PutObjectRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "PutObjectResponse":
        return await self._unary_unary(
            "/gateway.GatewayService/PutObject",
            put_object_request,
            PutObjectResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def put_object_stream(
        self,
        put_object_request_iterator: Union[
            AsyncIterable["PutObjectRequest"], Iterable["PutObjectRequest"]
        ],
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "PutObjectResponse":
        return await self._stream_unary(
            "/gateway.GatewayService/PutObjectStream",
            put_object_request_iterator,
            PutObjectRequest,
            PutObjectResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def start_task(
        self,
        start_task_request: "StartTaskRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "StartTaskResponse":
        return await self._unary_unary(
            "/gateway.GatewayService/StartTask",
            start_task_request,
            StartTaskResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def end_task(
        self,
        end_task_request: "EndTaskRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "EndTaskResponse":
        return await self._unary_unary(
            "/gateway.GatewayService/EndTask",
            end_task_request,
            EndTaskResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def stop_task(
        self,
        stop_task_request: "StopTaskRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "StopTaskResponse":
        return await self._unary_unary(
            "/gateway.GatewayService/StopTask",
            stop_task_request,
            StopTaskResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def list_tasks(
        self,
        list_tasks_request: "ListTasksRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "ListTasksResponse":
        return await self._unary_unary(
            "/gateway.GatewayService/ListTasks",
            list_tasks_request,
            ListTasksResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_or_create_stub(
        self,
        get_or_create_stub_request: "GetOrCreateStubRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "GetOrCreateStubResponse":
        return await self._unary_unary(
            "/gateway.GatewayService/GetOrCreateStub",
            get_or_create_stub_request,
            GetOrCreateStubResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def deploy_stub(
        self,
        deploy_stub_request: "DeployStubRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "DeployStubResponse":
        return await self._unary_unary(
            "/gateway.GatewayService/DeployStub",
            deploy_stub_request,
            DeployStubResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class GatewayServiceBase(ServiceBase):
    async def authorize(
        self, authorize_request: "AuthorizeRequest"
    ) -> "AuthorizeResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def head_object(
        self, head_object_request: "HeadObjectRequest"
    ) -> "HeadObjectResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def put_object(
        self, put_object_request: "PutObjectRequest"
    ) -> "PutObjectResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def put_object_stream(
        self, put_object_request_iterator: AsyncIterator["PutObjectRequest"]
    ) -> "PutObjectResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def start_task(
        self, start_task_request: "StartTaskRequest"
    ) -> "StartTaskResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def end_task(self, end_task_request: "EndTaskRequest") -> "EndTaskResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def stop_task(
        self, stop_task_request: "StopTaskRequest"
    ) -> "StopTaskResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def list_tasks(
        self, list_tasks_request: "ListTasksRequest"
    ) -> "ListTasksResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_or_create_stub(
        self, get_or_create_stub_request: "GetOrCreateStubRequest"
    ) -> "GetOrCreateStubResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def deploy_stub(
        self, deploy_stub_request: "DeployStubRequest"
    ) -> "DeployStubResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_authorize(
        self, stream: "grpclib.server.Stream[AuthorizeRequest, AuthorizeResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.authorize(request)
        await stream.send_message(response)

    async def __rpc_head_object(
        self, stream: "grpclib.server.Stream[HeadObjectRequest, HeadObjectResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.head_object(request)
        await stream.send_message(response)

    async def __rpc_put_object(
        self, stream: "grpclib.server.Stream[PutObjectRequest, PutObjectResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.put_object(request)
        await stream.send_message(response)

    async def __rpc_put_object_stream(
        self, stream: "grpclib.server.Stream[PutObjectRequest, PutObjectResponse]"
    ) -> None:
        request = stream.__aiter__()
        response = await self.put_object_stream(request)
        await stream.send_message(response)

    async def __rpc_start_task(
        self, stream: "grpclib.server.Stream[StartTaskRequest, StartTaskResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.start_task(request)
        await stream.send_message(response)

    async def __rpc_end_task(
        self, stream: "grpclib.server.Stream[EndTaskRequest, EndTaskResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.end_task(request)
        await stream.send_message(response)

    async def __rpc_stop_task(
        self, stream: "grpclib.server.Stream[StopTaskRequest, StopTaskResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.stop_task(request)
        await stream.send_message(response)

    async def __rpc_list_tasks(
        self, stream: "grpclib.server.Stream[ListTasksRequest, ListTasksResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.list_tasks(request)
        await stream.send_message(response)

    async def __rpc_get_or_create_stub(
        self,
        stream: "grpclib.server.Stream[GetOrCreateStubRequest, GetOrCreateStubResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_or_create_stub(request)
        await stream.send_message(response)

    async def __rpc_deploy_stub(
        self, stream: "grpclib.server.Stream[DeployStubRequest, DeployStubResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.deploy_stub(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/gateway.GatewayService/Authorize": grpclib.const.Handler(
                self.__rpc_authorize,
                grpclib.const.Cardinality.UNARY_UNARY,
                AuthorizeRequest,
                AuthorizeResponse,
            ),
            "/gateway.GatewayService/HeadObject": grpclib.const.Handler(
                self.__rpc_head_object,
                grpclib.const.Cardinality.UNARY_UNARY,
                HeadObjectRequest,
                HeadObjectResponse,
            ),
            "/gateway.GatewayService/PutObject": grpclib.const.Handler(
                self.__rpc_put_object,
                grpclib.const.Cardinality.UNARY_UNARY,
                PutObjectRequest,
                PutObjectResponse,
            ),
            "/gateway.GatewayService/PutObjectStream": grpclib.const.Handler(
                self.__rpc_put_object_stream,
                grpclib.const.Cardinality.STREAM_UNARY,
                PutObjectRequest,
                PutObjectResponse,
            ),
            "/gateway.GatewayService/StartTask": grpclib.const.Handler(
                self.__rpc_start_task,
                grpclib.const.Cardinality.UNARY_UNARY,
                StartTaskRequest,
                StartTaskResponse,
            ),
            "/gateway.GatewayService/EndTask": grpclib.const.Handler(
                self.__rpc_end_task,
                grpclib.const.Cardinality.UNARY_UNARY,
                EndTaskRequest,
                EndTaskResponse,
            ),
            "/gateway.GatewayService/StopTask": grpclib.const.Handler(
                self.__rpc_stop_task,
                grpclib.const.Cardinality.UNARY_UNARY,
                StopTaskRequest,
                StopTaskResponse,
            ),
            "/gateway.GatewayService/ListTasks": grpclib.const.Handler(
                self.__rpc_list_tasks,
                grpclib.const.Cardinality.UNARY_UNARY,
                ListTasksRequest,
                ListTasksResponse,
            ),
            "/gateway.GatewayService/GetOrCreateStub": grpclib.const.Handler(
                self.__rpc_get_or_create_stub,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetOrCreateStubRequest,
                GetOrCreateStubResponse,
            ),
            "/gateway.GatewayService/DeployStub": grpclib.const.Handler(
                self.__rpc_deploy_stub,
                grpclib.const.Cardinality.UNARY_UNARY,
                DeployStubRequest,
                DeployStubResponse,
            ),
        }
