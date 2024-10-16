from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
import os
from dotenv import load_dotenv

load_dotenv()
openapi_key=os.getenv('API_KEY')

llm = OpenAI(temperature=0.6, api_key=openapi_key) #0 means it is very safe but wont be much creative

def generate_chemicals_used_in_product(product):
    prompt_template_name = PromptTemplate(
        input_variables=['products'],
        template="I want to open a beauty store for {products} . Suggest a fancy name for this."
    )

    name_chain= LLMChain(llm=llm, prompt=prompt_template_name,output_key="store_name")

    prompt_template_name = PromptTemplate(
        input_variables=['products'],
        template="Give me the chemicals used in it the {products}. Return it as comma seperated "
    )

    chemical_chain= LLMChain(llm=llm, prompt=prompt_template_name,output_key="chemical_name")

    chain = SequentialChain(
        chains=[name_chain, chemical_chain],
        input_variables=["products"],
        output_variables=["store_name", "chemical_name"]
    )

    response = chain({'products': product})

    return response

if __name__ == "__main__":
    print(generate_chemicals_used_in_product("lipstick"))