# FlashData Skills

[English](README.md) · [FlashData](https://flashdata.dev) · [API 文档](https://flashdata.dev/docs) · [价格](https://flashdata.dev/pricing)

FlashData 官方 agent 技能仓库，提供 Google 搜索、YouTube 数据及基于来源的研究指导。共 **16 个可移植技能**：1 个通用研究技能和 15 个任务技能，包含说明与示例。

## 选择工作流

| 目标 | 入口 |
| --- | --- |
| 跨网页和视频来源开展研究 | `flashdata` |
| 使用单项 Google 或 YouTube 能力 | 下方任务技能列表 |
| 配置 MCP 连接 | [连接说明](skills/flashdata/references/connection.md) |
| 运行本地 MCP 服务 | [FlashData MCP](https://github.com/flashdatadev/flashdata-mcp) |
| 使用独立命令行应用 | [FlashData CLI](https://github.com/flashdatadev/flashdata-cli) |

## 安装

通过 [skills CLI](https://skills.sh/docs)查看可用技能：

```sh
npx skills add flashdatadev/flashdata-skills --list
```

安装通用研究技能，或仅选择需要的任务技能：

```sh
npx skills add flashdatadev/flashdata-skills --skill flashdata
npx skills add flashdatadev/flashdata-skills --skill google-search --skill youtube-transcript
```

按照提示选择 agent；使用 `--agent codex` 可指定 Codex，也可选择 CLI 支持的其他 agent。默认安装到当前项目，`--global` 表示用户全局安装。替换同名技能前，请检查技能来源和已有内容。

也可以按照 agent 的文档，将完整的 `skills/<name>/` 目录复制到相应位置。有 `references/` 的技能必须保留该子目录，各技能不依赖同级技能。

安装技能只提供说明及参考文件，不会安装 MCP 服务或 CLI，不会自动连接账户，也不会执行数据查询。客户端市场审核和目录收录与 GitHub 源码发布是不同事项。

## 连接 FlashData

优先复用已有连接，或按照[客户端配置说明](https://flashdata.dev/mcp)设置：

- 地址：`https://data.flashdata.dev/mcp`
- 传输：Streamable HTTP
- API Key 请求头：`X-API-Key`
- [在 FlashData 控制台获取密钥](https://flashdata.dev/app/api-keys)

密钥应放在客户端受保护的配置或环境变量中，不要发送到聊天或提交到仓库。客户端支持的认证方式不同，请使用对应客户端的配置格式。本地 stdio 服务参见 [flashdata-mcp](https://github.com/flashdatadev/flashdata-mcp#run-locally)。

连接后，可让 agent 调用 `get_pricing`，参数为 `source: "google_search"`、`request_count: 1`，只查询一次搜索的报价，不执行搜索。报价是免费连接检查，不代表授权执行付费查询。

任务技能的 Python 示例需要 Python 3.10+、`mcp==1.30.0` 和 `httpx==0.28.1`。这些是可选的托管 MCP 示例依赖，阅读或安装技能本身不需要安装它们。执行数据示例会发起付费查询，应遵循已授权的任务范围和预算。

## 技能列表

| 技能 | 用途 |
| --- | --- |
| [flashdata](skills/flashdata/SKILL.md) | 跨来源的网页与视频研究 |
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
```

验证技能元数据、相对文件引用、文件范围和 Python 示例语法，不执行示例，不连接 FlashData。CI 使用 Python 3.10 和 3.14。维护及来源说明见 [CONTRIBUTING.md](CONTRIBUTING.md) 和 [PROVENANCE.md](PROVENANCE.md)。

支持：[GitHub Issues](https://github.com/flashdatadev/flashdata-skills/issues) · [support@flashdata.dev](mailto:support@flashdata.dev)。安全问题请按 [SECURITY.md](SECURITY.md) 私下反馈。

[MIT 许可证](LICENSE)适用于技能说明，不授予 FlashData 服务或第三方数据的访问权。
