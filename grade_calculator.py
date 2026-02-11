
def calculate_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number.")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
    if score >= 90:
        print("A")
        return "A"
    elif score >= 80:
        print("B")
        return "B"
    elif score >= 70:
        print("C")
        return "C"
    elif score >= 60:
        print("D")
        return "D"
    else:
        print("F")
        return "F"
    
