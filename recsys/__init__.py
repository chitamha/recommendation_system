"""
Tác dụng:
- Vai trò khởi tạo package recsys và định nghĩa API công khai của thư viện.
- Là file giúp package có giao diện sử dụng gọn gàng
Ví dụ:
from recsys import (
    Dataset,
    PopularityRecommender,
    RecommendationService,
)
thay cho
from recsys.data.dataset import Dataset
from recsys.models.popularity import PopularityRecommender
from recsys.service.service import RecommendationService
"""


from recsys.evaluation.base import BaseMetric
from recsys.exceptions import (
    RecSysException,
    EvaluationException,
    InvalidMetricParameterError,
)

__version__ = "1.0.0"

__all__ = [
    # Data Layer
    
    # Model Layer
    
    # Evaluation Layer
    "BaseMetric",

    # Service Layer
    
    # Exceptions
    "RecSysException",
    "EvaluationException",
    "InvalidMetricParameterError",
]