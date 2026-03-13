import json
from collections import Counter


def load_jobs():

    with open("data/job_descriptions.json") as f:
        return json.load(f)


def get_related_skills_from_path(skill_path):

    jobs = load_jobs()

    skill_keywords = [
        "Python","Java","C++","SQL","TensorFlow","PyTorch",
        "Machine Learning","Deep Learning","Statistics",
        "Data Visualization","Docker","Kubernetes",
        "AWS","React","Node.js","Spring Boot",
        "REST APIs","MongoDB","PostgreSQL","Microservices",
        "Git","Pandas","NumPy","Scikit-learn",
        "Cybersecurity","Blockchain","Kotlin","Swift"
    ]

    related = []

    for role, descriptions in jobs.items():

        for text in descriptions:

            for skill in skill_path:

                if skill.lower() in text.lower():

                    for keyword in skill_keywords:

                        if keyword.lower() in text.lower() and keyword not in skill_path:

                            related.append(keyword)

    counter = Counter(related)

    # get top skills with frequency
    results = counter.most_common(10)

    # filter skills already in path
    filtered = [(skill,count) for skill,count in results if skill not in skill_path]

    return filtered[:5]