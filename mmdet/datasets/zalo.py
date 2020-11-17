from .coco import CocoDataset
from .registry import DATASETS

@DATASETS.register_module
class ZaloDataset(CocoDataset):
    CLASSES = ("No entry", "No parking / waiting", "No turning", "Max Speed", "Other prohibition signs", "Warning", "Mandatory")