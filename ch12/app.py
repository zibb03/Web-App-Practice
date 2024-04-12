import gradio as gr
from transformers import pipeline
# 한국어 감정 분석을 진행하는 pipeline을 생성하는 부분
classifier = pipeline("sentiment-analysis", model="sangrimlee/bert-base-multilingual-cased-nsmc")

# 감정 분석을 진행하는 함수
def sentiment_analysis(text):
    # 감정 분석(예측)을 진행하는 부분
    result = classifier(text)
    # result의 첫번쨰 값을 가져오고, label의 value를 가져오는 부분
    label = result[0]['label']
    # 예측한 label 값을 반환하는 부분
    return label

demo = gr.Interface(fn=sentiment_analysis, # Gradio가 실행할 함수를 지정하는 fn
                    inputs="text", # 사용자가 입력할 데이터의 타입을 지정하는 inputs
                    outputs="text", # 함수의 출력타입을 지정하는 outputs
                    title="감정분석", # 웹 애플리케이션의 제목을 지정하는 title
                    description="텍스트를 입력하면 감정을 분석합니다.") # 웹 애플리케이션에 대한 설명을 제공하는 description

# share의 값을 True로 변경해줄 시, local ULR과 public URL을 배포함
demo.launch(share=True)