# claude-skills

A collection of custom skills for [Claude](https://claude.ai) that extend its capabilities. Each skill can be installed directly via the Claude interface.

## What are Claude Skills?

Skills are small packages that teach Claude how to handle specific tasks automatically. Once installed, Claude recognizes when to apply a skill and uses it without you having to ask.

## Available Skills

| Skill | Description |
|-------|-------------|
| [auto-md-convert](./auto-md-convert/) | Automatically converts uploaded `.docx` and `.pdf` files to Markdown before reading them — saves tokens and improves accuracy |

## How to Install a Skill

1. Download the `.zip` file from the skill's folder
2. Go to [claude.ai](https://claude.ai)
3. Open **Settings → Skills** (or the skills panel)
4. Upload the `.zip` file

That's it — Claude will start using the skill automatically in future conversations.

## Contributing

Have a skill you'd like to share? Feel free to open a pull request! Please follow the existing folder structure and include a `SKILL.md` and a `README.md`.

## License

MIT
