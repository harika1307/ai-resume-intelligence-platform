ALLOWED_TYPES=[
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
]
MAX_FILE_SIZE=5*10254*1024
PROFILE_PARTS=4

WORD_COUNT_SCORES={
    1:1,
    2:5,
    3:4,
    4:3,
}

TOP_LINES_TO_CHECK=10
STOP_WORDS={
    "name",
    "resume",
    "contact",
    "profile",
    "summary",
    "curriculum",
    "vitae",
    "cv",
    "about"
}
EDUCATION_KEYWORDS={
    "university",
    "college",
    "institute",
    "school",
    "bachelor",
    "master",
    "phd",
    "technology",
    "engineering",
    "degree"
}
LINK_KEYWORDS={
    "github",
    "linkedin",
    "leetcode",
    "portfolio",
    "website",
    "http",
    "https",
    "www",
    "email"
}

SECTION_HEADERS={
    "education",
    "experience",
    "projects",
    "certification",
    "achievements",
    "languages",
    "interests",
    "publications",
    "summary"
}

SKILL_SECTION_HEADERS={
    "skills",
    "technical skills",
    "core competencies",
    "technologies",
    "tech stack"
}

