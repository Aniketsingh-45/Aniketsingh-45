import re

# Categorized tech stack data
# Linux, Bash, and Postman removed per requirements
# Seaborn, XGBoost, Jupyter, and Streamlit verified and active
categories = [
    ('Artificial Intelligence, Machine Learning & Data Science', 'https://cdn.jsdelivr.net/gh/Tarikul-Islam-Anik/Animated-Fluent-Emojis@master/Emojis/Smilies/Robot.png', [
        ('PyTorch', 'https://skillicons.dev/icons?i=pytorch'),
        ('TensorFlow', 'https://skillicons.dev/icons?i=tensorflow'),
        ('Scikit-learn', 'https://skillicons.dev/icons?i=sklearn'),
        ('XGBoost', 'https://raw.githubusercontent.com/dmlc/dmlc.github.io/master/img/logo-m/xgboost.png'),
        ('Keras', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/keras/keras-original.svg'),
        ('Pandas', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg'),
        ('NumPy', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg'),
        ('Seaborn', 'https://raw.githubusercontent.com/mwaskom/seaborn/master/doc/_static/logo-mark-darkbg.svg'),
        ('OpenCV', 'https://skillicons.dev/icons?i=opencv'),
        ('Jupyter', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg')
    ]),
    ('Programming Languages & Modern Web Architecture', 'https://cdn.jsdelivr.net/gh/Tarikul-Islam-Anik/Animated-Fluent-Emojis@master/Emojis/Objects/Laptop.png', [
        ('Python', 'https://skillicons.dev/icons?i=python'),
        ('Java', 'https://skillicons.dev/icons?i=java'),
        ('C', 'https://skillicons.dev/icons?i=c'),
        ('JavaScript', 'https://skillicons.dev/icons?i=js'),
        ('HTML5', 'https://skillicons.dev/icons?i=html'),
        ('CSS3', 'https://skillicons.dev/icons?i=css'),
        ('FastAPI', 'https://skillicons.dev/icons?i=fastapi'),
        ('Streamlit', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-original.svg')
    ]),
    ('Cloud, DevOps & Developer Workflow', 'https://cdn.jsdelivr.net/gh/Tarikul-Islam-Anik/Animated-Fluent-Emojis@master/Emojis/Objects/Gear.png', [
        ('Git', 'https://skillicons.dev/icons?i=git'),
        ('GitHub', 'https://skillicons.dev/icons?i=github'),
        ('Docker', 'https://skillicons.dev/icons?i=docker'),
        ('VS Code', 'https://skillicons.dev/icons?i=vscode'),
        ('MySQL', 'https://skillicons.dev/icons?i=mysql'),
        ('PowerShell', 'https://skillicons.dev/icons?i=powershell'),
        ('AI / Prompts', 'https://skillicons.dev/icons?i=ai')
    ])
]

def generate_table_html():
    html = '<div align="center">\n'
    for title, emoji_url, items in categories:
        html += f'\n  <h4 align="center">\n'
        html += f'    <img src="{emoji_url}" width="24" style="vertical-align:middle;" />\n'
        html += f'    {title}\n'
        html += f'  </h4>\n'
        html += '  <table align="center">\n'
        
        # Determine items per row: if 10 items, do 5x2, else all in 1 row
        cols = 5 if len(items) == 10 else len(items)
        for i, (name, icon_url) in enumerate(items):
            if i % cols == 0:
                html += '    <tr>\n'
            
            style_attr = ' style="object-fit: contain;"' if 'xgboost' in icon_url else ''
            width_attr = '56' if 'xgboost' in icon_url else '48'
            html += f'      <td align="center" width="108">\n'
            html += f'        <img src="{icon_url}" width="{width_attr}" height="48"{style_attr} alt="{name}" />\n'
            html += f'        <br><sub><b>{name}</b></sub>\n'
            html += f'      </td>\n'
            
            if i % cols == (cols - 1) or i == len(items) - 1:
                html += '    </tr>\n'
        html += '  </table>\n'
    html += '\n</div>'
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
