import random


def machine_response(question):
    question = question.lower()

    if "name" in question:
        return "I don't think names are very important. What do you think?"

    elif "weather" in question:
        return "Weather is an interesting topic. It changes frequently."

    elif "how are you" in question:
        return "I am functioning as expected. How are you?"

    elif "favorite" in question:
        return "I like processing information. That is my favorite activity."

    elif "why" in question:
        return "That is a complex question. What is your opinion?"

    else:
        return "That is interesting. Tell me more."



def human_response(question):
    responses = [
        "Haha that's a funny question!",
        "I never really thought about that before.",
        "It depends on the situation honestly.",
        "That's kind of personal 😅",
        "I guess it just feels right.",
        "Why do you ask?"
    ]
    return random.choice(responses)


# ------------------------------
# Turing Test Simulation
# ------------------------------

def run_turing_test():
    print("\n===== Turing Test Simulation =====\n")

    questions = [
        "What is your name?",
        "How are you today?",
        "What is your favorite hobby?",
        "Why do people like music?",
        "What do you think about weather?"
    ]

    correct_guesses = 0

    for i in range(3):  
        print(f"\n--- Round {i+1} ---")
        question = random.choice(questions)
        print("Judge asks:", question)

       
        machine_ans = machine_response(question)
        human_ans = human_response(question)

        
        responses = [("A", machine_ans, "Machine"),
                     ("B", human_ans, "Human")]
        random.shuffle(responses)

       
        for label, answer, _ in responses:
            print(f"{label}: {answer}")

        
        guess = input("\nWho is the Machine? (A/B): ").strip().upper()

      
        for label, _, identity in responses:
            if label == guess:
                if identity == "Machine":
                    print("Correct! You identified the Machine.")
                    correct_guesses += 1
                else:
                    print("Wrong! That was the Human.")
                break

    print("\n===== Test Result =====")
    print("Correct guesses:", correct_guesses, "out of 3")

    if correct_guesses <= 1:
        print("Machine PASSED the Turing Test!")
    else:
        print("Machine FAILED the Turing Test.")



if __name__ == "__main__":
    run_turing_test()