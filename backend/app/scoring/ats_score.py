
def calculate_ats_score(skill_match_result: dict)->dict:
    """Calculate the ATS score and skill analysis based on the skill matching results."""
    matched=len(skill_match_result["matched_skills"])
    missing=len(skill_match_result["missing_skills"])
    extra=len(skill_match_result["extra_skills"])
    total_required=matched+missing
    if total_required==0:
        skill_match_percentage=0
    else:
        skill_match_percentage=round((matched/total_required)*100,2)
    ats_score=skill_match_percentage
    skill_analysis={
        "matched_skills":matched,
        "missing_skills":missing,
        "extra_skills":extra,
        "total_required_skills":total_required,
        "skill_match_percentage":skill_match_percentage
    }
    return{
        "ats_score":ats_score,
        "skill_analysis":skill_analysis
    }
