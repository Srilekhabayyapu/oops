def get_grade_and_comment(mark):
    """Return grade and comment based on a mark (0-100)."""
    if mark >= 90:
        return "A+", "Excellent work!"
    elif mark >= 80:
        return "A", "Very good job!"
    elif mark >= 70:
        return "B", "Good, but room for improvement."
    elif mark >= 60:
        return "C", "Fair — you should aim higher."
    elif mark >= 50:
        return "D", "Passable, but weak."
    else:
        return "F", "Fail — you need to work hard."

def main():
    results = []  # will store tuples like (student_name, mark, grade, comment)
    while True:
        student_name = input("Enter student name (or type 'exit' to finish): ")
        if student_name.lower() == 'exit':
            break
        
        try:
            mark = float(input(f"Enter marks for {student_name} (0-100): "))
            if mark < 0 or mark > 100:
                print("Invalid mark — must be between 0 and 100. Try again.")
                continue
        except ValueError:
            print("Invalid input — please enter a number. Try again.")
            continue
        
        grade, comment = get_grade_and_comment(mark)
        results.append((student_name, mark, grade, comment))
        print(f"Student: {student_name} | Mark: {mark} | Grade: {grade} | Comment: {comment}")
        print("-" * 40)
    
    # After loop ends, you can show all results:
    print("\nAll results:")
    for entry in results:
        print(f"{entry[0]}: Mark={entry[1]}, Grade={entry[2]}, Comment={entry[3]}")
    
    # Optionally return results for further processing
    return results

if __name__ == "__main__":
    main()
