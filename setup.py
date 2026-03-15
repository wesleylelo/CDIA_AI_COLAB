from setuptools import setup, find_packages

setup(
    name="cdia-ai-colab",
    version="0.1.0",
    description="Repositório para projetos e estudos com Jupyter Notebooks em Python",
    author="Wesley Lelo",
    author_email="",
    url="https://github.com/wesleylelo/CDIA_AI_COLAB",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "jupyter>=1.0.0",
        "jupyterlab>=3.0.0",
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "matplotlib>=3.4.0",
        "scikit-learn>=0.24.0",
        "ipython>=7.0.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)