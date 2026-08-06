from app.rag.embedding import EmbeddingService
import numpy as np

from app.utils.similarity import get_similarity_score
class SemanticSkillMatcher:
    def __init__(self,embedding_service: EmbeddingService,similarity_threshold: float=0.75):
        self.embedding_service=embedding_service
        self.similarity_threshold=similarity_threshold
    
    def get_skill_embedding(self,skill: str)->np.ndarray:
        return self.embedding_service.embed_text(skill)
    def build_skill_map(self,skills: list)-> dict:
        skill_map={}
        for skill in skills:
            normalized_name=skill["name"].strip().lower()
            skill_map[normalized_name]=skill
        return skill_map
    def match_skills(self,resume_data: dict,jd_data: dict)->dict:
        resume_skills=resume_data["skills"]
        jd_skills=jd_data["skills"]

        resume_skill_data={}
        jd_skill_data={}
        
        for resume_skill in resume_skills:
            resume_skill_data[resume_skill["name"]]={
                "skill":resume_skill,
                "embedding":self.get_skill_embedding(resume_skill["name"])
            }
        for jd_skill in jd_skills:
            jd_skill_data[jd_skill["name"]]={
                "skill":jd_skill,
                "embedding":self.get_skill_embedding(jd_skill["name"])
            }
        matched_skills=[]
        missing_skills=[]
        extra_skills=[]
        matched_resume_skills=set()
        for skill,jd_skill_info in jd_skill_data.items():
            best_similarity=0.0
            best_resume_skill=None
            best_resume_info=None
            for resume_skill,res_skill_info in resume_skill_data.items():
                
                similarity=get_similarity_score(res_skill_info["embedding"],jd_skill_info["embedding"])
                if similarity>best_similarity:
                    best_similarity=similarity
                    best_resume_skill=resume_skill
                    best_resume_info=res_skill_info
            if best_similarity>=self.similarity_threshold:
                matched_skills.append({
                    "resume_skill":best_resume_info["skill"],
                    "jd_skill":jd_skill_info["skill"],
                    "similarity":best_similarity
                })
                matched_resume_skills.add(best_resume_skill)
            else:
                missing_skills.append(jd_skill_info["skill"])
        for skill_name,skill_info in resume_skill_data.items():
                if skill_name not in matched_resume_skills:
                    extra_skills.append(skill_info["skill"])
        return {
            "matched_skills":matched_skills,
            "missing_skills":missing_skills,
            "extra_skills":extra_skills
        }