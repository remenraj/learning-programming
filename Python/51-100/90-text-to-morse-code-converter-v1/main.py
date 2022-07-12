# Text to Morse Code Converter

import re
import pandas as pd


def morse_code_text_converter(text: str) -> str:
    """Converts the text into morse code and returns it"""
    morse_df = pd.read_csv(r"learning-programming\Python\51-100\90-text-to-morse-code-converter\morse.csv", header=None)
    morse_df.columns = ["symbol", "code"]
    
    morse_code = ""
    
    for i in range(len(text)):
        if text[i] == " ":
            continue
        morse_code += (morse_df.code[morse_df.symbol == text[i]].values[0] + " ")
    
    return morse_code

def main():
    """Main function"""
    
    is_continue = True
    while is_continue:
        user_input = input("Enter a String: ").upper()

        # check for valid input
        while not re.match(pattern="^[A-Z0-9 ]*$", string=user_input):
            user_input = input("Enter a valid string: ").upper()
        
        print(morse_code_text_converter(text=user_input))
        
        prompt = input("Do you want to try again? Enter 'yes' or 'no': ").lower()
        if not prompt in ["yes", "y", "true", "t"]:
            is_continue = False
    

if __name__ == "__main__":
    main()