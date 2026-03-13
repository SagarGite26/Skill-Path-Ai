from app.skill_graph import load_skill_graph
from app.path_generator import get_learning_path, calculate_total_time, filter_known_skills, suggest_skill

graph = load_skill_graph()

print("\nWelcome to the AI Learning Path Generator\n")

goal = input("Enter the skill you want to learn: ")

# check if skill exists
if goal not in graph:

    suggestions = suggest_skill(graph, goal)

    print("\nSkill not found.")

    if suggestions:
        print("Did you mean:")

        for s in suggestions:
            print("-", s)

    exit()


known_input = input("Enter skills you already know (comma separated, or press Enter if none): ")

if known_input.strip() == "":
    known_skills = []
else:
    known_skills = [skill.strip() for skill in known_input.split(",")]


path = get_learning_path(graph, goal)

filtered_path = filter_known_skills(path, known_skills)

print("\nRecommended Learning Path:\n")

for skill in filtered_path:

    difficulty = graph[skill]["difficulty"]
    hours = graph[skill]["estimated_hours"]

    print(f"{skill} ({difficulty}) - {hours} hours")


total = calculate_total_time(graph, filtered_path)

print("\nTotal Estimated Learning Time:", total, "hours")