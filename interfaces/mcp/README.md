# NovelOS MCP Alpha

MCP exposes tools, resources and prompts over JSON-RPC stdin/stdout. Launch locally:

```bash
python -m interfaces.mcp.server
```

Write actions return a proposal until `confirm=true`. Scene generation and rewriting additionally require `mode="creator"`. The adapter shares the GUI and Runtime Core.
