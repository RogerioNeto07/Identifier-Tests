import sys
import identifier

def main():
    if len(sys.argv) == 1:
        print("Uso: python IdentifierMain.py <string>")
    else:
        id = identifier.Identifier()
        if id.validate_identifier(sys.argv[1]):
            print("Valido")
        else:
            print("Invalido")

if __name__ == "__main__":
    main()
