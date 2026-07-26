from app.prompts.resume_parser_prompt import SKILL_DOMAINS
JD_JSON_SCHEMA="""
{
    "skills":[
        {
            "name":"<skill_name>",
            "domain":"<skill_domain>"
        }
    ]
}
"""
def build_jd_prompt(job_description: str)-> str:
    role="""You are an expert ATS parser specializing in extracting structured information from job descriptions.""" 
    task="""Your task is to extract ONLY the technical skills required from the  job description."""
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
    12.Ignore salary,location,eligibility.
    13.Every skill must belong to exactly one domain.
    14.Ignore soft skills.
    15.Ignore company information.
    16. Return each skill only once, even if it appears multiple times in the job description.     
    """
    domains=f"""
    Allowed Skill Domains:
    {", ".join(SKILL_DOMAINS)}
    """
    output_schema=f"""
    Return the output in exactly the following JSON schema:
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
    