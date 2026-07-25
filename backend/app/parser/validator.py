REQUIRED_KEYS={
        "skills":[],
        "education":[],
        "experience":[],
        "projects":[],
        "certifications":[]
    }
EXPECTED_TYPES={
    "skills":list,
    "education":list,
    "experience":list,
    "projects":list,
    "certifications":list,
}
def validate_ai_response(ai_data: dict)->dict:

    for key,default in REQUIRED_KEYS.items():
        ai_data.setdefault(key,default)
    for key,expected_type in EXPECTED_TYPES.items():
        if not isinstance(ai_data[key],expected_type):
            ai_data[key]=REQUIRED_KEYS[key]
    return ai_data