from datetime import datetime

class Distance:
    """
    Class to represent a distance measurement with timestamp.
    """
    def __init__(self, distance=None):
        self.distance = distance
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Distance: {self.distance} cm, Timestamp: {self.timestamp}"