import setuptools
with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='chase',
    version='1.0.0',
    author='Maciej Błażewicz, Sebastian Nawrocki',
    author_email='224264@edu.p.lodz.pl',
    description='Simulation where wolf chases sheep',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Blazzeq/full_wolf_but_sheep_dead/',
    packages=setuptools.find_packages(),
    license='MIT License',
    python_requires='>=3.6'
)
