"""Ranking Evaluation Metrics
Áp dụng các chỉ số đánh giá đề xuất tiêu chuẩn:
- Precision@K
- Recall@K
- NDCG@K (Lợi nhuận tích lũy chiết khấu chuẩn hóa)
- MAP@K (Độ chính xác trung bình)
- HitRate@K
- MRR@K (Hệ số thứ hạng nghịch đảo trung bình)
"""

import math
from typing import Any, Sequence
from recsys.__init__ import BaseMetric

class RecallAtK(BaseMetric):
    """Recall@K: Tỷ lệ phần trăm tổng số mục phù hợp được đưa vào danh sách
    các đề xuất hàng đầu (top-K)."""

    @property
    def name(self) -> str:
        return "Recall"

    def _compute_metric(
        self,
        ground_truth: set[Any],
        top_k_recs: Sequence[Any],
        k: int,
    ) -> float:
        if not ground_truth:
            return 0.0
        hits = sum(1 for item in top_k_recs if item in ground_truth)
        # Meaning:
        # hits = 0
        # for item in top_k_recs:
        #     if item in ground_truth:
        #         hits += 1
        return hits / float(len(ground_truth))


class NDCGAtK(BaseMetric):
    """Lợi nhuận lũy kế chiết khấu chuẩn hóa tại K (NDCG@K).

    Đánh giá chất lượng xếp hạng bằng cách áp dụng hệ số điều chỉnh vị trí theo logarit:
        DCG@K = sum_{i=1}^K rel_i / log2(i + 1)
        IDCG@K = sum_{i=1}^{min(K, |ground_truth|)} 1 / log2(i + 1)
        NDCG@K = DCG@K / IDCG@K
    """

    @property
    def name(self) -> str:
        return "NDCG"

    def _compute_metric(
        self,
        ground_truth: set[Any],
        top_k_recs: Sequence[Any],
        k: int,
    ) -> float:
        dcg = 0.0
        for rank_idx, item in enumerate(top_k_recs):
            if item in ground_truth:
                dcg += 1.0 / math.log2(rank_idx + 2)  # rank_idx 0 -> position 1 -> log2(2)

        ideal_hits = min(k, len(ground_truth))
        if ideal_hits == 0:
            return 0.0

        idcg = sum(1.0 / math.log2(i + 2) for i in range(ideal_hits))
        return dcg / idcg if idcg > 0 else 0.0