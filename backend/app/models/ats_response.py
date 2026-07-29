from pydantic import BaseModel
from typing import List
class Skill(BaseModel):
    name: str
    domain: str
    source: str | None=None

class SkillAnalysis(BaseModel):
    matched_skills: int
    missing_skills:int
    extra_skills:int
    total_required_skills:int
    skill_match_percentage: float
class AIFeedback(BaseModel):
    overall_feedback: str
    strengths: List[str]
    weaknesses: List[str]
    resume_improvements: List[str]
    keyword_suggestions: List[str]
    missing_skill_suggestions: List[str]
    interview_questions: List[str]

class ATSResponse(BaseModel):
    ats_score:float
    skill_analysis: SkillAnalysis
    matched_skills:list[Skill]
    missing_skills:list[Skill]
    extra_skills: list[Skill]
    ai_feedback: AIFeedback