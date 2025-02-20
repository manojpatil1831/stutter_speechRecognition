import speech_recognition as sr

def recognize_speech():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        try:
            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            print("Adjusted for ambient noise. Speak now...")
            audio = recognizer.listen(source, timeout=5)  # Capture audio input with a timeout
            print("Audio captured. Processing...")
        except sr.WaitTimeoutError :
            print("Listening timed out. Please speak again.")
            return None

    try:
        # Recognize speech using Google Web Speech API
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.strip().lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return None
    except sr.RequestError as e:
        print(f"Sorry, there was an issue with the speech recognition service: {e}")
        return None

def schonell_spelling_test():
    # List of words for the test (replace with the actual Schonell word list)
    words = [
        "mat", "sit", "run", "dog", "cat", "meat", "tree", "house", "apple", "happy",
        "jump", "green", "water", "flower", "school", "friend", "animal", "basket", "circle", "window"
    ]

    # Initialize variables
    correct_count = 0
    consecutive_mistakes = 0
    raw_score = 0

    print("Welcome to the Schonell Graded Spelling Test!")
    print("You will be given words to spell. Listen carefully to the word and the sentence.")
    print("Say the word out loud. The test will stop after 10 consecutive mistakes.\n")

    # Loop through each word
    for word in words:
        # Provide the word and context
        print(f"Word: {word}")
        sentence = f"We sit on the {word}."  # Example sentence (customize as needed)
        print(f"Sentence: {sentence}")
        print(f"Word again: {word}\n")

        # Keep listening until a valid input is received
        while True:
            print("Please say the word...")
            user_spelling = recognize_speech()

            # Check if the input is valid (i.e., not None)
            if user_spelling is None:
                print("Invalid input. Please try again.\n")
                continue

            # Check if the spelling is correct
            if user_spelling == word:
                correct_count += 1
                consecutive_mistakes = 0  # Reset consecutive mistakes
                print("Correct!\n")
                break  # Move to the next word
            else:
                consecutive_mistakes += 1
                print(f"Incorrect. The correct spelling is '{word}'.\n")

                # Stop the test if 10 consecutive mistakes are made
                if consecutive_mistakes >= 10:
                    print("You have made 10 consecutive mistakes. The test is over.\n")
                    break

        # Stop the test if 10 consecutive mistakes are made
        if consecutive_mistakes >= 10:
            break

    # Calculate raw score and spelling age
    raw_score = correct_count
    spelling_age = calculate_spelling_age(raw_score)

    # Display results
    print("\nTest Results:")
    print(f"Raw Score: {raw_score}")
    print(f"Spelling Age: {spelling_age}")

def calculate_spelling_age(raw_score):
    # Formula: (raw_score / 10) + 5 years, converted to twelfths
    spelling_age_years = (raw_score / 10) + 5
    years = int(spelling_age_years)  # Whole number of years
    months = (spelling_age_years - years) * 12  # Convert decimal to months
    return f"{years} years and {round(months)} months"

# Run the test
schonell_spelling_test()