# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: gateway.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional

import betterproto
import grpclib


@dataclass
class AuthorizeRequest(betterproto.Message):
    pass


@dataclass
class AuthorizeResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    workspace_id: str = betterproto.string_field(2)
    new_token: str = betterproto.string_field(3)
    error_msg: str = betterproto.string_field(4)


@dataclass
class ObjectMetadata(betterproto.Message):
    name: str = betterproto.string_field(1)
    size: int = betterproto.int64_field(2)


@dataclass
class HeadObjectRequest(betterproto.Message):
    hash: str = betterproto.string_field(1)


@dataclass
class HeadObjectResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    exists: bool = betterproto.bool_field(2)
    object_id: str = betterproto.string_field(3)
    object_metadata: "ObjectMetadata" = betterproto.message_field(4)
    error_msg: str = betterproto.string_field(5)


@dataclass
class PutObjectRequest(betterproto.Message):
    object_content: bytes = betterproto.bytes_field(1)
    object_metadata: "ObjectMetadata" = betterproto.message_field(2)
    hash: str = betterproto.string_field(3)
    overwrite: bool = betterproto.bool_field(4)


@dataclass
class PutObjectResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    object_id: str = betterproto.string_field(2)
    error_msg: str = betterproto.string_field(3)


@dataclass
class StartTaskRequest(betterproto.Message):
    """Task queue messages"""

    task_id: str = betterproto.string_field(1)
    container_id: str = betterproto.string_field(2)


@dataclass
class StartTaskResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)


@dataclass
class EndTaskRequest(betterproto.Message):
    task_id: str = betterproto.string_field(1)
    task_duration: float = betterproto.float_field(2)
    task_status: str = betterproto.string_field(3)
    container_id: str = betterproto.string_field(4)
    container_hostname: str = betterproto.string_field(5)
    scale_down_delay: float = betterproto.float_field(6)


@dataclass
class EndTaskResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)


@dataclass
class StringList(betterproto.Message):
    values: List[str] = betterproto.string_field(1)


@dataclass
class ListTasksRequest(betterproto.Message):
    filters: Dict[str, "StringList"] = betterproto.map_field(
        1, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )
    limit: int = betterproto.uint32_field(2)


@dataclass
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


@dataclass
class ListTasksResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    err_msg: str = betterproto.string_field(2)
    tasks: List["Task"] = betterproto.message_field(3)
    total: int = betterproto.int32_field(4)


@dataclass
class StopTaskRequest(betterproto.Message):
    task_id: str = betterproto.string_field(1)


@dataclass
class StopTaskResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    err_msg: str = betterproto.string_field(2)


@dataclass
class Volume(betterproto.Message):
    id: str = betterproto.string_field(1)
    mount_path: str = betterproto.string_field(2)


@dataclass
class GetOrCreateStubRequest(betterproto.Message):
    object_id: str = betterproto.string_field(1)
    image_id: str = betterproto.string_field(2)
    stub_type: str = betterproto.string_field(3)
    name: str = betterproto.string_field(4)
    python_version: str = betterproto.string_field(5)
    cpu: int = betterproto.int64_field(6)
    memory: int = betterproto.int64_field(7)
    gpu: str = betterproto.string_field(8)
    volumes: List["Volume"] = betterproto.message_field(9)


@dataclass
class GetOrCreateStubResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    stub_id: str = betterproto.string_field(2)


class GatewayServiceStub(betterproto.ServiceStub):
    async def authorize(self) -> AuthorizeResponse:
        request = AuthorizeRequest()

        return await self._unary_unary(
            "/gateway.GatewayService/Authorize",
            request,
            AuthorizeResponse,
        )

    async def head_object(self, *, hash: str = "") -> HeadObjectResponse:
        request = HeadObjectRequest()
        request.hash = hash

        return await self._unary_unary(
            "/gateway.GatewayService/HeadObject",
            request,
            HeadObjectResponse,
        )

    async def put_object(
        self,
        *,
        object_content: bytes = b"",
        object_metadata: Optional["ObjectMetadata"] = None,
        hash: str = "",
        overwrite: bool = False,
    ) -> PutObjectResponse:
        request = PutObjectRequest()
        request.object_content = object_content
        if object_metadata is not None:
            request.object_metadata = object_metadata
        request.hash = hash
        request.overwrite = overwrite

        return await self._unary_unary(
            "/gateway.GatewayService/PutObject",
            request,
            PutObjectResponse,
        )

    async def start_task(
        self, *, task_id: str = "", container_id: str = ""
    ) -> StartTaskResponse:
        request = StartTaskRequest()
        request.task_id = task_id
        request.container_id = container_id

        return await self._unary_unary(
            "/gateway.GatewayService/StartTask",
            request,
            StartTaskResponse,
        )

    async def end_task(
        self,
        *,
        task_id: str = "",
        task_duration: float = 0,
        task_status: str = "",
        container_id: str = "",
        container_hostname: str = "",
        scale_down_delay: float = 0,
    ) -> EndTaskResponse:
        request = EndTaskRequest()
        request.task_id = task_id
        request.task_duration = task_duration
        request.task_status = task_status
        request.container_id = container_id
        request.container_hostname = container_hostname
        request.scale_down_delay = scale_down_delay

        return await self._unary_unary(
            "/gateway.GatewayService/EndTask",
            request,
            EndTaskResponse,
        )

    async def stop_task(self, *, task_id: str = "") -> StopTaskResponse:
        request = StopTaskRequest()
        request.task_id = task_id

        return await self._unary_unary(
            "/gateway.GatewayService/StopTask",
            request,
            StopTaskResponse,
        )

    async def list_tasks(
        self, *, filters: Optional[Dict[str, "StringList"]] = None, limit: int = 0
    ) -> ListTasksResponse:
        request = ListTasksRequest()
        request.filters = filters
        request.limit = limit

        return await self._unary_unary(
            "/gateway.GatewayService/ListTasks",
            request,
            ListTasksResponse,
        )

    async def get_or_create_stub(
        self,
        *,
        object_id: str = "",
        image_id: str = "",
        stub_type: str = "",
        name: str = "",
        python_version: str = "",
        cpu: int = 0,
        memory: int = 0,
        gpu: str = "",
        volumes: List["Volume"] = [],
    ) -> GetOrCreateStubResponse:
        request = GetOrCreateStubRequest()
        request.object_id = object_id
        request.image_id = image_id
        request.stub_type = stub_type
        request.name = name
        request.python_version = python_version
        request.cpu = cpu
        request.memory = memory
        request.gpu = gpu
        if volumes is not None:
            request.volumes = volumes

        return await self._unary_unary(
            "/gateway.GatewayService/GetOrCreateStub",
            request,
            GetOrCreateStubResponse,
        )
