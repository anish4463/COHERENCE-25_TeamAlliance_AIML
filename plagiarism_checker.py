from difflib import SequenceMatcher

def check_plagiarism(text, known_texts):
    """Compare text against known samples for plagiarism."""
    for known in known_texts:
        similarity = SequenceMatcher(None, text, known).ratio()
        if similarity > 0.8:  # If similarity > 80%, flag as potential plagiarism
            return True
    return False
