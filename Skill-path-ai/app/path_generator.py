def get_learning_path(graph, goal):

    path = []
    visited = set()

    def dfs(skill):

        if skill in visited:
            return

        visited.add(skill)

        if skill not in graph:
            return

        for prereq in graph[skill].get("prerequisites", []):
            dfs(prereq)

        path.append(skill)

    dfs(goal)

    return path


def calculate_total_time(graph, path):

    total_time = 0

    for skill in path:
        if skill in graph:
            total_time += graph[skill].get("estimated_hours", 0)

    return total_time


def filter_known_skills(path, known_skills):

    return [skill for skill in path if skill not in known_skills]