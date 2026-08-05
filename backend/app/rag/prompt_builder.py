from typing import List
SYSTEM_PROMPT="""You are an expert ATS Resume Assistant."""
def _format_context(documents: List[str])->str:
    context="\n\n-------------\n\n".join(documents)
    return context
               
def build_chat_prompt(query: str,documents: List[str])->str:
    
    
    
    instructions="""
    Use ONLY the provided resume context to answer the user's question.
    Do not make assumptions or invent information that is not present in the provided context.
    Do not use external knowledge or prior knowledge.
    If the provided context does not contain enough information, clearly state that the available information is insufficient.
    Provide concise, accurate, and well-structured answers.
    """
    context=f"""Resume context:
    {_format_context(documents)}
    """
    question=f"""
        User Question:
        {query}
        Answer:

        """
        
    
    prompt="\n\n".join([
        SYSTEM_PROMPT,
        instructions,
        context,
        question
    ])
    return prompt

def build_resume_summary_prompt(documents: List[str])->str:
    
    instructions=f"""
    Generate a structured resume summary from the given context.
    Include relevant sections such as:
    • Professional Summary
    • Technical Skills
    • Projects
    • Experience
    • Education
    • Certifications
    • Achievements
    Only include sections that contain information from the provided resume context.
    Do not create empty sections.
    """
    context=f"""Resume context:
    {_format_context(documents)}
    """
    prompt="\n\n".join([
        SYSTEM_PROMPT,
        instructions,
        context,
        "Resume Summary:"
    ])
    return prompt

def build_skill_gap_prompt(
        resume_documents: List[str],job_description: str
)->str:
    
    instructions=f"""
    Use ONLY the provided resume context and job description.
    Compare the candidate's qualifications with the job requirements.
    Generate your response using the following sections:
    1. Matching Skills
    2. Missing Skills
    3. Candidate Strengths
    4. Areas for Improvement
    5. Personalized Recommendations
    Do not calculate an ATS score.
    Do not invent qualifications that are not present.
    If information is insufficient, clearly state it.
    """
    context=f"""
    Resume context:
    {_format_context(resume_documents)}
    """
    job_description_section=f"""
    Job Description:
    {job_description}
    """
    prompt="\n\n".join([
        SYSTEM_PROMPT,
        instructions,
        context,
        job_description_section,
        "Response:"
    ])
    return prompt

def build_resume_analysis_prompt(resume_documents: List[str])->str:
    instructions="""
    Analyze the candidate's resume using ONLY the provided resume context.
    Generate a structured analysis with the following sections:
    1. Overall Assessment
    2. Technical Skills Assessment
    3. Project Assessment
    4. Experience Assessment
    5. Education Assessment
    6. Resume Strengths
    7. Areas for Improvement
    8. Suggestions for Improvement
    Do not invent information that is not present.
    If a section cannot be evaluated due to insufficient information, state that clearly.
    Keep the analysis professional and concise.
    """
    context=f"""
    Resume context:
    {_format_context(resume_documents)}
    """
    prompt="\n\n".join([
        SYSTEM_PROMPT,
        instructions,
        context,
        "Response:"
    ])

def build_interview_prompt(resume_documents: List[str],job_description: str)->str:
    role="""You are an expert technical interviewer."""
    instructions="""
    Use ONLY the provided resume context and job description.
    Generate interview questions tailored to the candidate and the target job role.
    Organize the response into the following sections:
    1. Technical Questions (5)
    2. Project-Based Questions (3)
    3. Behavioral Questions (3)
    4. Job-Specific Questions (3)
    5. Follow-up Questions (2)
    For each question provide:
    • The interview question
    • Key points expected in an excellent answer
    Do not provide the complete answer.
    Prioritize questions based on the job description and the candidate's most relevant skills and projects.
    If there is a mismatch between the resume and the job description,
    focus questions on the job-relevant skills while also highlighting important skill gaps.
    Do not generate questions unrelated to the provided resume or job description.
    """
    context=f"""
    Resume context:
    {_format_context(resume_documents)}
    """
    job_description_section=f"""
    Job Description:
    {job_description}
    """
    prompt="\n\n".join([
        role,
        instructions,
        context,
        job_description_section,
        "Response:"
    ])
    return prompt

    