from app.matcher.skill_matcher import match_skills
from app.scoring.ats_score import calculate_ats_score

def generate_ats_report(resume_data: dict,jd_data: dict)->dict:
    """Generate a complete ATS report by matching resume skills with job description skills and recalculating the ATS score."""
    skill_match_result=match_skills(resume_data,jd_data)
    ats_result=calculate_ats_score(skill_match_result)
    return {
        "ats_score":ats_result["ats_score"],
        "skill_analysis":ats_result["skill_analysis"],
        "matched_skills":skill_match_result["matched_skills"],
        "missing_skills":skill_match_result["missing_skills"],
        "extra_skills":skill_match_result["extra_skills"],
    }
