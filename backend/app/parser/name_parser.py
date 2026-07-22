from app.core.constants import TOP_LINES_TO_CHECK,STOP_WORDS,EDUCATION_KEYWORDS,LINK_KEYWORDS,WORD_COUNT_SCORES

def score_name_candidate(line: str)->int:
    score=0
    words=line.split()
    lower_words=[word.lower() for word in words]
    word_count=len(words)
    score+=WORD_COUNT_SCORES.get(word_count,0)
    for char in line:
        if char.isdigit():
            score-=3
            break
    # captilization
    for word in words:
        if word.istitle():
            score+=1
    #educational check
    for word in lower_words:
        if word in EDUCATION_KEYWORDS:
            score-=5
            break
    #stop word check
    for word in lower_words:
        if word in STOP_WORDS:
            score-=5
            break
    #link keywords check
    for word in lower_words:
        if word in LINK_KEYWORDS:
            score-=5
            break
    return score
def extract_name(text: str)->str | None:
    lines=text.splitlines()
    candidate_lines=lines[:TOP_LINES_TO_CHECK]
    best_name=None
    best_score=float("-inf")
    for line in candidate_lines:
        if not line.strip() :
            continue
        score=score_name_candidate(line)
        if score>best_score:
            best_score=score
            best_name=line
    return best_name



