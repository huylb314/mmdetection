from .coco import CocoDataset
from .registry import DATASETS

@DATASETS.register_module
class ZaloDataset(CocoDataset):
    CLASSES = ("1. No entry", "2. No parking / waiting", "3. No turning", "4. Max Speed", "5. Other prohibition signs", "6. Warning", "7. Mandatory")