"""
Optimized Interface for Edge AI - YOLOv8-nano.
Handles processing of vision triggers from the frontend.
"""
from typing import Dict, List

class EdgeVisionHandler:
    def __init__(self, confidence_threshold: float = 0.4):
        self.threshold = confidence_threshold
        # Pre-trained class mappings for mobility assistance
        self.classes = {0: "person", 1: "bicycle", 2: "car", 3: "motorcycle", 5: "bus", 7: "truck", 11: "stop sign"}

    def process_edge_trigger(self, detections: List[Dict]):
        """
        Analyzes detections reported by the client-side YOLOv8 model.
        Returns safety warnings if hazards are detected in the path.
        """
        for item in detections:
            if item.get("confidence", 0) > self.threshold:
                if item["class"] in [11, 2, 5, 7]: # High hazard classes
                    return {
                        "alert": True,
                        "command": "STOP",
                        "reason": f"{self.classes.get(item['class'])} detected ahead."
                    }
        return {"alert": False, "command": "CONTINUE"}

vision_handler = EdgeVisionHandler()
