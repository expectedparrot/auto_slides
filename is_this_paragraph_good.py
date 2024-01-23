from edsl import Scenario, Model, Survey
from edsl.questions import QuestionList, QuestionFreeText, QuestionYesNo

m = Model('gpt-4-1106-preview')

def latex_paragraph_generator(file_path):
    with open(file_path, 'r') as file:
        paragraph = []
        for line in file:
            if line.strip():  # If the line is not blank, add it to the current paragraph
                paragraph.append(line)
            else:  # If the line is blank, yield the current paragraph and start a new one
                if paragraph:  # Check if there is something to yield
                    yield ''.join(paragraph)
                    paragraph = []
        if paragraph:  # Yield any remaining text as a paragraph
            yield ''.join(paragraph)

q_topic = QuestionFreeText(question_text = """
    Here is a paragraph: {{ paragraph }}.
    Does this paragraph contain a strong topic sentence as the first sentence?
    """, 
    question_name = "topic")

q_errors = QuestionFreeText(question_text = """
    Here is a paragraph: {{ paragraph }}.
    Does this paragraph contain any evidence of grammatical or usage errors?
    """, 
    question_name = "errors")

q_reasoning = QuestionFreeText(question_text = """
    Here is a paragraph: {{ paragraph }}.
    Does this paragraph contain any evidence of reasoning errors?
    """, 
    question_name = "reasoning")


scenario = [Scenario({'paragraph':para}) for para in latex_paragraph_generator('example_writing.tex')]
survey = Survey([q_topic, q_errors, q_reasoning])
data = survey.by(m).by(scenario).run()
d = {q.question_name: q.question_text for q in [q_topic, q_errors, q_reasoning]}

data.select( 'scenario.*', 'answer.*').print()

