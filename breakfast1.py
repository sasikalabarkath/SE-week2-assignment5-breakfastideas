
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 1. Initialize the OpenAI model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

# 2. Create a specific prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a nutrition-aware healthy cooking assistant."),
    ("human", """
    Suggest exactly 5 healthy breakfast ideas.

    Requirements:
    - Include a variety of breakfast options.
    - Prefer balanced meals with protein, fiber, and healthy fats.
    - Include the main ingredients for each idea.
    - Give one short sentence explaining its benefits.
    - Use a numbered list.
    - Keep the answer concise and practical.
    """)
])

# 3. Create the LangChain pipeline
chain = prompt | llm

# 4. Invoke the model
response = chain.invoke({})

# 5. Print the message content, not the message object
print(response.content)
