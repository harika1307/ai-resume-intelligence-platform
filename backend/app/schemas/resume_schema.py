from typing import List,Optional
from pydantic import BaseModel

class Github(BaseModel):
    profile: Optional[str]=None
    repositories: List[str]=[]

class Skill(BaseModel):
    name: str
    domain: str
    source: str

class Education(BaseModel):
    degree: str
    field_of_study: str
    institution: str
    location: str
    cgpa: str
    start_year: str
    end_year: str

class Experience(BaseModel):
    company: str
    role: str
    employment_type: str
    location: str
    start_date: str
    end_date: str
    currently_working: bool
    description: str
    skills_used: List[str]

class Project(BaseModel):
    title: str
    description: str
    skills_used: List[str]
    github: str
    live_demo: str
    duration: str

class Certification(BaseModel):
    name: str
    issuer: str
    issue_date: str
    credential_id: str
    credential_url: str

class Resume(BaseModel):
    name: str
    emails: List[str]
    phones: List[str]
    github: Github
    linkedin: Optional[str]=None
    leetcode: Optional[str]=None
    portfolio: Optional[str]=None
    skills: List[Skill]
    education: List[Education]
    experience: List[Experience]
    projects: List[Project]
    certifications: List[Certification]