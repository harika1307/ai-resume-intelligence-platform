import json
from app.schemas.resume_schema import Resume

with open("tests/output.json","r",encoding="utf-8") as f:
    data=json.load(f)
resume=Resume.model_validate(data)

with open("tests/validated_output.json", "w", encoding="utf-8") as f:
    f.write(resume.model_dump_json(indent=4))

print("Resume validated successfully..")