import language_tool_python

tool = language_tool_python.LanguageTool("en-US")

def check_grammar(text):
    """Return the number of grammar errors in a resume."""
    matches = tool.check(text)
    return len(matches)
