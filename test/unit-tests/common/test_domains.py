# -*- coding: utf-8 -*-
"""
    :copyright: Copyright 2019-2020 by the contributors (see AUTHORS file).
    :license: BSD-2-Clause, see LICENSE for details.
"""

from pkg_resources import parse_version
from sphinx.__init__ import __version__ as sphinx_version
from sphinxcontrib_confluencebuilder_util import ConfluenceTestUtil as _
import os
import unittest

class TestConfluenceDomains(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        config = _.prepareConfiguration()
        config['confluence_adv_restricted'] = ['anchor']
        test_dir = os.path.dirname(os.path.realpath(__file__))
        dataset = os.path.join(test_dir, 'dataset-domains')
        self.expected = os.path.join(test_dir, 'expected-domains')

        doc_dir, doctree_dir = _.prepareDirectories('domains')
        self.doc_dir = doc_dir

        with _.prepareSphinx(dataset, doc_dir, doctree_dir, config) as app:
            app.build(force_all=True)

    def _assertExpectedWithOutput(self, name, expected=None):
        expected = expected if expected else self.expected
        _.assertExpectedWithOutput(self, name, expected, self.doc_dir)

    def test_domains_c(self):
        if parse_version(sphinx_version) >= parse_version('3.0'):
            self._assertExpectedWithOutput('c')
        else:
            # pre-v3.0 left-aligns pointer asterisk and embeds in variable
            expected = self.expected + '-legacy'
            self._assertExpectedWithOutput('c', expected)

    def test_domains_cpp(self):
        self._assertExpectedWithOutput('cpp')

    def test_domains_js(self):
        self._assertExpectedWithOutput('js')

    def test_domains_py(self):
        self._assertExpectedWithOutput('py')

    def test_domains_rst(self):
        self._assertExpectedWithOutput('rst')
