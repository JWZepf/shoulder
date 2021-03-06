#
# Shoulder
# Copyright (C) 2018 Assured Information Security, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import unittest
import os
import sys

from shoulder.generator import *
from shoulder.register import Register
from shoulder.logger import logger
from test.support.constants import *

class TestGeneratorInit(unittest.TestCase):

    def test_generate_all(self):
        test_outfile = os.path.abspath(os.path.join(TEST_TOP_DIR, "out/generate_all_output.txt"))
        all_generators = [cls for cls in abstract_generator.AbstractGenerator.__subclasses__()]
        generator_count = len(all_generators)

        regs = [Register()]

        generate_all(regs, test_outfile)

        # TODO: parse the generator output to verify that all generators have
        # been applied and succeeded
        # applied_count = parse_the_logger_output()
        # self.assertTrue(generator_count == applied_count)

    def _generate_test_register_set(self):
        regs = []

        valid_r = Register()
        valid_r.name = "register"

        return regs
