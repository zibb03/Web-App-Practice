# Hugging Face 모델 링크:  https://huggingface.co/sangrimlee/bert-base-multilingual-cased-nsmc

from transformers import pipeline

# 한국어 감정 분석을 진행하는 pipeline을 생성하는 부분
classifier = pipeline("sentiment-analysis", model="sangrimlee/bert-base-multilingual-cased-nsmc")
# 감정 분석을 진행하는 부분
# result = classifier("흠...포스터보고 초딩영화줄....오버연기조차 가볍지 않구나.")
result = classifier("액션이 화려하고 스토리도 좋았음")
# result의 첫번쨰 값을 가져오고, label의 value를 가져오는 부분
label = result[0]['label']
# result의 첫번쨰 값을 가져오고, score의 value를 가져오는 부분
# 소수점 15자리까지 값이 존재하는 score을 소수점 4자리까지 반올림하는 부분
score = round(result[0]['score'], 4)

# python f-string을 통해 문자열에 원하는 값을 넣는 부분
print(f"label: {label}, score: {score}")