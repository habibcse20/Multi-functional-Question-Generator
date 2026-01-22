import random
from ml.keyword_extractor import extract_keywords
from services.text_service import split_sentences
from services.difficulty_service import filter_by_difficulty

def generate_questions(text, num, qtype, difficulty):
    sentences = split_sentences(text)
    sentences = filter_by_difficulty(sentences, difficulty)
    keywords = extract_keywords(text)

    questions = []
    used = set()

    for sent in sentences:
        for kw in keywords:
            if kw.lower() in sent.lower() and sent not in used:
                used.add(sent)

                if qtype == "fill":
                    question = sent.replace(kw, "________")
                    questions.append({
                        "type": "Fill in the Blank",
                        "question": question,
                        "answer": kw
                    })

                elif qtype == "tf":
                    question = sent
                    answer = random.choice(["True", "False"])
                    questions.append({
                        "type": "True / False",
                        "question": question,
                        "answer": answer
                    })

                else:
                    question = sent.replace(kw, "________")
                    options = random.sample(keywords, min(3, len(keywords)))
                    options.append(kw)
                    random.shuffle(options)

                    questions.append({
                        "type": "MCQ",
                        "question": question,
                        "options": options,
                        "answer": kw
                    })

                if len(questions) == num:
                    return questions

    return questions

