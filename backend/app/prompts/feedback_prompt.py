import json

def build_feedback_prompt(resume_json: dict,jd_json: dict,ats_report: dict)->str:
    prompt=f"""
You are an expert ATS recruiter,senior hiring manager, and career coach.
Your task is to analyze a candidate's resume against the given job description and ATS analysis.
=======
RESUME
======
{json.dumps(resume_json,indent=2)}

======
JOB DESCRIPTION
======
{json.dumps(jd_json,indent=2)}

======
ATS ANAlysis
======
{json.dumps(ats_report,indent=2)}

======
YOUR TASK
======
Provide detailed,constructive, and actionable feedback.

Evaluate:
1.Overall resume quality.
2.Resume strengths.
3.Resume weaknesses.
4.Missing technical skills.
5.Resume improvement suggestions.
6.Keyword optimization suggestions.
7.Whether projects align with the role.
8.Whether work experience is sufficient.
9.Whether education is relevant.
10.Generate interview questions based on the resume and JD.

Do NOT invent experience.
Do NOT fabricate projects.
Only use the information provided.
Return ONLY valid JSON.
Output Schema:
{{
    "overall_feedback":"...",
    "strengths":[
        "...",
        "..."
    ],
    "weaknesses":[
        "...",
        "..."
    ],
    "resume_improvements":[
        "...",
        "..."
    ],
    "keyword_suggestions":[
        "...",
        "..."
    ],
    "missing_skill_suggestions":[
        "...",
        "..."
    ],
    "interview_questions":[
        "...",
        "...",
        "...",
        "...",
        "..."
    ]
}}
Return ONLY JSON.
Do not include markdown.
Do not inlude explanations outside JSON.
"""
    return prompt