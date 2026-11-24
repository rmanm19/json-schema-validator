import re

def sanitize_text(text: str) -> str:
    return re.sub(r"(sk-[A-Za-z0-9]{8,}|ghp_[A-Za-z0-9]{10,})", "[REDACTED]", text)
