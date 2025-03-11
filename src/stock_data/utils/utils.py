# =================
# ==== IMPORTS ====
# =================

from datetime import UTC, datetime

# ===================
# ==== FUNCTIONS ====
# ===================

def generate_timestamp() -> str:
    """Generate the timestamp to be used by versionning data

    Returns:
        (str): Timestamp in 'YYYY_MM_DDTHH_MM_SSz' format.
    """
    current_ts = datetime.now(tz=UTC).strftime("%Y_%m_%dT%H_%M_%S_%fz")
    return current_ts[:-4] + current_ts[-1:]  # Don't keep microseconds
