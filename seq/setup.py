from setuptools import setup
setup(
    name='xen_pyseq',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'pyseq=seq:play'
        ]
    }
)
