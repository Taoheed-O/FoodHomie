from key import key
import os
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
from langchain.chains import LLMChain


api_key = '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'
#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
os.environ['HUGGINGFACEHUB_API_TOKEN'] = api_key
'''
Available models:
XGen by sales force: "Salesforce/xgen-7b-8k-base"
Dolly by data bricks : "databricks/dolly-v2-3b"
flan by Google: "google/flan-t5-xxl"
Camel by writer: "Writer/camel-5b-hf"
Falcon by Technology Innovation Institute(TII): "tiiuae/falcon-40b"
'''

repo_id = "google/flan-t5-xxl"
# See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options

llm = HuggingFaceHub(
    repo_id=repo_id,
    model_kwargs={"temperature": 0.7, "max_length": 1000}
                      )


def name_item_generator(cuisine):
    return {'restaurant name': 'curry delight',
            'menu items': 'samosa, chicken tikka, chicken biryani, pizza'}