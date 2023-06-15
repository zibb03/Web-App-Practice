from transformers import pipeline

# 감정 분석을 진행하는 pipeline을 생성하는 부분
nlp = pipeline("sentiment-analysis")
# 감정 분석을 진행하는 부분
result = nlp("I love this movie")
# result의 첫번쨰 값을 가져오고, label의 value를 가져오는 부분
label = result[0]['label']
# result의 첫번쨰 값을 가져오고, score의 value를 가져오는 부분
# 소수점 15자리까지 값이 존재하는 score을 소수점 4자리까지 반올림하는 부분
score = round(result[0]['score'], 4)

print(result)
# python f-string을 통해 문자열에 원하는 값을 넣는 부분
print(f"label: {label}, score: {score}")