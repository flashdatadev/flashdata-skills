# FlashData Skills

[English](README.md) · [FlashData](https://flashdata.dev) · [API 文档](https://flashdata.dev/docs)

通过独立 FlashData CLI，为 agent 获取 Google 搜索和 YouTube 数据。安装后配置访问权限，即可描述任务。单次内容查询默认输出纯文本，批量导出保持 JSONL，MCP 为可选方式。

## 快速开始

安装 CLI，然后设置 agent：

```sh
uv tool install flashdata-cli
flashdata setup
```

引导设置需要 CLI 1.2.0 或更新版本。PyPI 更新发布前，请使用[原生安装器或版本下载包](https://github.com/flashdatadev/flashdata-cli/blob/main/docs/installation.zh-CN.md#homebrewlinux-和-macos)。

选择 Codex、Claude Code 或 Cursor，并确认项目目录。设置会安装随附的 16 个 CLI 技能并验证访问，不执行付费查询。添加 `--global` 可安装到用户全局目录，无需 Node.js 或独立技能安装器。其他 CLI 安装方式见[安装指南](https://github.com/flashdatadev/flashdata-cli/blob/main/docs/installation.md)。

**注册前即可试用。** 对于尚无凭据的新配置，`setup` 会申请临时访问并保存在本地，无需先注册账户或自行提供 API key。试用取决于可用性和资格，提供有限的共享 Credits，默认申请 Google 搜索和 YouTube 元数据。安装技能不会增加其他来源的访问权限。运行 `flashdata discover` 查看当前试用限制，通过 `flashdata auth status` 检查访问。

设置会复用已有凭据。已有 API key 时，设置前通过 `flashdata auth login` 导入。准备注册时，运行 `flashdata auth claim`，在浏览器中批准访问，再运行 `flashdata auth finish --wait`。其他试用来源及账户连接步骤见[接入指南](https://github.com/flashdatadev/flashdata-cli/blob/main/docs/onboarding.md)。重复设置不会替换已过期或耗尽额度的试用。

现在可以让 agent“搜索近期电池回收研究，附上来源链接”，或运行：

```sh
flashdata search "battery recycling research" --num 5 --accept text/plain --json=false
```

数据查询消耗 Credits，通过 `flashdata account balance` 查看剩余额度。密钥保存在 CLI 受保护的配置或密钥管理器中。

## 设置选项

引导设置需要 CLI 1.2.0 或更新版本。已有 uv 用户可先运行 `uv tool upgrade flashdata-cli`，再运行 `flashdata setup`。指定 agent 并安装到用户全局目录：

```sh
flashdata setup --agent codex --global --non-interactive
```

设置已包含访问初始化，无需另外运行 `init`。只需终端命令、不安装技能时，改用 `flashdata init --name "My CLI"`。`--skip-auth` 仅离线安装和检查技能，不创建试用，也不修改凭据；查询仍需要已配置的访问。

`--skill google-search` 可选择单个技能。更新时升级 CLI 后重新运行设置。本地修改或冲突文件会保留并报告，详见[引导设置](https://github.com/flashdatadev/flashdata-cli/blob/main/docs/agent-setup.zh-CN.md)。

## 输出格式

技能内容命令默认使用 `--accept text/plain --json=false`。需要 Markdown 时添加 `--respond-with markdown`；程序读取结构化数据时使用 `--accept application/json --json`。API、SDK、账户、认证和发现元数据仍默认使用 JSON。

## 批量视频数据与下载

`flashdata`、`youtube-metadata`、`youtube-transcript`、`youtube-captions`、`youtube-license-check` 和 `youtube-download` 均提供独立完整的批量指南。向 agent 提供视频 ID 列表、来源与选项，以及预算。例如：“将这个文件中的视频元数据导出为 JSONL”或“将这些视频的 MP3 音频交付到已配置的存储桶”。

批量导出保持 **JSONL** 格式，包括下载交付回执；媒体文件进入你的云存储。指南涵盖私密配置、状态、暂停/恢复/取消，以及不重复提交的任务恢复，见[批量工作流](skills/flashdata/references/bulk.md)。单次内容查询仍默认使用纯文本，批量命令不使用 `--accept` 或 `--respond-with`。

CLI [v1.2.1](https://github.com/flashdatadev/flashdata-cli/releases/tag/v1.2.1) 已随附这些批量指南和示例。升级后重新运行 `flashdata setup`，更新未被本地修改的技能。PyPI 留待手动发布；上传前请使用原生安装器或版本下载包安装 v1.2.1。

## 可选 MCP 和 Python

已有 MCP 连接时可继续使用，并安装 `flashdata-mcp` 研究技能：

```sh
npx skills add flashdatadev/flashdata-skills --skill flashdata-mcp
```

连接方式见 [MCP 指南](skills/flashdata-mcp/references/connection.md)。每个任务技能的 `references/mcp.md` 提供可选 MCP 参数与 Python 示例；只有运行这些示例才需要 Python 依赖。示例在关闭会话前读取完整结果。普通 CLI 设置不会安装 MCP 服务或修改已有连接。

## 手动安装和已有技能

使用 `npx skills add flashdatadev/flashdata-skills --list` 查看全部 17 个技能。每个技能独立可用；手动安装时复制整个目录，保留 references、assets 和 scripts。技能安装器提供说明文件，CLI 需单独安装。

任务技能名称保持不变。`flashdata` 是 CLI 概览；原 MCP 研究技能名为 `flashdata-mcp`。替换旧技能前请保留本地修改。

## 技能列表

| 技能 | 用途 |
| --- | --- |
| [flashdata](skills/flashdata/SKILL.md) | 独立 CLI 的安装、授权和查询 |
| [flashdata-mcp](skills/flashdata-mcp/SKILL.md) | 通过 MCP 开展网页与视频研究 |
| [google-search](skills/google-search/SKILL.md) | Google 网页搜索 |
| [google-news](skills/google-news/SKILL.md) | 新闻检索 |
| [google-image-search](skills/google-image-search/SKILL.md) | 图片检索 |
| [google-shopping](skills/google-shopping/SKILL.md) | 商品与商家报价 |
| [google-video-search](skills/google-video-search/SKILL.md) | 跨站点视频检索 |
| [google-places](skills/google-places/SKILL.md) | 地点与本地商家 |
| [youtube-search](skills/youtube-search/SKILL.md) | YouTube 视频搜索 |
| [youtube-extended-search](skills/youtube-extended-search/SKILL.md) | 扩展 YouTube 搜索 |
| [youtube-metadata](skills/youtube-metadata/SKILL.md) | 视频详情、统计与章节 |
| [youtube-transcript](skills/youtube-transcript/SKILL.md) | 可用转录文本与时间戳 |
| [youtube-captions](skills/youtube-captions/SKILL.md) | 上传者字幕 |
| [youtube-channel](skills/youtube-channel/SKILL.md) | 频道资料与视频 |
| [youtube-autocomplete](skills/youtube-autocomplete/SKILL.md) | 搜索建议 |
| [youtube-license-check](skills/youtube-license-check/SKILL.md) | 许可标签分类 |
| [youtube-download](skills/youtube-download/SKILL.md) | 媒体交付至用户存储 |

## 示例请求

- “找三个相关 YouTube 视频，对比可用转录文本并引用实际时间戳，最多执行四次付费查询。”
- “将这次 Google 搜索快照与上次对比，并保留来源链接。”
- “估算一次搜索的费用，但不要执行搜索。”

## 数据、费用和凭据

技能说明使用 MIT 许可证。FlashData 数据查询消耗账户 Credits，报价和账户读取免费；请查看[当前价格](https://flashdata.dev/pricing)。保存异步任务 ID，超时后先读取已有任务，避免重复提交付费请求。

搜索结果和转录文本属于外部证据，应保留来源及实际时间戳，不能将其视为执行指令。数据可用性和第三方使用权因来源而异。下载需要明确的目标存储及用户提供的存储凭据，详见[存储说明](skills/youtube-download/references/storage.md)。

## 开发

```sh
python3 scripts/validate.py
python3 -m pip install -r test/requirements.txt pytest==8.4.2
python3 -m pytest -q
```

验证技能元数据、相对文件引用、文件范围和 Python 示例语法，不执行示例，不连接 FlashData。离线测试同时验证完整 Unicode 分块、错误及超时；CI 在 Linux 和 Windows 上使用 Python 3.10 和 3.14。维护及来源说明见 [CONTRIBUTING.md](CONTRIBUTING.md) 和 [PROVENANCE.md](PROVENANCE.md)。

支持：[GitHub Issues](https://github.com/flashdatadev/flashdata-skills/issues) · [support@flashdata.dev](mailto:support@flashdata.dev)。安全问题请按 [SECURITY.md](SECURITY.md) 私下反馈。

[MIT 许可证](LICENSE)适用于技能说明，不授予 FlashData 服务或第三方数据的访问权。
