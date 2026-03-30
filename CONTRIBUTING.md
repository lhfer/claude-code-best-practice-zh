# CONTRIBUTING

欢迎贡献，但请先接受这件事：

这不是一个“谁都可以随手翻两句”的仓库。  
它更像一个需要持续维护的中文本土化 fork。

## 欢迎哪类贡献

- 上游同步提醒
- 中文润色和结构优化
- 术语统一修正
- 本土化建议
- README 学习路径改进
- 链接失效、事实漂移、概念过时修复

## 不欢迎哪类贡献

- 直接把 `.claude/`、`.codex/`、`.mcp.json` 翻成中文
- 逐词直译、没有解释价值的“机翻式 PR”
- 改坏命令、路径、frontmatter、配置键
- 只改语气，不核对 upstream 事实

## PR 之前先做这几步

1. 看 [LOCALIZATION_POLICY.md](LOCALIZATION_POLICY.md)
2. 看 [GLOSSARY.md](GLOSSARY.md)
3. 看 [SYNC_STATUS.md](SYNC_STATUS.md)
4. 判断你的改动属于哪类：
   - `sync`
   - `docs`
   - `glossary`
   - `community`

## 提交建议

推荐 commit message：

- `sync: align README with upstream v2.x.x`
- `docs: rewrite skills guide for Chinese readers`
- `glossary: unify agent terminology`
- `community: add issue template for upstream drift`

## 提交 PR 时请说明

- 改了哪些文件
- 这是同步 upstream 还是中文重编
- 有没有改动执行层
- 是否更新了 `SYNC_STATUS.md`
- 是否影响了术语一致性

## 关于 upstream 漂移

如果你发现上游更新了，但中文仓还没跟上，请优先提 issue，内容最好包含：

- upstream 链接
- 受影响模块
- 你判断这是“事实变更”还是“文案层更新”

## 对中文化的要求

好的中文化应该满足：

- 中文自然，不像机翻
- 对新手友好，不只翻术语
- 对老开发者可信，不胡编乱造
- 执行层不被破坏

如果你的改动做不到这四条，先别急着提 PR。
