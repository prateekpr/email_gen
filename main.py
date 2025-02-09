from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from email_generator import generate_candidate_email, generate_recruiter_email
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Set up templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Pydantic model for request validation
class CandidateRequest(BaseModel):
    name: str
    experience: int
    skills: str
    job_description: str

class RecruiterRequest(BaseModel):
    name: str
    experience: int
    skills: str
    job_description: str

# Landing page
@app.get("/")
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Recruiter page
@app.get("/recruiter")
async def get_recruiter_form(request: Request):
    return templates.TemplateResponse("recruiter.html", {"request": request})

# Candidate page
@app.get("/candidate")
async def get_candidate_form(request: Request):
    return templates.TemplateResponse("candidate.html", {"request": request})

# Generate candidate email
@app.post("/generate/candidate")
def generate_candidate(request: CandidateRequest):
    try:
        email_content = generate_candidate_email(request.name, request.experience, request.skills, request.job_description)
        return {"email": email_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Generate recruiter email
@app.post("/generate/recruiter")
def generate_recruiter(request: RecruiterRequest):
    try:
        email_content = generate_recruiter_email(request.name, request.experience, request.skills, request.job_description)
        return {"email": email_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))