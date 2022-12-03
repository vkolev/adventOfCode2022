# adventOfCode2022
Challenges from adventOfCode 2022


## The generator.py

With the generator.py you can generate a template for a current day challange

```bash
sage: generate.py [OPTIONS]

Options:
  --template TEXT                 [default: %d_%B_%Y]
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.
```

Template is a strftime formatted string, which allows you to have a different template for your folder structure. Default is of course the one 
I am using, but feel free to change it to your liking.

**Example:**

```bash
python generate.py %d_%B_%Y
```

will generate:

```
01_December_2022/
├── input.txt
└── main.py
```