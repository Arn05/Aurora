import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
#from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return (textwrap.indent(text, '> ', predicate=lambda _: True))


genai.configure(api_key='AIzaSyASZqZgHvFivk5xoXVN-p1cGGjOZ-_JMmw')
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')


response = model.generate_content("What is the meaning of life?")

print(response.text)
response.prompt_feedback
response.candidates
response = model.generate_content("What is the meaning of life?", stream=True)
for chunk in response:
  print(chunk.text)
  print("_"*80)
