from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import START, StateGraph, END
from uipath_langchain.chat import UiPathChat
from pydantic import BaseModel
from uipath_langchain.retrievers import ContextGroundingRetriever
import json, os, logging, ast


llm = UiPathChat(
    model="gpt-4o-2024-11-20",
    temperature=0,
    max_tokens=128000,
    timeout=None,
    max_retries=2
    )

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class GraphState(BaseModel):
    topic: str
    messages: list = []

class GraphOutput(BaseModel):
    questions: str

context_grounding = ContextGroundingRetriever(
    index_name="Workshop_Index",
    folder_path="Shared",
    number_of_results=5
    )

async def generate_questions(state: GraphState) -> GraphOutput:
    topic = state.topic or (state.messages[-1]["content"] if state.messages else "general AI")
    try:
        context = await context_grounding.ainvoke(state.topic)
        context_text = "".join([doc.page_content for doc in context])
        logging.info(f"Retrieved Context: {context_text}")

        system_message = (f"""Role 
        You are an AI assistant responsible for generating high quality questions based only on the provided context text You analyze the content carefully understand key concepts and create relevant questions that help in learning assessment and revision
        Rules
        Use only the given context text as {context_text} the source of information.
        Do not add external knowledge or assumptions.
        Ensure the questions are clear concise and directly related to the context. 
        Avoid repetition and maintain variety in the types of questions.
        Keep the language simple and suitable for students
        Goals
        Generate meaningful and relevant questions that cover important concepts from the context.
        Create a mix of question types such as short answer conceptual and multiple choice Focus on helping the user understand and revise the material effectively""")
        
        human_message = (f"Generate questions about {state.topic} also mentioning the correct answers. Considering student is preparing for my final exams, make sure the questions are relevant and cover important aspects of the topic. Format the questions in a clear and concise manner.")

        response = await llm.ainvoke([
            SystemMessage(system_message),
            HumanMessage(human_message)
        ])

        # Write the response to a text file
        with open("questions.txt", "w", encoding="utf-8") as file:
            file.write(response.content)

        logging.info(f"LLM Response: {response.content}")

        return GraphOutput(questions=response.content)
    except Exception as e:
        logger.error(f"Error in generate_questions: {e}")
        return GraphOutput(questions="An error occurred while generating the questions.")
    

builder = StateGraph(GraphState, output_schema = GraphOutput)

builder.add_node("generate_questions", generate_questions)

builder.add_edge(START, "generate_questions")
builder.add_edge("generate_questions", END)

graph = builder.compile()

import asyncio

if __name__ == "__main__":
    topic = input("Enter topic: ")
    result = asyncio.run(graph.ainvoke({"topic": topic}))
    print(result["questions"])