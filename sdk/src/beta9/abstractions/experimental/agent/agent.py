from typing import Callable, List, Optional, Union

from beta9.abstractions.base.runner import RunnerAbstraction
from beta9.abstractions.image import Image
from beta9.abstractions.volume import Volume
from beta9.type import GpuType, GpuTypeAlias


class Agent(RunnerAbstraction):
    def __init__(
        self,
        cpu: Union[int, float, str] = 1.0,
        memory: Union[int, str] = 128,
        gpu: GpuTypeAlias = GpuType.NoGPU,
        image: Image = Image(),
        timeout: int = 180,
        workers: int = 1,
        keep_warm_seconds: int = 180,
        max_pending_tasks: int = 100,
        on_start: Optional[Callable] = None,
        volumes: Optional[List[Volume]] = None,
        secrets: Optional[List[str]] = None,
        name: Optional[str] = None,
        authorized: bool = True,
        callback_url: Optional[str] = None,
    ):
        super().__init__(
            cpu,
            memory,
            gpu,
            image,
            timeout,
            workers,
            keep_warm_seconds,
            max_pending_tasks,
            on_start,
            volumes,
            secrets,
            name,
            authorized,
            callback_url,
        )

        self.is_asgi = True
