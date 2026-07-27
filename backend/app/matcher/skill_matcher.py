def build_skill_map(skills: list)-> dict:
    skill_map={}
    for skill in skills:
        normalized_name=skill["name"].strip().lower()
        skill_map[normalized_name]=skill
    return skill_map

def match_skills(resume_data: dict,jd_data: dict)->dict:
    """Compare resume skills with job description skills and return matched,missing,and extra skills."""
    resume_skills=resume_data["skills"]
    jd_skills=jd_data["skills"]
    resume_skill_map=build_skill_map(resume_skills)
    jd_skill_map=build_skill_map(jd_skills)
    missing_skills=[]
    matched_skills=[]
    extra_skills=[]
    for skill_name,skill in jd_skill_map.items():
        if skill_name in resume_skill_map:
            matched_skills.append(resume_skill_map[skill_name])
        else :
            missing_skills.append(skill)
    for skill_name,skill in resume_skill_map.items():
        if skill_name not in jd_skill_map:
            extra_skills.append(skill)
    return{
        "matched_skills":matched_skills,
        "missing_skills":missing_skills,
        "extra_skills":extra_skills
    }