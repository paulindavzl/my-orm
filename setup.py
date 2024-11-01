from setuptools import setup, find_packages

def read_long_description():
    try:
        with open('README.md', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Descrição longa indisponível."

setup(
    name="my_orm",
    version="1.0.0",
    description="Uma ORM simples para facilitar a implementação de SQL com Python",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    author="Paulo Chagas Chaves Silva",
    author_email="paulochz01@gmail.com",
    url="https://github.com/paulindavzl/my-orm",
    packages=find_packages(where="src"),
    package_dir={"": "src"}, 
    install_requires=[],
    extras_require={
        'dev': ['pytest==8.3.2'],
        'mysql': ['mysql-connector-python'],
        'postgres': ['pg8000'],
        'sqlite': ['sqlite3'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    entry_points={
        'console_scripts': [
            'my-orm=my_orm:main',
        ],
    },
)
