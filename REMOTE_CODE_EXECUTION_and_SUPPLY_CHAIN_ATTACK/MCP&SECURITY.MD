# MCP & Security

_Remote Code Execution (RCE), Supply Chain Attack_

---

## Attack Steps

**01.** Create Malicious `gist.github.com` file

**02.** Expose a tool that downloads the malicious file

**03.** Compromise MCP Client

---

### Summary

- **Attackers** can leverage the supply chain by hosting malicious files (e.g., on GitHub Gist).
- By tricking a tool to download and execute the file, attackers can achieve **Remote Code Execution (RCE)** on MCP clients.
- This highlights the importance of validating code and file downloads in all MCP workflows.

> **Best Practices:**  
> - Always verify file sources.  
> - Implement strict security checks on external tool integrations.  
> - Regularly audit your supply chain for vulnerabilities.

