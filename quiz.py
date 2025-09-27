import csv
import random

def load_questions(filename="questions.csv"):
    """Load questions and answers from a CSV file."""
    questions = []
    with open(filename, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            q = row["question"].strip()
            a = row["answer"].strip()
            questions.append((q, a))
    return questions

def run_quiz(questions):
    """Ask questions in random order and keep score."""
    score = 0
    total = len(questions)
    random.shuffle(questions)

    print("\nWelcome to the Flashcard Quiz!")
    print(f"There are {total} questions.\n")

    for idx, (q, a) in enumerate(questions, start=1):
        print(f"Q{idx}: {q}")
        user = input("Your answer: ").strip()
        if user.lower() == a.lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect. Correct answer: {a}\n")

    print("Quiz finished!")
    print(f"Your score: {score}/{total}")
    percent = (score / total) * 100
    print(f"Percentage: {percent:.1f}%")

def main():
    questions = load_questions()
    if not questions:
        print("No questions found. Please add entries to questions.csv")
        return
    run_quiz(questions)

if __name__ == "__main__":
    main()
