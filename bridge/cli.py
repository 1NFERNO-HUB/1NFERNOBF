import argparse
from core.pipeline import run_obfuscation

def start_cli():
    print("--- 1NFERNO OBFUSCATOR ---")
    parser = argparse.ArgumentParser(description="Professional Lua Obfuscator")
    parser.add_argument("-i", "--input", help="The Lua file to protect", required=True)
    parser.add_argument("-o", "--output", help="Where to save the result", default="out.lua")
    
    args = parser.parse_args()
    
    # Send the info to the engine
    run_obfuscation(args.input, args.output)
    print(f"Successfully protected {args.input}!")
