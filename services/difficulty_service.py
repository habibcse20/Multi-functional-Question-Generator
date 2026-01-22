def filter_by_difficulty(sentences, level):
    if level == "easy":
        return [s for s in sentences if len(s.split()) < 12]
    if level == "medium":
        return [s for s in sentences if 12 <= len(s.split()) <= 20]
    return [s for s in sentences if len(s.split()) > 20]

