from datetime import datetime
import pytz

class DateTimeParser:
    def __init__(self, timezone='Asia/Bangkok'):
        # Set the default timezone (Bangkok in this case)
        self.timezone = pytz.timezone(timezone)

    def parse(self, date_str):
        try:
            # Try parsing the string with the expected format (including the timezone)
            parsed_datetime = datetime.strptime(date_str, "%d-%m-%YT%H:%M:%S%z")
            return parsed_datetime
        except ValueError:
            # If it fails (due to missing timezone), assume Bangkok timezone and localize it
            # Remove the timezone part and parse the naive datetime
            naive_datetime = datetime.strptime(date_str, "%d-%m-%YT%H:%M:%S")
            
            # Localize the naive datetime to the chosen timezone (default is Bangkok)
            localized_datetime = self.timezone.localize(naive_datetime)
            return localized_datetime