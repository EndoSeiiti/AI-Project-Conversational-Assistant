from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool 
def calculator(a:float, b:float) -> str:
    """Util para fazer calculos aritmeticos basicos com números"""
    print ("Ferramenta foi ativada")
    return f"A soma de `{a} e {b} é {a + b}"

def main():
    model = ChatOpenAI(temperature=0)

    tools = [calculator]
    agent_executor = create_react_agent(model,tools)

    print("Olá, sou seu assistente IA. Digite 'SAIR' para sair")
    print ("Você pode me pedir para fazer calculos matematicos ou apenas conversar comigo")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "SAIR":
            break

        print ("\nAssistente: ", end="")
        for chunk in agent_executor.stream(
            {"messages":[HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk ["agent"]["messages"]:
                    print(message.content, end="")
    
    print()

if __name__ == "__main__":
    main()