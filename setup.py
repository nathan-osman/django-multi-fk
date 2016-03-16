from distutils.core import find_packages, setup


setup(
    name='multi_fk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Django>=1.7',
    ],
    author='Nathan Osman',
    author_email='nathan@quickmediasolutions.com',
    description="Automatically update multiple foreign keys in the Django admin",
    license='MIT',
    url='https://github.com/nathan-osman/django-multi-fk',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
