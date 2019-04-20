import random

print("Hello, sir! I am you new psychotherapist. How do you feel today?")
answer = input()

questions = ["Do you like football?",
             "Do you want to break free?",
             "Do you feel good usually?",
             "Can you stop talking to me?"]

while "bye" not in answer and "Bye" not in answer:
    if "?" in answer:
        print("I don't understand you. Try again")

    elif "bad" in answer or "terrible" in answer:
        print("Why do you take everything so negatively?")
        print("Did you have mental injury in your childhood?")
        answer = input()

        if "yes" in answer or "of course" in answer:
            print("Try to erase the memory of it, at least for the duration of this conversation.")
            questions.append("Did your childhood injury makes you feel bad?")
        elif "no" in answer:
            print("I shall study this moment at the next conversation")
    elif "good" in answer or "excellent" in answer:
        print("I know what is wrong with you, but now i can't to say that")
        questions.append("You are friendly. Am i right?")
        questions.append("Now i want to escape this city. Goodbye")
    elif "yes" in answer or "of course" in answer:
        print("You are very tractable, try to be more independent")
        questions.append("How do you feel about the terrorism?")
    elif "no" in answer:
        print("Why you are so negative again?")
        print("Maybe you need medication? I shall give you a prescription for it")
        questions.append("Oh, god. I feel so bad, I need to sleep. Goodbye")
    else:
        print("Please don't burden me, I feel bad")

    print(random.choice(questions))
    answer = input()
