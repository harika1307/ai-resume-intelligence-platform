import numpy as np
from app.rag.embedding import EmbeddingService
from app.utils.context_builder import build_jd_context,build_project_context,build_experience_context
from app.utils.similarity import get_similarity_score
class ATSScoringEngine:
    SKILL_WEIGHT=0.40
    PROJECT_WEIGHT=0.20
    EXPERIENCE_WEIGHT=0.20
    EDUCATION_WEIGHT=0.10
    COMPLETENESS_WEIGHT=0.10
    PROJECT_SIMILARITY_THRESHOLD = 0.45
    EXPERIENCE_SIMILARITY_THRESHOLD = 0.50
    DEGREE_WEIGHT = 0.70
    FIELD_WEIGHT = 0.30
    DEGREE_NORMALIZATION = {
        "b.tech": "bachelor",
        "b.e": "bachelor",
        "bachelor of technology": "bachelor",
        "bachelor of engineering": "bachelor",
        "bachelor": "bachelor",

        "m.tech": "master",
        "m.e": "master",
        "master": "master",

        "phd": "doctorate",
        "doctorate": "doctorate"
    }
    DEGREE_LEVELS = {
        "bachelor": 1,
        "master": 2,
        "doctorate": 3
    }
    FIELD_NORMALIZATION = {
        "cse": "computer science",
        "computer science and engineering": "computer science",
        "it": "information technology",
        "ece": "electronics and communication",
    }
    def __init__(self,resume_data: dict,jd_data: dict,skill_match_result: dict,embedding_service: EmbeddingService):
        self.resume_data=resume_data
        self.jd_data=jd_data
        self.skill_match_result=skill_match_result
        self.embedding_service=embedding_service
    def calculate_skill_score(self)->dict:
        matched_skills=self.skill_match_result["matched_skills"]
        missing_skills=self.skill_match_result["missing_skills"]
        # coverage_score=matched_skills/required_skills
        # quality_score=Average similairty
        required_skills=len(matched_skills)+len(missing_skills)
        if required_skills==0:
            coverage_score=0.0
        else:
            coverage_score=len(matched_skills)/required_skills
        similarities=[skill["similarity"] for skill in matched_skills]
        if len(matched_skills)==0:
            quality_score=0.0
        else:   
            quality_score=float(np.mean(similarities))
        final_skill_score=coverage_score*quality_score*100
        return {
            "score": round(final_skill_score, 2),
            "coverage_score": round(coverage_score * 100, 2),
            "quality_score": round(quality_score * 100, 2),
            "matched_skills": len(matched_skills),
            "missing_skills": len(missing_skills),
            "total_required": required_skills
        }
    def calculate_project_score(self):
        jd_context=build_jd_context(self.jd_data)
        jd_embedding=self.embedding_service.embed_text(jd_context)
        
        relevant_projects=[]
        for project in self.resume_data.get("projects",[]):
            
            project_context=build_project_context(project)
            project_embedding=self.embedding_service.embed_text(project_context)
            similarity=get_similarity_score(project_embedding,jd_embedding)
            print(project["title"])
            print(similarity)
            print("-" * 40)
            if similarity>=self.PROJECT_SIMILARITY_THRESHOLD:
                relevant_projects.append({
                    "project":project,
                    "similarity":similarity
                })
        if len(relevant_projects)==0:
            project_score=0.0
        else:
            similarities=[project["similarity"] for project in relevant_projects]
            project_score=float(np.mean(similarities))*100
        return {
            "score":round(project_score,2),
            "relevant_projects":relevant_projects,
            
        }
    def calculate_experience_score(self):
        jd_context=build_jd_context(self.jd_data)
        jd_embedding=self.embedding_service.embed_text(jd_context)
        
        relevant_experiences=[]
        for experience in self.resume_data.get("experience",[]):
            experience_context=build_experience_context(experience)
            experience_embedding=self.embedding_service.embed_text(experience_context)
            similarity=get_similarity_score(experience_embedding,jd_embedding)
            print(experience["role"])
            print(similarity)
            print("-" * 40)
            if similarity>=self.EXPERIENCE_SIMILARITY_THRESHOLD:
                relevant_experiences.append({
                    "experience":experience,
                    "similarity":similarity
                })
        if len(relevant_experiences)==0:
            experience_score=0.0
        else:
            similarities=[experience["similarity"] for experience in relevant_experiences]
            experience_score=float(np.mean(similarities))*100
        return {
            "score":round(experience_score,2),
            "relevant_experiences":relevant_experiences,
            
        }

    def normalize_degree(self, degree: str) -> str:
        degree = degree.strip().lower()
        return self.DEGREE_NORMALIZATION.get(degree, degree)
    def normalize_field(self, field: str) -> str:
            field = field.strip().lower()
            return self.FIELD_NORMALIZATION.get(field, field)

    def calculate_education_score(self):
        resume_education = self.resume_data.get("education", [])
        jd_education = self.jd_data.get("requirements", {}).get("education", [])
        if not resume_education or not jd_education:
            return {
                "score": 0.0,
                "degree_match": 0.0,
                "field_match": 0.0
            }
        # Assume highest/latest education
        education = resume_education[0]
        resume_degree = self.normalize_degree(
            education.get("degree", "")
        )
        resume_field = self.normalize_field(education.get(
            "field_of_study", ""
        ))
        jd_text = self.normalize_field(
            " ".join(jd_education)
        )
        # Degree Match
        resume_level = self.DEGREE_LEVELS.get(
            resume_degree,
            0
        )
        jd_level = max(
            (
                level
                for degree, level in self.DEGREE_LEVELS.items()
                if degree in jd_text
            ),
            default=0
        )
        if jd_level == 0:
            degree_score = 100.0
        elif resume_level >= jd_level:
            degree_score = 100.0
        else:
            degree_score = 0.0
        # Field Match
        if resume_field and resume_field in jd_text:
            field_score = 100.0
        else:
            field_score = 0.0

        education_score = (
            degree_score * self.DEGREE_WEIGHT +
            field_score * self.FIELD_WEIGHT
        )
        return {
            "score": round(education_score, 2),
            "degree_match": degree_score,
            "field_match": field_score
        }


    def calculate_completeness_score(self):
        score=0
        if self.resume_data.get("name"):
            score+=10
        if self.resume_data.get("emails"):
            score+=10
        if self.resume_data.get("phones"):
            score+=10
        if self.resume_data.get("skills"):
            score+=20
        if self.resume_data.get("projects"):
            score+=15
        if self.resume_data.get("certifications"):
            score+=5
        if self.resume_data.get("education"):
            score+=15
        if self.resume_data.get("experience"):
            score+=15
        return {
            "score":score
        }
    def calculate_final_score(self):
        skill_score=self.calculate_skill_score()
        project_score=self.calculate_project_score()
        experience_score=self.calculate_experience_score()
        education_score=self.calculate_education_score()
        completeness_score=self.calculate_completeness_score()
        final_score = (
            skill_score["score"] * self.SKILL_WEIGHT +
            project_score["score"] * self.PROJECT_WEIGHT +
            experience_score["score"] * self.EXPERIENCE_WEIGHT +
            education_score["score"] * self.EDUCATION_WEIGHT +
            completeness_score["score"] * self.COMPLETENESS_WEIGHT
        )
        return{
            "final_score":round(final_score,2),
            "skill":skill_score,
            "project":project_score,
            "experience":experience_score,
            "education":education_score,
            "completeness":completeness_score
        }
