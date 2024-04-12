from transformers import pipeline

# 질문 응답을 진행하는 pipeline을 생성하는 부분
nlp = pipeline("question-answering")
# 질문 응답을 진행하는 부분
result = nlp(question="What is my name?", context="My name is John")

print(result)
# answer의 value를 가져오는 부분
answer = result['answer']
# score의 value를 가져오는 부분
# 소수점 15자리까지 값이 존재하는 score을 소수점 4자리까지 반올림하는 부분
score = round(result['score'], 4)
# python f-string을 통해 문자열에 원하는 값을 넣는 부분
print(f"answer: {answer}, score: {score}")