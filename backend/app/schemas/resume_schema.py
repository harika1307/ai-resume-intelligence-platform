SKILL_DOMAINS=[
    "programming",
    "Web Development",
    "Backend Development",
    "Frontend Development",
    "Mobile Development",
    "Machine Learning",
    "Deep Learning",
    "Computer Vision",
    "Natural Language Processing",
    "Data Science",
    "Data Engineering",
    "Cloud Engineering",
    "DevOps",
    "Cybersecurity",
    "Database",
    "Operating Systems",
    "Networking",
    "Embedded Engineering",
    "Software Engineering",
    "Testing",
    "Other"
]

RESUME_JSON_SCHEMA = """
{
    "skills": [
        {
            "name": "",
            "domain": "",
            "source": ""
        }
    ],

    "education": [
        {
            "degree": "",
            "field_of_study": "",
            "institution": "",
            "location": "",
            "cgpa": "",
            "start_year": "",
            "end_year": ""
        }
    ],

    "experience": [
        {
            "company": "",
            "role": "",
            "employment_type": "",
            "location": "",
            "start_date": "",
            "end_date": "",
            "currently_working": false,
            "description": "",
            "skills_used": []
        }
    ],

    "projects": [
        {
            "title": "",
            "description": "",
            "skills_used": [],
            "github": "",
            "live_demo": "",
            "duration": ""
        }
    ],

    "certifications": [
        {
            "name": "",
            "issuer": "",
            "issue_date": "",
            "credential_id": "",
            "credential_url": ""
        }
    ]
}
"""