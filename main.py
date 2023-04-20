import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

load_dotenv()

llm = OpenAI()
prompt = PromptTemplate(
    input_variables=['lang'],
    template="{lang}で何かコードを書いてみてください"
)

# print(llm(prompt.format(lang="C++")))
chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run('ruby'))
