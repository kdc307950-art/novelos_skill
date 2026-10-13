"""Extract cautious theme candidates from structured text, never definitive intent."""


def analyze(text: str):
    candidates = []
    keywords = {"责任": "责任与选择", "自由": "责任与选择", "孤独": "孤独与连接", "救赎": "救赎与代价", "权力": "权力与责任"}
    for keyword, theme in keywords.items():
        if keyword in text and theme not in candidates:
            candidates.append(theme)
    return [{"theme": theme, "confidence": 0.35, "status": "candidate"} for theme in candidates]
