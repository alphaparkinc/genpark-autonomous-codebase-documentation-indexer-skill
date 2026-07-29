from client import AutonomousCodebaseDocumentationIndexerClient

def main():
    client = AutonomousCodebaseDocumentationIndexerClient()
    res = client.index_codebase("src/", [".py", ".ts"])
    print(f"Indexed Symbols: {res['indexed_symbols_count']}")
    print(f"Modules Mapped: {res['architecture_graph']['modules']}")

if __name__ == "__main__":
    main()
