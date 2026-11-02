"""Tests for rule f588c0de: ORDER_API_PATH constant in order.py.

Rule: src/backend/order.py 必须定义常量 ORDER_API_PATH，
值为字符串「/api/orders」
"""

import importlib
import inspect
from pathlib import Path

import pytest


@pytest.fixture
def order_module():
    """Import src.backend.order fresh for each test."""
    return importlib.import_module("src.backend.order")


def test_rule_f588c0de_order_api_path_is_defined(order_module) -> None:
    """ORDER_API_PATH 必须在 src/backend/order.py 中被定义。"""
    assert hasattr(order_module, "ORDER_API_PATH"), (
        "src/backend/order.py 未定义常量 ORDER_API_PATH"
    )


def test_rule_f588c0de_order_api_path_value(order_module) -> None:
    """ORDER_API_PATH 的值必须是字符串 '/api/orders'。"""
    value = getattr(order_module, "ORDER_API_PATH")
    assert value == "/api/orders", (
        f"ORDER_API_PATH 期望 '/api/orders'，实际为 {value!r}"
    )


def test_rule_f588c0de_order_api_path_is_string(order_module) -> None:
    """ORDER_API_PATH 必须是字符串类型。"""
    value = getattr(order_module, "ORDER_API_PATH")
    assert isinstance(value, str), (
        f"ORDER_API_PATH 期望 str 类型，实际为 {type(value).__name__}"
    )


def test_rule_f588c0de_source_location() -> None:
    """ORDER_API_PATH 必须来源于 src/backend/order.py，不能从别处重导出。"""
    import src.backend.order as order_module

    source_path = Path(inspect.getsourcefile(order_module)).resolve()
    expected = Path("src/backend/order.py").resolve()
    # 允许在任意深度仓库里匹配后缀
    assert source_path.parts[-3:] == expected.parts[-3:], (
        f"ORDER_API_PATH 所在文件路径不符，期望以 src/backend/order.py 结尾，"
        f"实际为 {source_path}"
    )
