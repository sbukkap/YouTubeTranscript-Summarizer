from transformers import pipeline
summarization = pipeline("summarization")
original_text = """
For the first time in many years , shredder won his legendary battle against Turtles , he was about to lose
his fierce battle but he clutched up in a 1v3 with a dlq sniper in his hand! One shot to the head with the sniper
and then two smaks to the face with the shotgun  . This battle is really worth a watch
"""
summary_text = summarization(original_text)[0]['summary_text']
print("Summary:", summary_text)
