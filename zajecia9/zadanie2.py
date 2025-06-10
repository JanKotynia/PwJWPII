# from transformers import pipeline
# import gradio as gr
# from transformers import BertTokenizer, BertForSequenceClassification
#
# tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
# model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)
# classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
#
# def greet(data):
#     result = classifier(data)
#     if round(result[0]['score']) > 0.5:
#         return "Spam"
#     else:
#         return "Not spam"
#
# gr.Interface(fn=greet, inputs="text", outputs="text").launch()

