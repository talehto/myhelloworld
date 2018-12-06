from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='myhelloworld',
      version='0.1',
      description='Simple python library',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='packaging test helloworld',
      url='https://github.com/talehto/myhelloworld',
      author='Tarmo Lehto',
      author_email='tarmoejlehto@gmail.com',
      license='MIT',
      packages=['myhelloworld'],
      install_requires=[],
      #test_suite='nose.collector',
      #tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['myhelloworld=myhelloworld.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)