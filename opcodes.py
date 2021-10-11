allOpcodes = {
    "MOV A,B":     "0000000",
    "MOV B,A":     "0000001",
    "MOV A,Lit":   "0000010",
    "MOV B,Lit":   "0000011",
    "ADD A,B":     "0000100",
    "ADD B,A":     "0000101",
    "ADD A,Lit":   "0000110",
    "ADD B,Lit":   "0000111",
    "SUB A,B":     "0001000",
    "SUB B,A":     "0001001",
    "SUB A,Lit":   "0001010",
    "SUB B,Lit":   "0001011",
    "AND A,B":     "0001100",
    "AND B,A":     "0001101",
    "AND A,Lit":   "0001110",
    "AND B,Lit":   "0001111",
    "OR A,B":      "0010000",
    "OR B,A":      "0010001",
    "OR A,Lit":    "0010010",
    "OR B,Lit":    "0010011",
    "NOT A,A":     "0010100",
    "NOT A,B":     "0010101",
    "NOT B,A":     "0010110",
    "NOT B,B":     "0010111",
    "XOR A,B":     "0011000",
    "XOR B,A":     "0011001",
    "XOR A,Lit":   "0011010",
    "XOR B,Lit":   "0011011",
    "SHL A,A":     "0011100",
    "SHL A,B":     "0011101",
    "SHL B,A":     "0011110",
    "SHL B,B":     "0011111",
    "SHR A,A":     "0100000",
    "SHR A,B":     "0100001",
    "SHR B,A":     "0100010",
    "SHR B,B":     "0100011",
    "INC B":       "0100100",
    "MOV A,(Dir)": "0100101",
    "MOV B,(Dir)": "0100110",
    "MOV (Dir),A": "0100111",
    "MOV (Dir),B": "0101000",
    "MOV A,(B)":   "0101001",
    "MOV B,(B)":   "0101010",
    "MOV (B),A":   "0101010",
    "ADD A,(Dir)": "0101100",
    "ADD B,(Dir)": "0101101",
    "ADD A,(B)":   "0101110",
    "ADD (Dir)":   "0101111",
    "SUB A,(Dir)": "0110000",
    "SUB B,(Dir)": "0110001",
    "SUB A,(B)":   "0110010",
    "SUB (Dir)":   "0110011",
    "AND A,(Dir)": "0110100",
    "AND B,(Dir)": "0110101",
    "AND A,(B)":   "0110110",
    "AND (Dir)":   "0110111",
    "OR A,(Dir)":  "0111000",
    "OR B,(Dir)":  "0111001",
    "OR A,(B)":    "0111010",
    "OR (Dir)":    "0111011",
    "NOT (Dir),A": "0111100",
    "NOT (Dir),B": "0111101",
    "NOT (B)":     "0111110",
    "XOR A,(Dir)": "0111111",
    "XOR B,(Dir)": "1000000",
    "XOR A,(B)":   "1000001",
    "XOR (Dir)":   "1000010",
    "SHL (Dir),A": "1000011",
    "SHL (Dir),B": "1000100",
    "SHL (B)":     "1000101",
    "SHR (Dir),A": "1000110",
    "SHR (Dir),B": "1000111",
    "SHR (B)":     "1001000",
    "INC (Dir)":   "1001001",
    "INC (B)":     "1001010",
    "RST (Dir)":   "1001011",
    "RST (B)":     "1001100",
    "CMP A,B":     "1001101",
    "CMP A,Lit":   "1001110",
    "CMP B,Lit":   "1001111",
    "CMP A,(Dir)": "1010000",
    "CMP B,(Dir)": "1010001",
    "CMP A,(B)":   "1010010",
    "JMP Dir":     "1010011",
    "JEQ Dir":     "1010100",
    "JNE Dir":     "1010101",
    "JGT Dir":     "1010110",
    "JLT Dir":     "1010111",
    "JGE Dir":     "1011000",
    "JLE Dir":     "1011001",
    "JCR Dir":     "1011010",
    "JOV Dir":     "1011011"
    }