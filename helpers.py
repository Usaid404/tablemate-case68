"""Small helpers completed with an AI completion tool (L3.2) and reviewed by hand."""

def format_wait_message(position, minutes):
    # Return a guest message such as "You are #3 in line, about 40 min wait".
    if position < 1 or minutes < 0:
        raise ValueError("invalid position or minutes")
    return f"You are #{position} in line, about {minutes} min wait"

def mask_phone(phone):
    # Mask all but the last 4 digits of a phone number.
    digits = "".join(ch for ch in phone if ch.isdigit())
    if len(digits) < 4:
        raise ValueError("phone too short")
    return "X" * (len(digits) - 4) + digits[-4:]

def is_party_valid(size, max_size=12):
    # A party is valid if size is an int from 1 to max_size.
    return isinstance(size, int) and not isinstance(size, bool) and 1 <= size <= max_size
