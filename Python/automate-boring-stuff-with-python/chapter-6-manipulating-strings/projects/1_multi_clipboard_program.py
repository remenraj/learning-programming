#! python3
# 1_multi_clipboard_program.py: A multi-clipboard program.

import pyperclip, sys

def main() -> None:
    """Main function"""
    
    TEXT = {
        "agree": """Yes, I agree. That sounds fine to me.""",
        "busy": """Sorry, can we do this later this week or next week?""",
        "upsell": """Would you consider making this a monthly donation?""",
    }

    
    if len(sys.argv) < 2:
        
        
        print('Usage: python 1_multi_clipboard_program.py [keyphrase] - copy phrase text')
        sys.exit()
    
    # first command line arg is the keyphrase
    keyphrase = sys.argv[1] 
    
    if keyphrase in TEXT:
        
        pyperclip.copy(TEXT[keyphrase])
        print('Text for ' + keyphrase + ' copied to clipboard.')
        
    else:
        
        print('There is no text for ' + keyphrase)
    
    
if __name__ == "__main__":
    main()