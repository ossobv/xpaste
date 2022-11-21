#!/usr/bin/env python
from distutils.core import setup

if __name__ == '__main__':
    long_descriptions = []
    with open('README.rst') as file:
        long_descriptions.append(file.read())

    setup(
        name='xpaste',
        version='1.6',
        scripts=['xpaste'],
        data_files=[
            ('share/doc/xpaste', ['LICENSE.txt', 'README.rst']),
            ('share/man/man1', ['xpaste.1x'])],
        install_requires=[
            'python-xlib',  # >=0.14 ? not needed for Wayland..
        ],
        description=(
            "paste text into X windows that don't work with selections"),
        long_description=('\n\n\n'.join(long_descriptions)),
        author='Walter Doekes, OSSO B.V.',
        author_email='wjdoekes+xpaste@osso.nl',
        url='https://github.com/ossobv/xpaste',
        license='GPLv3+',
        platforms=['linux'],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: End Users/Desktop',
            ('License :: OSI Approved :: GNU General Public License v3 '
             'or later (GPLv3+)'),
            'Operating System :: POSIX :: Linux',
            'Environment :: X11 Applications',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Topic :: Terminals :: Terminal Emulators/X Terminals',
            'Topic :: Utilities',
        ],
    )

# vim: set ts=8 sw=4 sts=4 et ai tw=79:
