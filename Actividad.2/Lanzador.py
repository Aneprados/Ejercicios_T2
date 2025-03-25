from ConversationFormatter import ConversationFormatter

def main():
    text = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

    # Create an instance of ConversationFormatter
    formatter = ConversationFormatter(text)

    # Format the conversation
    formatted_text = formatter.format_conversation()
    formatted_text = formatted_text.replace("#", "\n")

    # Print the formatted text
    print(formatted_text)

class ConversationFormatter:
    def __init__(self, text):
        self.text = text

    def format_conversation(self):
        # Split the text by '#' to separate the sentences
        sentences = self.text.split('#')
        
        # Capitalize the first letter of the first sentence
        sentences[0] = sentences[0].capitalize() + "..."
        
        # Capitalize the first letter of each subsequent sentence and add a period at the end
        for i in range(1, len(sentences)):
            sentences[i] = sentences[i].capitalize() + "."
        
        # Join the sentences with new lines
        formatted_text = "\n".join(sentences)
        
        return formatted_text

if __name__ == "__main__":
    main()