# ------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# ------------------------------------------------------------------------------


import luaparser.ast
import json


def test_parse_modulefile_01():
    modulefile_path = "test/share/lmod/modulefiles/01-GCCcore-15.1.0.lua"

    with open(modulefile_path, "r") as file:
        modulefile_string = file.read()

    modulefile_ast = luaparser.ast.parse(modulefile_string)

    ast_json = None
    for index, node in enumerate(luaparser.ast.walk(modulefile_ast)):
        if index == 0:
            ast_json = json.loads((luaparser.ast.to_pretty_json(node)))["body"]["body"]
        else:
            break

    print(json.dumps(ast_json, indent=2))
