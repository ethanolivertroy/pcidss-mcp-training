"""
PCI-DSS Compliance MCP Server
Built with FastMCP - the leading Python framework for MCP development
"""
from fastmcp import FastMCP
import json
from pathlib import Path

# Initialize server
mcp = FastMCP("pci-dss-compliance")

# Load requirements at startup
data = json.loads(Path("requirements.json").read_text())
REQUIREMENTS = {r["id"]: r for r in data["requirements"]}

@mcp.tool()
def get_requirement(id: str, include_children: bool = False) -> dict:
    """
    Get a specific PCI-DSS requirement by ID.

    Args:
        id: Requirement ID (e.g., "1.2.3")
        include_children: Include child requirements in response
    """
    req = REQUIREMENTS.get(id)
    if not req:
        return {"error": f"Requirement {id} not found"}

    result = {"requirement": req}
    if include_children:
        result["children"] = [
            r for r in REQUIREMENTS.values()
            if r.get("parentId") == id
        ]
    return result

@mcp.tool()
def search_requirements(query: str, limit: int = 10) -> dict:
    """
    Search PCI-DSS requirements by keyword.

    Args:
        query: Search terms (e.g., "encryption", "firewall")
        limit: Maximum number of results to return
    """
    query_lower = query.lower()
    matches = [
        {"id": r["id"], "title": r["title"]}
        for r in REQUIREMENTS.values()
        if query_lower in r["title"].lower()
    ]
    return {
        "query": query,
        "count": len(matches),
        "results": matches[:limit]
    }

@mcp.tool()
def list_requirements(level: int = None, limit: int = 20) -> dict:
    """
    List PCI-DSS requirements, optionally filtered by hierarchy level.

    Args:
        level: Filter by level (1=principal, 2=sub, 3=detailed, 4=specific)
        limit: Maximum number of results to return
    """
    if level:
        reqs = [r for r in REQUIREMENTS.values() if r["level"] == level]
    else:
        reqs = list(REQUIREMENTS.values())

    return {
        "level": level or "all",
        "count": len(reqs),
        "requirements": [
            {"id": r["id"], "title": r["title"]}
            for r in reqs[:limit]
        ]
    }

if __name__ == "__main__":
    mcp.run()
