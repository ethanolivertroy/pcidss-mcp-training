# PCI-DSS MCP Training

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ethanolivertroy/pcidss-mcp-training/blob/main/build-mcp-server.ipynb)

Learn to build Model Context Protocol (MCP) servers for compliance documentation.

## What You'll Learn

This hands-on notebook teaches GRC professionals how to build MCP servers that AI assistants can use. PCI-DSS is the example, but patterns apply to any framework:

- NIST 800-53
- ISO 27001
- SOC 2
- FedRAMP
- HIPAA

## Getting Started

### Option 1: Google Colab (Recommended)

**Click the Colab badge above** to start the interactive tutorial - no local setup required.

### Option 2: VS Code with Colab Extension

Use the [Google Colab extension for VS Code](https://marketplace.visualstudio.com/items?itemName=Google.colab) to run the notebook directly in your editor:

1. Install the extension from VS Code Marketplace
2. Open `build-mcp-server.ipynb` in VS Code
3. Click "Open in Colab" or run cells directly with Colab runtime

This gives you the best of both worlds: VS Code's editing experience with Colab's free GPU/compute.

### Option 3: Local Jupyter

```bash
pip install jupyter openpyxl
jupyter notebook build-mcp-server.ipynb
```

## Topics Covered

1. Data extraction from Excel (Prioritized Approach Tool)
2. Building fast O(1) lookup indexes
3. MCP tool patterns with Zod schemas
4. Full-text search with TF-IDF
5. Building a complete MCP server in TypeScript
6. Adapting for other compliance frameworks

## Data Source

The tutorial uses the [PCI-DSS Prioritized Approach Tool](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Supporting%20Document/Prioritized-Approach-Tool-For-PCI-DSS-v4_0_1.xlsx) from PCI Security Standards Council.

## License

MIT - See [LICENSE](LICENSE)
