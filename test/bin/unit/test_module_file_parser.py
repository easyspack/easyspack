# ------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# ------------------------------------------------------------------------------


import luaparser.ast


def test_parse_modulefile_01():
    modulefile_path = "test/share/lmod/modulefiles/01-GCCcore-15.1.0.lua"

    with open(modulefile_path, "r") as file:
        modulefile_string = file.read()

    modulefile_ast = luaparser.ast.parse(modulefile_string)


    for node in luaparser.ast.walk(modulefile_ast):
        print(luaparser.ast.to_pretty_str(node))
    # print(luaparser.ast.to_pretty_str(modulefile_ast))
    # print("Hello, world!")
