"""Type stubs for the `dlib` module.

This project uses dlib at runtime (face detection / landmark / recognition).
However, dlib wheels are not always available/installed in the active VSCode
interpreter, which causes Pylance to show: "Import \"dlib\" could not be resolved".

These stubs are only for IDE/static type resolution; they do not provide
runtime functionality.
"""

from typing import Any, Sequence, List


def get_frontal_face_detector() -> Any: ...


class rectangle:
    def left(self) -> int: ...
    def right(self) -> int: ...
    def top(self) -> int: ...
    def bottom(self) -> int: ...


def shape_predictor(model_path: str) -> Any: ...


class face_recognition_model_v1:
    def __init__(self, model_path: str) -> None: ...
    def compute_face_descriptor(self, img: Any, shape: Any) -> Any: ...

