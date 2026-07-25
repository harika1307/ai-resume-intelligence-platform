# import spacy

# nlp=spacy.load("en_core_web_sm")

# text = """
# Harika Nagineni is a final year Electrical Engineering student at IIT Bhubaneswar.
# She has experience in Python, Machine Learning and Deep Learning.
# """
# doc=nlp(text)

# print(type(doc))
# print(doc)
# print(len(doc))

# # for token in doc:
# #     print(f"Token:{token.text}")

# for ent in doc.ents:
#     print(ent.text,ent.label_)