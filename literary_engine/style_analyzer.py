"""Small, transparent prose indicators for the Runtime MVP."""


def analyze(text: str):
    sentences = [item for item in text.replace("！", "。").replace("？", "。").split("。") if item.strip()]
    lengths = [len(item) for item in sentences]
    return {"sentence_count": len(sentences), "average_sentence_length": round(sum(lengths) / max(len(lengths), 1), 2), "dialogue_marker_count": text.count("“") + text.count('"')}
