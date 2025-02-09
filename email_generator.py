from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

# Load API Key from .env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize LangChain Groq LLM
llm = ChatGroq(model_name="mixtral-8x7b-32768", groq_api_key=groq_api_key)

# Generate candidate email
def generate_candidate_email(name: str, experience: int, skills: str, job_description: str):
    prompt = f"""
    Generate a cold email for {name}, who has {experience} years of experience in {skills}. 
    The email should be tailored to the following job description: 
    {job_description}
    """
    
    response = llm([HumanMessage(content=prompt)])
    return response.content

# Generate recruiter email
def generate_recruiter_email(name: str, experience: int, skills: str, job_description: str):
    prompt = f"""
    Generate a cold email for a recruiter inviting a candidate for the job.
    The candidate has {experience} years of experience in {skills}. 
    The email should be tailored to the following job description: 
    {job_description}
    """
    
    response = llm([HumanMessage(content=prompt)])
    return response.content