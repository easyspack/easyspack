# ------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# ------------------------------------------------------------------------------

import lmod.spider
import lmod
import subprocess


def test_GCCcore():
    """
    Test function for the module.
    This function is a placeholder for actual tests.
    """

    spider = lmod.spider.Spider()
    module_list = spider.get_modules()

    print(module_list)




