"""Hệ thống phân cấp Custom Exception cho Recommendation System

Mô-đun này thiết lập hệ thống phân cấp ngoại lệ có cấu trúc tuân thủ các nguyên tắc xử lý ngoại lệ OOP.
Tất cả các ngoại lệ đều bắt nguồn từ `RecSysException`, cho phép người gọi phát hiện các lỗi trên toàn
hệ thống hoặc xử lý các ngoại lệ cụ thể theo từng lớp một cách thích hợp.
"""

from typing import Any, Optional

class RecSysException(Exception):
    """Basic Class cho tất cả các ngoại lệ trong Recommendation System"""
    def __init__(self, message, details: Optional[dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}


# ==========================================
# Evaluation Layer Exceptions
# ==========================================

class EvaluationException(RecSysException):
    """"Base Class cho các ngoại lệ được đưa ra trong khi model evaluation"""
    pass

class InvalidMetricParameterError(EvaluationException):
    """Raise khi tham số không hợp lệ (ví dụ: k)"""
    def __init__(self, message: str, k: Optional[int] = None) -> None:
        details = {"k": k} if k is not None else {}
        super().__init__(message, details)
        self.k = k