
from datetime import datetime
from logger import function_logger

KEY = "TSTFEED0300|7E3E|0400"
file_data = "hblog.txt"


def get_timestamp(line):
    index = line.find("Timestamp ") + len("Timestamp ")
    time_str = line[index:index + 8]
    return datetime.strptime(time_str, "%H:%M:%S")


def analyze_heartbeat():
    previous_time = None

    with open(file_data, "r", encoding="utf-8") as f:
        for line in f:
            if KEY not in line:
                continue

            current_time = get_timestamp(line)

            if previous_time is not None:
                diff = (previous_time - current_time).total_seconds()
                event_time = previous_time.strftime("%H:%M:%S")

                if 31 < diff < 33:
                    function_logger.warning(
                        f"Heartbeat delay {int(diff)}s at {event_time} (key={KEY})"
                    )
                elif diff >= 33:
                    function_logger.error(
                        f"Heartbeat delay {int(diff)}s at {event_time} (key={KEY})"
                    )

            previous_time = current_time


analyze_heartbeat()
