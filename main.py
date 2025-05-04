from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("docs")

USER_AGENT = "docs-app/1.0"
SERPER_URL = ""

def main():
    print("Hello from mcp-document-server!")


if __name__ == "__main__":
    main()
