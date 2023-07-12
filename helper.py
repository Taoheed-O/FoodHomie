import os
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


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


def name_item_generator(restaurant):
     # First prompt in the chain
    prompt_name = PromptTemplate(
        template = "I want to open a restaurant for {restaurant} food. Suggest a fancy name for that",
        input_variables=['restaurant']
                            )
    llm_name_chain = LLMChain(prompt=prompt_name, llm=llm, output_key='restaurant_name')


    # Second prompt in the chain
    prompt_items = PromptTemplate(
        template="Suggest 10 menu items for {restaurant_name}. Return as a comma separated variable",
                            input_variables=['restaurant_name']
                            )
    llm_item_chain = LLMChain(prompt=prompt_items, llm=llm, output_key='menu_items')

    chain =  SequentialChain(
        chains=[llm_name_chain, llm_item_chain],
        input_variables=['restaurant'],
        output_variables=['restaurant_name', 'menu_items']
                            )
    response = chain({'restaurant':restaurant})
    return response