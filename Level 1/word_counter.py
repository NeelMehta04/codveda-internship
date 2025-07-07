def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"Total words in file: {word_count}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Word Counter")
file_name = input("Enter the filename (e.g., sample.txt): ")
count_words(file_name)
