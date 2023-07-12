import os
import json

# Get the parent directory path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Define the book groupings
book_groups = [
    ["Jeremiah", "Joel", "Obadiah", "2 Peter"],
    ["Genesis", "Jonah", "3 John", "Malachi","Ruth", "1 Thessalonians", "2 Thessalonians",],
    [ "Amos","Isaiah", "Micah", "1 Timothy"],
    ["1 Chronicles","2 Chronicles",],
    ["Exodus", "Lamentations", "Romans"],
    ["Esther", "Habakkuk", "Haggai", "Nahum", "Numbers","1 Peter", "Zephaniah"],
    ["Deuteronomy", "Hebrews", "Hosea","James", "2 John", "Zechariah"],
    ["Daniel","Ezra","Judges","Nehemiah"],
    ["Job","Luke"],
    ["Acts","John", "1 John"],
    ["Ecclesiastes", "Mark", "1 Samuel", "Song of Solomon"],
    ["Matthew", "2 Samuel"],
    ["Jude", "1 Kings", "Leviticus","Philemon", "Titus"],
    ["Psalms"],
    ["2 Kings", "Proverbs"],
    ["Ephesians", "Ezekiel", "Galatians", "Philippians", "2 Timothy"],
    ["Colossians", "1 Corinthians", "2 Corinthians", "Joshua", "Revelation"],
]

# Load the book JSON files
def load_books():
    books = {}
    book_names = [
        "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges", "Ruth", "1 Samuel",
        "2 Samuel", "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra", "Nehemiah", "Esther", "Job",
        "Psalms", "Proverbs", "Ecclesiastes", "Song of Solomon", "Isaiah", "Jeremiah", "Lamentations", "Ezekiel",
        "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah",
        "Haggai", "Zechariah", "Malachi", "Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians",
        "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians",
        "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter",
        "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"
    ]

    for book_name in book_names:
        filename = os.path.join(parent_dir, f"{book_name}.json")
        with open(filename, "r") as file:
            book_data = json.load(file)
            books[book_name] = book_data

    return books

# Generate the HTML content for each book group
def generate_html():
    books = load_books()

    for group_idx, book_group in enumerate(book_groups):
        # Create a new HTML file for each book group
        file_name = f"group{group_idx + 1}.html"
        with open(file_name, "w") as file:
            # Write the HTML content for the book group
            file.write("<!DOCTYPE html>\n<html>\n<head>\n")
            file.write("<meta charset=\"UTF-8\">\n")
            file.write("<title>The Holy Bible</title>\n")  # Added main title
            file.write("<style>\n")
            file.write("body {\n")
            file.write("  background-color: black;\n")
            file.write("  color: white;\n")
            file.write("  font-family: Arial, sans-serif;\n")
            file.write("}\n")
            file.write("h1 {\n")
            file.write("  color: orange;\n")
            file.write("  text-align: center;\n")
            file.write("}\n")
            file.write("h2 {\n")
            file.write("  color: orange;\n")
            file.write("  text-align: left;\n")
            file.write("}\n")
            file.write(".book-list {\n")
            file.write("  column-count: 3;\n")
            file.write("  column-gap: 20px;\n")
            file.write("}\n")
            file.write(".book {\n")
            file.write("  margin-bottom: 10px;\n")
            file.write("  color: white;\n")
            file.write("}\n")
            file.write(".chapter-list {\n")
            file.write("  column-count: 3;\n")
            file.write("  column-gap: 20px;\n")
            file.write("}\n")
            file.write(".chapter {\n")
            file.write("  margin-bottom: 5px;\n")
            file.write("  color: orange;\n")
            file.write("}\n")
            file.write(".verse {\n")
            file.write("  color: white;\n")
            file.write("}\n")
            file.write(".verse-number {\n")  # Added verse number style
            file.write("  color: white;\n")
            file.write("  font-size: 14px;\n")
            file.write("  margin-right: 5px;\n")
            file.write("}\n")
            file.write(".private-message {\n")  # Added private message style
            file.write("  text-align: center;\n")
            file.write("  color: #FF9900;\n")
            file.write("  margin-top: 20px;\n")
            file.write("  font-size: 12px;\n")
            file.write("}\n")
            file.write(".go-to-top-button {\n")  # Added go to top button style
            file.write("  position: fixed;\n")
            file.write("  bottom: 100px;\n")
            file.write("  right: 20px;\n")
            file.write("  background-color: orange;\n")
            file.write("  color: white;\n")
            file.write("  padding: 10px;\n")
            file.write("  border: none;\n")
            file.write("  cursor: pointer;\n")
            file.write("}\n")
            file.write("</style>\n")
            file.write("</head>\n<body>\n")
            file.write("<h1>The Holy Bible</h1>\n")  # Added main heading

          # Generate the book index HTML for the group
            file.write("<div class=\"book-list\">\n")
            for book_name in book_group:
                file.write(f'<div class="book"><a href="#{book_name.lower()}">{book_name}</a></div>\n')
            file.write("</div>\n")

            # Generate the content for each book in the group
            for book_name in book_group:
                book_data = books[book_name]
                file.write(f'<div class="book" id="{book_name.lower()}">\n')
                file.write(f'<h2>{book_name}</h2>\n')

                # Generate the chapter index HTML for the book
                file.write("<div class=\"chapter-list\">\n")
                for chapter in book_data["chapters"]:
                    file.write(
                        f'<div class="chapter"><a href="#chapter-{book_name.lower()}-{chapter["chapter"]}">Chapter {chapter["chapter"]}</a></div>\n')
                file.write("</div>\n")

                # Generate the content for each chapter in the book
                for chapter in book_data["chapters"]:
                    file.write(f'<div class="chapter" id="chapter-{book_name.lower()}-{chapter["chapter"]}">\n')
                    file.write(f'<h3>Chapter {chapter["chapter"]}</h3>\n')

                    # Generate the verses
                    for verse in chapter["verses"]:
                        file.write(
                            f'<p class="verse"><span class="verse-number">{verse["verse"]}:</span>{verse["text"]}</p>\n')

                    file.write("</div>\n")

                file.write("</div>\n")

            # Add button to go to the top of the screen
            file.write('<button class="go-to-top-button" onclick="window.scrollTo({ top: 0, behavior: \'smooth\' })">Go to Top</button>\n')

            # Add private message in orange at the bottom
            file.write('<p class="private-message">Στην οικογένειά μου και τον Θεό που μας καθοδηγεί. Inspired by a conversation on Degen Saturdays between @AdrianDittmann and @T_Bilderberg. Revelations Chapter 20: 1-3 "And I saw an angel come down from heaven, having the key of the bottomless pit and a great chain in his hand. And he laid hold on the dragon, that old serpent, which is the Devil, and Satan, and bound him a thousand years, And cast him into the bottomless pit, and shut him up, and set a seal upon him, that he should deceive the nations no more, till the thousand years should be fulfilled: and after that he must be loosed a little season". Thank you Arul John who made the JSON files available on GitHub. @Andrew_Kyriacou.</p>\n')

            file.write("</body>\n</html>")

# Run the script to generate HTML files for each book group
generate_html()
