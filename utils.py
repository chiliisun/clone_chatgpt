from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

def get_chat_response(prompt,memory,openai_api_key):
    model = ChatOpenAI(model="gpt-3.5-turbo",openai_api_key=openai_api_key,base_url="https://api.aigc369.com/v1")
    chain = ConversationChain(llm=model,memory=memory)

    response = chain.invoke({"input":prompt})

    return response["response"]

memory = ConversationBufferMemory(return_messages=True)
# get_chat_response("Hello",memory,"sk-BNrnisPDBUHJEqWeeZaQB0QaoIoAefy1aDq0vkurGsbmPO2z")
