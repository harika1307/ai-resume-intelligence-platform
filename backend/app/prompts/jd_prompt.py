from app.prompts.resume_parser_prompt import SKILL_DOMAINS

JD_JSON_SCHEMA="""
{
    "skills":[
        {
            "name":"<skill_name>",
            "domain":"<skill_domain>"
        }
    ],
    "responsibilities":[],
    "requirements": {
        "technical": [],
        "education": [],
        "experience": []
    }
}
"""
def build_jd_prompt(job_description: str)-> str:
    role="""You are an expert ATS parser specializing in extracting structured information from job descriptions.""" 
    task = """
    Your task is to extract structured information from the job description.Preserve the original meaning while rewriting into concise structured statements.
    Extract:
    1. Technical skills required for the role.
    2. Key responsibilities of the role.
    3. Requirements, including:
        • Technical requirements
        • Educational requirements
        • Experience requirements
    Ignore information unrelated to evaluating a candidate such as salary, company overview, benefits, office location, and application instructions.
    """
    rules="""Rules:
    1.Return ONLY valid JSON.
    2.Do not return markdown.
    3.Do not explain anything.
    4.Use only the provided skill domains.
    5.Do not invent information.
    6.Normalize common abbreviations when their meaning is clear.
    Examples:
    - JS → JavaScript
    - Py → Python
    - C++ → C++
    - Node → Node.js
    Do not normalize if the meaning is ambiguous.
    
    
    7.Use closest matching value from the allowed skill domains.
    8.Do not omit any keys from JSON schema.
    9.Return every key in the schema even if it is empty.
    10.Maintain order of keys exactly as shown in the schema.
    
    11.Return valid JSON that can be parsed directly using json.loads().
    12. Ignore salary, location, company overview, benefits, application process, equal opportunity statements, and other non-evaluation information.
    13.Every skill must belong to exactly one domain.
    14.Ignore soft skills unless they are explicitly listed as mandatory technical requirements.
    15.Ignore company information.
    16. Return each skill only once, even if it appears multiple times in the job description.
    17. Responsibilities should describe the actual work expected from the candidate.
    18. Populate the requirements object as follows:
    - technical: technical requirements, tools, technologies and certifications.
    - education: degree, field of study or educational qualifications.
    - experience: years of experience, prior work experience or industry experience requirements.
    19. Do not duplicate information across skills, responsibilities, and requirements.
    20. Responsibilities and requirements should be concise but preserve the original meaning. 
    21. If a section is not present in the job description, return an empty list for that section instead of inventing information.    
    """
    domains=f"""
    Allowed Skill Domains:
    {", ".join(SKILL_DOMAINS)}
    """
    output_schema = f"""
    Populate the JSON schema as follows:
    - skills:
    Extract all technical skills and assign the closest matching domain.
    - responsibilities:
    Extract the main responsibilities of the role as short statements.
    - requirements:
    Populate the nested fields:

        - technical:
        Technical skills, tools, frameworks, certifications or technologies.

        - education:
        Required degree, field of study or educational qualifications.

        - experience:
        Years of experience, industry experience or role-specific experience.
    Return exactly the following JSON schema:
    {JD_JSON_SCHEMA}
    """
    job_description_section=f"""
    Job Description:
    {job_description}
    """
    final_instruction="""
    Return ONLY the JSON object.
    Do not include markdown.
    Do not wrap the JSON inside ```.
    Do not include explanations before or after the JSON
    """
    prompt="\n\n".join([
        role,
        task,
        rules,
        domains,
        output_schema,
        job_description_section,
        final_instruction
    ])
    return prompt
    