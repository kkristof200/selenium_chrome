import setuptools, os

readme_path = 'README.md'

if os.path.exists(readme_path):
    with open(readme_path, 'r') as f:
        long_description = f.read()
else:
    long_description = 'selenium_chrome'

setuptools.setup(
    name='selenium_chrome',
    version='0.0.25',
    author='Kristóf-Attila Kovács',
    description='selenium_chrome',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kkristof200/selenium_chrome',
    packages=setuptools.find_packages(),
    install_requires=[
        'kproxy>=0.0.1',
        'selenium>=4.0.0b4',
        'selenium-browser>=0.0.12',
        'undetected-chromedriver>=3.0.3',
        'xpath-utils>=0.0.3'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.4',
    include_package_data=True
)