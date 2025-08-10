# AST-Aware Tooling Investigation

**Goal:** Investigate AST-aware tooling that can be integrated with Claude Code to improve code search speed and precision beyond grep-based approaches.

## Progress Log

### 2025-08-10
- **Initial insight:** Claude Code does extensive grepping for tool-based searches. AST and type-system aware tooling could provide significant speed and precision improvements.

- **Investigated:** https://github.com/oraios/serena
  - **Result:** Abandoned - missing basic features like "rename symbol" refactoring

### Next Steps
- [ ] Investigate https://github.com/isaacphi/mcp-language-server
- [ ] Evaluate integration possibilities with Claude Code
- [ ] Compare performance vs grep-based searches

## Notes
- Focus on tools that provide comprehensive language server features
- Must support common refactoring operations
- Integration should work within Claude Code's MCP architecture