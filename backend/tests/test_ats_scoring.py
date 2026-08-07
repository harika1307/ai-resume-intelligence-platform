from app.ats.scoring_engine import ATSScoringEngine
from app.matcher.semantic_matcher import SemanticSkillMatcher
from app.rag.embedding import EmbeddingService
from tests.sample_resume import resume_data
from tests.sample_jd import jd_data

embedding_service=EmbeddingService()
matcher=SemanticSkillMatcher(embedding_service=embedding_service)
skill_match_result=matcher.match_skills(resume_data,jd_data)
print("=" * 60)
print("Skill Match Result")
print("=" * 60)
print(skill_match_result)
engine=ATSScoringEngine(resume_data,jd_data,skill_match_result,embedding_service)

result=engine.calculate_final_score()
print()

print("=" * 60)
print("ATS Score")
print("=" * 60)
print(result)