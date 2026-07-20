from app.parser.resume_parser import parse_resume

text = """
Harika Nagineni

Email: harika@gmail.com
College: ee22b123@iitbbs.ac.in

Phone: +91 9876543210
"""

print(parse_resume(text))



