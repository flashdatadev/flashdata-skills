# FlashData Skills

[English](README.md) · [FlashData CLI](https://github.com/flashdatadev/flashdata-cli) · [API 文档](https://flashdata.dev/docs)

让 AI agent 使用 Google 搜索和 YouTube 数据：网页结果、视频元数据、转录文本及批量导出。

## 安装

使用 [uv](https://docs.astral.sh/uv/) 安装 CLI，然后设置 agent：

```sh
uv tool install flashdata-cli
flashdata setup
```

选择 Codex、Claude Code 或 Cursor，并确认项目目录。设置会安装 16 个 CLI 技能并配置访问，不执行付费查询。MCP 可选。

**注册前即可试用。** 符合条件的新用户可获得临时访问及有限 Credits，默认用于 Google 搜索和 YouTube 元数据。设置会复用已有凭据；已有密钥时，先运行 `flashdata auth login`。试用限制和后续注册步骤见[账户接入](https://github.com/flashdatadev/flashdata-cli/blob/main/docs/onboarding.md)。

[其他 CLI 安装方式](https://github.com/flashdatadev/flashdata-cli/blob/main/docs/installation.zh-CN.md)包括 pip、uv pip、Homebrew、APT、RPM 和独立下载包。

## 使用

直接向 agent 描述你需要的结果：

- “搜索近期电池回收研究，附上来源链接。”
- “找三个相关 YouTube 视频，使用可用转录文本进行总结并引用时间戳。”
- “将这个文件中的视频元数据导出为 JSONL。”
- “将这些视频的 MP3 音频交付到已配置的存储桶。”

技能对单次内容查询默认使用纯文本；需要时可要求 Markdown 或结构化 JSON。批量导出保持 **JSONL**。下载需要所有者访问权限和你的云存储目标，导出行保存交付回执。详见[批量指南](skills/flashdata/references/bulk.md)。

数据查询消耗 Credits。请向 agent 说明预算，或通过 `flashdata account balance` 查看额度。

## 技能列表

| 技能 | 用途 |
| --- | --- |
| [flashdata](skills/flashdata/SKILL.md) | CLI 设置、查询和批量工作流 |
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
| [flashdata-mcp](skills/flashdata-mcp/SKILL.md) | 可选：通过 MCP 开展网页与视频研究 |

## 设置选项

为指定 agent 安装到用户全局目录，供多个项目使用：

```sh
flashdata setup --agent codex --global --non-interactive
```

使用 `--skill google-search` 选择单个技能。`--skip-auth` 只离线安装技能，不创建访问或改变凭据；查询仍需要已配置的访问。项目目录及其他 agent 选项见[Agent 设置](https://github.com/flashdatadev/flashdata-cli/blob/main/docs/agent-setup.zh-CN.md)。

需要 MCP 时，使用可选的 [flashdata-mcp 技能及连接指南](skills/flashdata-mcp/references/connection.md)。默认安装的 16 个技能不包含该技能。

手动安装时，请复制技能的整个目录，保留 references、assets 和 scripts，并单独安装 CLI。

## 升级

```sh
uv tool upgrade flashdata-cli
flashdata setup
```

设置会更新未修改的技能，并保留本地修改。通过其他安装器安装时，先使用原安装器升级 CLI，再重新运行设置。

[贡献与测试](CONTRIBUTING.md) · [反馈问题](https://github.com/flashdatadev/flashdata-skills/issues) · [安全](SECURITY.md) · [MIT 许可证](LICENSE)
