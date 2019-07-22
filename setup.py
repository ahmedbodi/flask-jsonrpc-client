from setuptools import setup

setup(
    name='Flask-JSONRPC-Client',
    version='1.0',
    license='BSD',
    author='Ahmed Bodiwala',
    author_email='admin@multicoin.co',
    long_description=__doc__,
    packages=['flask_jsonrpc_client'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'requests',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
