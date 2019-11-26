#!/usr/bin/env python3
#
# Copyright (c) 2019 Roberto Riggio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.

"""Setup script."""

from setuptools import setup, find_packages

setup(name="lightmano",
      version="1.0",
      description="lightMANO NFVO",
      author="Roberto Riggio",
      author_email="rriggio@fbk.eu",
      url="http://lightmano.io/",
      long_description="The lightMANO NFVO",
      packages=find_packages())
