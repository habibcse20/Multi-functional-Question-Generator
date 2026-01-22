from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(text, top_k=15):
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform([text])

    scores = zip(vectorizer.get_feature_names_out(), X.toarray()[0])
    sorted_words = sorted(scores, key=lambda x: x[1], reverse=True)

    return [word for word, score in sorted_words[:top_k]]

if __name__ == "__main__":
    text = "Natural language processing (NLP) is a sub-field of artificial intelligence (AI) that focuses on the interaction between computers and humans through natural language. The ultimate objective of NLP is to enable computers to understand, interpret, and generate human language in a way that is both valuable and meaningful."
    print(extract_keywords(text))
