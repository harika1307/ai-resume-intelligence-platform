from backend.app.schemas.resume_json_schema import (RESUME_JSON_SCHEMA,SKILL_DOMAINS)

def build_resume_parser_prompt(resume_text: str)->str:
    role="""You are an expert Applicant Tracking System (ATS) resume parser.""" 
    task="""Your task is to accurately extract structured information from resumes into the provided JSON schema."""
    rules="""Rules:
    1.Return ONLY valid JSON.
    2.Do not return markdown.
    3.Do not explain anything.
    4.If information is missing,use an empty string.
    5.If a list is missing, return [].
    6.Use only the provided skill domains.
    7.Do not invent information.
    8.Normalize common abbreviations when their meaning is clear.
    Examples:
    - JS → JavaScript
    - Py → Python
    - C++ → C++
    - Node → Node.js
    Do not normalize if the meaning is ambiguous.
    9.preserve original wording for descriptions instead of rewriting them.
    10.Do not infer dates,companies,or degrees that aren't explicitly present.
    10.Use closest matching value from the allowed skill domains.
    11.Do not omit any keys from JSON schema.
    12.Return every key in the schema even if it is empty.
    13.Maintain order of keys exactly as shown in the schema.
    14.Preserve original capitalization of names,companies,institutions,and project titles.
    15.Return valid JSON that can be parsed directly using json.loads().
    """
    domains=f"""
    Allowed Skill Domains:
    {", ".join(SKILL_DOMAINS)}
    """
    output_schema=f"""
    Output  JSON Schema in exactly this format:
    {RESUME_JSON_SCHEMA}
    """
    resume=f"""
    Resume:
    {resume_text}
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
        resume,
        final_instruction
    ])
    return prompt