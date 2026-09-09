import re

# Tech stack items categorized into 3 clean rows of 9 items each (27 items)
items = [
    # Row 1: Core Programming & Languages
    ('Python', 'https://skillicons.dev/icons?i=python'),
    ('Java', 'https://skillicons.dev/icons?i=java'),
    ('C', 'https://skillicons.dev/icons?i=c'),
    ('JavaScript', 'https://skillicons.dev/icons?i=js'),
    ('HTML5', 'https://skillicons.dev/icons?i=html'),
    ('CSS3', 'https://skillicons.dev/icons?i=css'),
    ('Git', 'https://skillicons.dev/icons?i=git'),
    ('GitHub', 'https://skillicons.dev/icons?i=github'),
    ('Bash', 'https://skillicons.dev/icons?i=bash'),

    # Row 2: AI, Machine Learning & Data Science
    ('TensorFlow', 'https://skillicons.dev/icons?i=tensorflow'),
    ('PyTorch', 'https://skillicons.dev/icons?i=pytorch'),
    ('Scikit-learn', 'https://skillicons.dev/icons?i=sklearn'),
    ('OpenCV', 'https://skillicons.dev/icons?i=opencv'),
    ('Keras', 'https://cdn.simpleicons.org/keras/D00000'),
    ('Pandas', 'https://cdn.simpleicons.org/pandas/150458'),
    ('NumPy', 'https://cdn.simpleicons.org/numpy/013243'),
    ('AI / Prompts', 'https://skillicons.dev/icons?i=ai'),
    ('Jupyter', 'https://skillicons.dev/icons?i=jupyter'),

    # Row 3: Frameworks, Platforms & Tools
    ('FastAPI', 'https://skillicons.dev/icons?i=fastapi'),
    ('Streamlit', 'https://skillicons.dev/icons?i=streamlit'),
    ('Docker', 'https://skillicons.dev/icons?i=docker'),
    ('VS Code', 'https://skillicons.dev/icons?i=vscode'),
    ('MySQL', 'https://skillicons.dev/icons?i=mysql'),
    ('Canva', 'https://skillicons.dev/icons?i=canva'),
    ('Linux', 'https://skillicons.dev/icons?i=linux'),
    ('Postman', 'https://skillicons.dev/icons?i=postman'),
    ('PowerShell', 'https://skillicons.dev/icons?i=powershell')
]

def generate_table_html():
    cols_per_row = 9
    html = '<div align="center">\n    <table align="center">\n'
    for i, (name, icon_url) in enumerate(items):
        if i % cols_per_row == 0:
            html += '        <tr>\n'
        
        html += f'            <td align="center" width="96">\n'
        html += f'                <img src="{icon_url}" width="48" height="48" alt="{name}" />\n'
        html += f'                <br><sub><b>{name}</b></sub>\n'
        html += f'            </td>\n'
        
        if i % cols_per_row == (cols_per_row - 1) or i == len(items) - 1:
            html += '        </tr>\n'
            
    html += '    </table>\n</div>'
    return html

if __name__ == '__main__':
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    start_tag = '<!-- TECH_STACK_START -->'
    end_tag = '<!-- TECH_STACK_END -->'

    if start_tag in content and end_tag in content:
        start_idx = content.find(start_tag) + len(start_tag)
        end_idx = content.find(end_tag)
        table_html = '\n' + generate_table_html() + '\n'
        new_content = content[:start_idx] + table_html + content[end_idx:]
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('README.md tech stack table updated successfully!')
    else:
        print('Tech stack tags not found in README.md. Generated HTML:\n')
        print(generate_table_html())
