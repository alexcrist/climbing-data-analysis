import json

SCORES_FILE = './data/county-scores-raw.json'
NORMALIZED_SCORES_FILE = './data/county-scores-normalized.json'

if __name__ == '__main__':

    with open(SCORES_FILE) as file:
        scores = json.load(file)

    max_score = 0
    for county, score in scores.items():
        max_score = max(score, max_score)

    normalized_scores = {}
    for county, score in scores.items():
        normalized_score = round(score / max_score * 100)
        normalized_scores[county] = normalized_score

    with open(NORMALIZED_SCORES_FILE, 'w') as file:
        json.dump(normalized_scores, file)
