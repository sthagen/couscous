#! /usr/bin/env python
"""Actionable information from specification prose.

1. visit specification textual representation documents
2. derive policies as well as rules, validate the consistency
3. generate configurations

"""
import sys

import couscous.couscous as derive


def main(argv=None):
    """Process the job."""
    argv = sys.argv[1:] if argv is None else argv
    derive.main(argv)
