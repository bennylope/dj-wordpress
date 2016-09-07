from setuptools import setup
import wordpress

long_description = open('README.rst').read()


setup(
    name='dj-wordpress',
    version=wordpress.__version__,
    description='Django models and views for a WordPress database.',
    long_description=long_description,
    author='Jeremy Carbaugh',
    author_email='jcarbaugh@sunlightfoundation.com',
    maintainer='Ben Lopatin',
    maintainer_email='ben@benlopatin.com',
    url='http://github.com/bennylope/dj-wordpress/',
    packages=['wordpress'],
    package_data={'wordpress': ['templates/wordpress/*']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
    license='BSD License',
    platforms=["any"],
)
