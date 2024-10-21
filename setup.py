from setuptools import setup, find_packages

setup(
    name='django-xml-view',  # Name of your library
    version='0.1.0',  # Initial release version
    description='A Django-based library for rendering XML responses with XSLT support',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/django-xml-view',  # Replace with your repo URL
    packages=find_packages(where='src'),  # Automatically find packages in the src directory
    package_dir={'': 'src'},  # Specify that packages are under the src directory
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'Django>=3.0',  # Add Django as a dependency
    ],
    python_requires='>=3.6',
)
