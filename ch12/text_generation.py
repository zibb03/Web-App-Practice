from transformers import pipeline

# 텍스트 생성을 진행하는 pipeline을 생성하는 부분
nlp = pipeline("text-generation")
# 텍스트 생성을 진행하는 부분
result = nlp("In a world")

# result의 첫번쨰 값을 가져오고, generated_text의 value를 가져오는 부분
print(result[0]['generated_text'])