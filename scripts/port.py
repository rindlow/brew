#!/usr/bin/env python3

import ast
import sys


class Port(ast.NodeTransformer):

    brew_date = None
    original_gravity = None
    racking_date = None
    final_gravity = None

    def visit_ImportFrom(self, node):
        if node.module == 'Brew':
            return ast.Import([ast.alias(name='brew')])
        elif node.module == 'fermentables':
            node.module = 'brew.fermentables'
        elif node.module == 'hops':
            node.module = 'brew.hops'
        elif node.module == 'profiles':
            node.module = 'brew.profiles'
        elif node.module == 'yeast':
            node.module = 'brew.yeast'
        elif node.module == 'shbf':
            node.module = 'brew.shbf'
        return node

    def visit_Import(self, node):
        for alias in node.names:
            if alias.name == 'shbf':
                alias.name = 'brew.shbf'
        return node

    def visit_ClassDef(self, node):
        self.generic_visit(node)
        for base in node.bases:
            if base.id == 'Recipe':
                base.id = 'brew.Recipe'
                node.name = 'Recipe'
        return node

    def visit_Assign(self, node):
        # print(f'visit_Assign({ast.dump(node)}')
        self.generic_visit(node)
        for target in node.targets:
            if type(target) == ast.Name and target.id.startswith('log'):
                return None
            if type(target) == ast.Name and target.id == 'recipe':
                node.value.func.id = 'Recipe'
            if (type(target) == ast.Attribute
                and target.value.id.startswith('log')):
                if target.attr == 'brew_date':
                    self.brew_date = node.value
                if target.attr == 'bottling_date':
                    self.racking_date = node.value
                if (target.attr == 'postboil_gravity'
                    and self.original_gravity is None):
                    self.original_gravity = node.value
                if (target.attr == 'original_gravity'
                    and type(node.value) == ast.Constant):
                    self.original_gravity = node.value
                if target.attr == 'final_gravity':
                    self.final_gravity = node.value
                return None
        return node

    def visit_Call(self, node):
        self.generic_visit(node)
        # print(f'visit_Call({ast.dump(node)}')
        if type(node.func) == ast.Attribute and node.func.attr == 'report':
            node.func.value.id = 'recipe'
            node.func.attr = 'log'
            if self.brew_date is not None:
                node.keywords.append(ast.keyword('brew_date', self.brew_date))
            if self.original_gravity is not None:
                node.keywords.append(ast.keyword('original_gravity',
                                                 self.original_gravity))
            if self.racking_date is not None:
                node.keywords.append(ast.keyword('racking_date',
                                                 self.racking_date))
            if self.final_gravity is not None:
                node.keywords.append(ast.keyword('final_gravity',
                                                 self.final_gravity))
        if type(node.func) == ast.Attribute and node.func.value.id == 'shbf':
            node.func.value.id = 'brew.shbf'
        # if (type(node.func) == ast.Name
        #     and node.func.id in ('MashSchedule',
        #                          'Step',
        #                          'SingleStepMashWithMashOut')):
        #     node.func = ast.Attribute(ast.Name('brew', ast.Load()),
        #                               node.func.id,
        #                               ast.Load())

        return node

    def visit_Name(self, node):
        if node.id in ('Ingredient',
                       'MashSchedule',
                       'Step',
                       'SingleStepMashWithMashOut',
                       'dryhop',
                       'firstwort'):
            return ast.Attribute(value=ast.Name('brew', ast.Load()),
                                 attr=node.id,
                                 ctx=ast.Load())
        return node

    def visit_Attribute(self, node):
        self.generic_visit(node)
        if node.attr == 'compile':
            node.attr = 'run'
        return node


with open(sys.argv[1]) as f:
    source = ast.parse(f.read(), sys.argv[1])
    # print(ast.dump(source, indent=4))
    transformer = Port()
    source = transformer.visit(source)
    dump = ast.dump(source, indent=4)
    ported = ast.unparse(source)
    print('#!/usr/bin/env python')
    print()
    print(ported)
    # print(dump)
