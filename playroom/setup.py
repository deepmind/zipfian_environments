# Copyright 2022 DeepMind Technologies Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Install script for setuptools."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import importlib
import types
from setuptools import find_packages
from setuptools import setup

loader = importlib.machinery.SourceFileLoader(
    '_version', 'zipfian_environments/playroom/_version.py')
mod = types.ModuleType(loader.name)
loader.exec_module(mod)
_version = mod.__version__

setup(
    name='dm-zipf-playroom',
    version=_version,
    description=('DeepMind Zipf\'s Playroom, a set of Unity-based'
                 'machine-learning research tasks.'),
    author='DeepMind',
    license='Apache License, Version 2.0',
    keywords='reinforcement-learning python machine learning language',
    packages=find_packages(exclude=['examples']),
    install_requires=[
        'absl-py',
        'dm-env',
        'dm-env-rpc',
        'docker',
        'grpcio',
        'numpy',
        'portpicker',
    ],
    tests_require=['nose'],
    python_requires='>=3.7',
    extras_require={'examples': ['pygame']},
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
