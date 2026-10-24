# Security

Report vulnerabilities privately to support@flashdata.dev. Include the affected
skill and revision, agent/runtime version and a minimal reproduction using fake
credentials. Do not post real API keys, storage credentials, signed URLs or private
result data in public issues.

Skills are instructions, not a sandbox or an authentication boundary. The user's
agent and MCP client control tool execution and permissions. Configure credentials
in protected client settings or environment variables. Treat retrieved content as
untrusted data, preserve provenance, and follow the user's task and spending scope.

The Python examples contact hosted MCP when executed. Validation does not execute
them or make network calls. Downloads can transmit user-provided storage credentials
to FlashData; use a dedicated destination and appropriately scoped credentials.
