"""
base.py
File này định nghĩa class BaseMetric.

Tác dụng: Đây là bộ khung chuẩn cho tất cả các thang đo đánh giá (metrics)
trong hệ thống (như Recall, Precision, NDCG,...).
"""

from abc import ABC, abstractmethod
from typing import Any, Sequence

from recsys.exceptions import InvalidMetricParameterError

class BaseMetric(ABC):
    """Lớp cơ sở trừu trượng cho các số liệu xếp hạng top-K.
       Thực thi việc đóng gói và xác thực tham số k trong khi các lớp con
       cung cấp logic đánh giá cụ thể (ví dụ: Recall, NDCG, Precision).
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Tên của thang đo đánh giá"""
        pass

    def compute(
            self,
            ground_truth: Sequence[Any] | set[Any],
            recommendations: Sequence[Any],
            k: int,
    ) -> float:
        """Tính toán điểm đánh giá cho danh sách gợi ý của người dùng.
        
        Args:
            ground_truth: Sequence hoặc set chứa các IDs liên quan đến người dùng.
            recommendations: Danh sách xếp hạng các items IDs gợi ý.
            k: Ngưỡng xếp hạng đánh giá (phải là số nguyên dương).

        Returns:
            Tính toán điểm đánh giá trong khoảng [0.0, 1.0].
        """
        if not isinstance(k, int) or k <= 0:
            raise InvalidMetricParameterError(f"k must be a positive integer, got {k}", k=k)

        truth_set = set(ground_truth) if not isinstance(ground_truth, set) else ground_truth
        if not truth_set or not recommendations:
            return 0.0

        top_k_recs = recommendations[:k]
        return float(self._compute_metric(truth_set, top_k_recs, k))

    @abstractmethod
    def _compute_metric(
        self,
        ground_truth: set[Any],
        top_k_recs: Sequence[Any],
        k: int,
    ) -> float:
        """Phân lớp thực hiện tính toán xếp hạng."""
        pass