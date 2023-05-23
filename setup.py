from setuptools import setup, find_namespace_packages

setup(
    name="files_sort",
    version=0.1,
    description='This for sort files in folder',
    url=" ",
    author="Igor Groza",
    packages=find_namespace_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main',
        ],
    },
)
