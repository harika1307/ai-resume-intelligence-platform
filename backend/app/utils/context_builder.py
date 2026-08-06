from typing import Dict
def build_jd_context(jd_data: Dict)->str:
    skills=jd_data.get("skills",[])
    responsibilities=jd_data.get("responsibilities",[])
    requirements=jd_data.get("requirements",{})
    technical=requirements.get("technical",[])
    education=requirements.get("education",[])
    experience=requirements.get("experience",[])
    sections=[]
    if skills:
        skill_lines=[f'{skill["name"]} ({skill["domain"]})' for skill in skills]
        sections.append(
            "Required Skills:\n"+
            "\n".join(skill_lines)
        )
    if responsibilities:
        sections.append(
            "Responsibilities:\n"+
            "\n".join(responsibilities)
        )
    if technical:
        sections.append(
            "Technical Requirements:\n"+
            "\n".join(technical)
        )
    if education:
        sections.append(
            "Education Requirements:\n"+
            "\n".join(education)
        )
    if experience:
        sections.append(
            "Experience Requirements:\n"+
            "\n".join(experience)
        )
    return "\n\n".join(sections)

def build_project_context(project: Dict)->str:
    title=project.get("title","")
    description=project.get("description","")
    skills_used=project.get("skills_used","")
    duration=project.get("duration","")
    sections=[]
    if title:
        sections.append(
            f"Project Title:\n{title}"
        )
    if description:
        sections.append(
            f"Description:\n{description}"
        )
    if skills_used:
        sections.append(
            "Skills Used:\n" +
            "\n".join(skills_used)
        )
    if duration:
        sections.append(
            f"Duration:\n{duration}"
        )
    return "\n\n".join(sections)

def build_experience_context(experience: dict)->str:
    role=experience.get("role","")
    employment_type=experience.get("employment_type","")
    company=experience.get("company","")
    start_date=experience.get("start_date","")
    end_date=experience.get("end_date","")
    
    description=experience.get("description","")
    skills_used=experience.get("skills_used",[])

    if start_date or end_date:
        if experience.get("currently_working"):
            duration = f"{start_date} - Present"
        else:
            duration = f"{start_date} - {end_date}"
    else:
        duration = ""
    sections=[]
    if role:
        sections.append(
            f"Role:\n{role}"
        )
    if employment_type:
        sections.append(
            f"Employment Type:\n{employment_type}"
        )
    if company:
        sections.append(
            f"Company:\n{company}"
        )
    
    if description:
        sections.append(
            f"Description:\n{description}"
        )
    if skills_used:
        sections.append(
            "Skills Used:\n" +
            "\n".join(skills_used)
        )
    if duration:
        sections.append(
            f"Duration:\n{duration}"
        )
    return "\n\n".join(sections)