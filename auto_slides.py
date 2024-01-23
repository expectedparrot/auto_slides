import subprocess

import typer 
from edsl.questions import QuestionList, QuestionFreeText, QuestionYesNo
from edsl import Scenario, Model, Survey

app = typer.Typer()

m = Model('gpt-4-1106-preview')

def generate_quiz(content, num_questions):
    scenario = Scenario({'content':content, 'num_questions':num_questions})
    q = QuestionList(
        question_text = """Please create {{num_questions}} asessing student comprehension 
        of the following content: {{content}}.
        """, question_name = "quiz_questions")
    quiz_questions = q.by(m).by(scenario).run()
    return quiz_questions.select('answer.quiz_questions').first() 

def get_slide_titles(topic, num_slides):
    scenario = Scenario({'topic':topic, 'num_slides':num_slides})
    q_slide_titles = QuestionList(
        question_text = """I'm preparing slides on the topic {{ topic }}.
        Please give me titles for {{ num_slides }} slides.
        """, 
        question_name = "slide_titles")
    ideas = q_slide_titles.by(m).by(scenario).run()
    return ideas.select('answer.slide_titles').first()

def get_slide_content(topic, slide_titles, max_bullets = 3):
    q_content = QuestionFreeText(question_text = """
    I am creating slides on {{ topic }}. This slide is about {{ slide_title }}.
    It should consist of {{ max_bullets }} bullet points.
    The format to return is markdown, with the first line being the title, with a '#' heading.
    Code samples should be in code blocks.
    """,
    question_name = "content")
    scenarios = [Scenario({'topic':topic, 'slide_title':slide_title, 'max_bullets':max_bullets}) for slide_title in slide_titles]
    data = q_content.by(m).by(scenarios).run()
    return data.select('answer.content').to_list()

def create_markdown(content, filename):
    def generate_slides():
        for slide_text in content:
            yield slide_text

    with open(filename + ".md", 'w') as f:
        f.write('\n\n'.join(list(generate_slides())))

def write_quiz(topic, content, num_questions, filename):
    questions = generate_quiz(content, num_questions)
    with open(filename + "_quiz.md", 'a') as f:
        f.write(f'\n\n# Quiz on {topic}')
        for index, question in enumerate(questions):
            f.write(f'\n\n{index + 1}: {question}')
    subprocess.run(['pandoc', filename + "_quiz.md", '-o', filename + '_quiz.pdf'])           

@app.command()
def main(filename: str = None, topic: str = None, num_slides: int = None):

    slide_titles = get_slide_titles(topic, num_slides)
    content = get_slide_content(topic, slide_titles)
    write_quiz(topic, content, 5, filename)

    create_markdown(content, filename)

    args = ['-t', 'beamer', filename + ".md", '-o', filename + '.pdf']
    subprocess.run(['pandoc'] + args)
    subprocess.run(['open', filename + '.pdf'])

if __name__ == "__main__":
    app()

