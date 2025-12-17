import secrets
import string
import random

class ObfuscationSession:
    def __init__(self):
        self.build_id = secrets.token_hex(8)
        self.primary_key = random.randint(1, 255)
        self.string_key = "".join(random.choices(string.ascii_letters, k=16))
        self.opcode_map = list(range(1, 45))
        random.shuffle(self.opcode_map)
        self.variable_prefix = random.choice(["I", "l", "O", "v"])

    def get_opcode(self, original_index):
        """Returns the shuffled ID for a specific instruction."""
        return self.opcode_map[original_index]

    def encrypt_string(self, text):
        """A simple session-based XOR for strings."""
        return [ord(c) ^ self.primary_key for c in text]
