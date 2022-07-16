#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Visit specification textual representation documents, derive policies as well as rules, validate the consistency, and generate configurations."""
import sys

import couscous.couscous as derive


def main(argv=None):
    """Process the job."""
    argv = sys.argv[1:] if argv is None else argv
    derive.main(argv)
