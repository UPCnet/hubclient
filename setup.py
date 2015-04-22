from setuptools import setup, find_packages

version = '0.0'

setup(name='hubclient',
      version=version,
      description="Rest client for ULearn HUB",
      long_description="""\
""",
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Carles Bruguera',
      author_email='carles.bruguera@upcnet.es',
      url='https://github.com/UPCnet/hubclient',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
          'maxclient'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
