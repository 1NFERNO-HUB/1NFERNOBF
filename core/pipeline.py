# core/pipeline.py
from lexer.scanner import Scanner
from parser.ast_generator import Parser
from transformer.control_flow import FlowFlattener
from compiler.assembler import BytecodeCompiler

class ObfuscationPipeline:
    def __init__(self, input_file, output_file, config):
        self.input = input_file
        self.output = output_file
        self.config = config

    def start(self):
        # 1. Read
        with open(self.input, "r") as f:
            raw_code = f.read()

        # 2. Process (The Pipe)
        tokens = Scanner(raw_code).tokenize()
        ast = Parser(tokens).parse()
        
        if self.config.CONTROL_FLOW_FLATTENING:
            ast = FlowFlattener(ast).obfuscate()

        # 3. Finalize
        bytecode = BytecodeCompiler(ast).generate()
        final_script = self.wrap_in_vm(bytecode)

        with open(self.output, "w") as f:
            f.write(final_script)

    def wrap_in_vm(self, bytecode):
        # Logic to read vm/template.lua and inject bytecode
        return f"-- 1NFERNO PROTECTED\n{bytecode}"
