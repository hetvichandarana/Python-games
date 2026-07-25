import random

# Dictionary containing category, word and hint
game_data = {
    "Fruit": [
        ("apple", "A common red or green fruit."),
        ("banana", "A long yellow fruit."),
        ("mango", "The national fruit of India."),
        ("orange", "A citrus fruit rich in Vitamin C."),
        ("grapes", "Small fruits that grow in bunches."),
        ("papaya", "An orange fruit with black seeds."),
        ("pineapple", "A tropical fruit with a spiky outer skin."),
        ("watermelon", "A large fruit with green skin and red flesh."),
        ("guava", "A fruit with many small seeds inside."),
        ("kiwi", "A small brown fruit with green flesh.")
    ],

    "Animal": [
        ("elephant", "The largest land animal."),
        ("tiger", "India's national animal."),
        ("giraffe", "The tallest animal."),
        ("rabbit", "A small animal with long ears."),
        ("monkey", "An animal that loves climbing trees."),
        ("zebra", "An animal with black and white stripes."),
        ("kangaroo", "An animal that carries its baby in a pouch."),
        ("dolphin", "A very intelligent sea animal."),
        ("penguin", "A bird that cannot fly but can swim."),
        ("camel", "Known as the ship of the desert.")
    ],

    "Programming": [
        ("python", "A beginner-friendly programming language."),
        ("java", "A popular object-oriented language."),
        ("variable", "Stores data in a program."),
        ("function", "A reusable block of code."),
        ("loop", "Repeats a block of code."),
        ("string", "A sequence of characters."),
        ("integer", "Represents whole numbers."),
        ("boolean", "Can be either True or False."),
        ("compiler", "Converts source code into machine code."),
        ("debugging", "Finding and fixing errors in code.")
    ],

    "Technology": [
        ("computer", "An electronic machine used for many tasks."),
        ("keyboard", "Used to type on a computer."),
        ("monitor", "Displays the computer screen."),
        ("printer", "Produces a paper copy."),
        ("internet", "Connects computers worldwide."),
        ("browser", "Used to open websites."),
        ("laptop", "A portable computer."),
        ("software", "Programs that run on a computer."),
        ("hardware", "Physical parts of a computer."),
        ("database", "Stores and organizes information.")
    ],

    "Education": [
        ("school", "A place where students learn."),
        ("teacher", "Helps students learn."),
        ("student", "A person who studies."),
        ("library", "A place full of books."),
        ("notebook", "Used for writing notes."),
        ("homework", "Work given by teachers."),
        ("classroom", "Where lessons are taught."),
        ("science", "The study of the natural world."),
        ("mathematics", "The subject of numbers."),
        ("exam", "Tests a student's knowledge.")
    ],

    "Country": [
        ("india", "The country known for the Taj Mahal."),
        ("canada", "A country famous for maple syrup."),
        ("japan", "The Land of the Rising Sun."),
        ("brazil", "Home to the Amazon Rainforest."),
        ("australia", "Known for kangaroos."),
        ("france", "The Eiffel Tower is here."),
        ("germany", "Known for engineering and cars."),
        ("italy", "Famous for pizza and pasta."),
        ("nepal", "Home of Mount Everest."),
        ("china", "The Great Wall is located here.")
    ],

    "Sports": [
        ("cricket", "India's most popular sport."),
        ("football", "Also called soccer in some countries."),
        ("tennis", "Played with a racket."),
        ("hockey", "India's national sport (traditionally)."),
        ("badminton", "Played with a shuttlecock."),
        ("volleyball", "Played over a net."),
        ("basketball", "Played using a hoop."),
        ("swimming", "A water sport."),
        ("boxing", "A combat sport using gloves."),
        ("chess", "A game of strategy with 64 squares.")
    ],

    "Vehicle": [
        ("bicycle", "Has two wheels and no engine."),
        ("motorcycle", "A two-wheeled motor vehicle."),
        ("airplane", "Flies in the sky."),
        ("helicopter", "Can take off vertically."),
        ("tractor", "Used on farms."),
        ("ambulance", "Carries sick or injured people."),
        ("bus", "Carries many passengers."),
        ("train", "Runs on railway tracks."),
        ("submarine", "Travels underwater."),
        ("scooter", "A lightweight two-wheeler.")
    ]
}

last_word = ""

print("===== Welcome to Hangman Game =====")

while True:

    # Choose a random category
    category = random.choice(list(game_data.keys()))

    # Choose a random word and hint from that category
    word, hint = random.choice(game_data[category])

    # Avoid repeating the same word
    while word == last_word:
        category = random.choice(list(game_data.keys()))
        word, hint = random.choice(game_data[category])

    last_word = word

    guessed = set()

    # Chances based on word length
    chances = len(word) + 2

    print("\nCategory :", category)
    print("Hint     :", hint)

    # One complete game
    while chances > 0:

        display = ""

        # Create the hidden word
        for letter in word:
            if letter in guessed:
                display += letter
            else:
                display += "_"

        print("\nWord :", " ".join(display))
        print("Guessed Letters :", " ".join(sorted(guessed)))
        print("Chances Left :", chances)

        # Check if player won
        if display == word:
            print("\n🎉 Congratulations! You guessed the word.")
            break

        guess = input("Enter one letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet.")
            continue

        # Already guessed
        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)

        # Correct or wrong
        if guess in word:
            print("✅ Correct!")
        else:
            chances -= 1
            print("❌ Wrong!")

    # If player loses
    if chances == 0:
        print("\n😔 You Lost!")
        print("The word was:", word)

    # Play again
    choice = input("\nPlay Again? (yes/no): ").lower().strip()

    if choice != "yes":
        print("\nThanks for playing!")
        break
