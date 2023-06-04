from datetime import datetime

class Hour:
    @staticmethod
    def now():
        current_hour = datetime.now()
        return current_hour
