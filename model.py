def predict_stress(sleep, screen, activity, typing):
    score = 0

    if sleep < 6:
        score += 1
    if screen > 6:
        score += 1
    if activity < 2:
        score += 1
    if typing > 95:
        score += 1

    if score >= 3:
        level = "High"
    elif score == 2:
        level = "Medium"
    else:
        level = "Low"

    return level, score


def get_solutions(level, sleep, screen, activity, typing):
    solutions = []

    if sleep < 6:
        solutions.append("Increase sleep toward 7-8 hours and avoid late-night study sessions.")
    else:
        solutions.append("Maintain a regular sleep schedule to stabilize mood and focus.")

    if screen > 6:
        solutions.append("Reduce screen exposure with 25-30 minute study blocks and short offline breaks.")
    else:
        solutions.append("Your screen time is manageable; keep balancing online work with offline activity.")

    if activity < 2:
        solutions.append("Add at least 20-30 minutes of walking, stretching, or exercise daily.")
    else:
        solutions.append("Keep up your physical activity because it helps regulate stress.")

    if typing > 95:
        solutions.append("Fast typing with long sessions may indicate workload pressure; add short rest breaks.")
    else:
        solutions.append("Your typing load looks moderate; continue pacing your work.")

    if level == "High":
        solutions.append("High stress detected: prioritize sleep, reduce overload, talk to a mentor/friend, and practice breathing exercises.")
    elif level == "Medium":
        solutions.append("Medium stress detected: improve time management, break tasks into smaller chunks, and schedule recovery time.")
    else:
        solutions.append("Low stress detected: keep your current routine and monitor habits to prevent future spikes.")

    return solutions


def build_chart_data(history):
    labels = [f"Attempt {i+1}" for i in range(len(history))]
    scores = [item["score"] for item in history]
    stress_levels = [item["stress"] for item in history]
    sleep = [item["sleep"] for item in history]
    screen = [item["screen"] for item in history]
    activity = [item["activity"] for item in history]

    distribution = {"Low": 0, "Medium": 0, "High": 0}
    for level in stress_levels:
        distribution[level] += 1

    return {
        "labels": labels,
        "scores": scores,
        "stress_levels": stress_levels,
        "sleep": sleep,
        "screen": screen,
        "activity": activity,
        "distribution_labels": list(distribution.keys()),
        "distribution_values": list(distribution.values())
    }
