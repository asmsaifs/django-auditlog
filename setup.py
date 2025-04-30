from setuptools import setup, find_packages

setup(
    name='django-auditlog',
    version='0.1.0',
    description='Automatic audit logging for Django using LogEntry.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='ASM Saiful Islam Chowdhury',
    author_email='asmsaifs@gmail.com',
    url='https://github.com/asmsaifs/django-auditlog',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'Django>=3.2',
        'djangorestframework',
    ],
    python_requires='>=3.7',
)
