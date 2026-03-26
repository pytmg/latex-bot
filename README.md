# latex-bot

Basically, a LaTeX Discord Bot.

It renders math. Not graphs or anything, just the formulae.

![LaTeX Example](./LaTeX%20Example.png)

`S\to S+\frac{\left(S_{target}-S\right)}{40},R\to R+\frac{S}{10}`

---

# Setup Guide

## Requirements

- Python
- PIP
- venv

## Setup

> [!NOTE]
> I'll be using Linux as an example here, venv setup may differ if you're on MacOS, Windows or otherwise.

Git clone the repository and cd into it.
```sh
~ $ git clone https://github.com/pytmg/latex-bot.git
~ $ cd latex-bot
```

Setup a .venv and enter the virtual environment to install the dependencies.
```sh
~/latex-bot $ python3 -m venv .venv
~/latex-bot $ .venv/bin/activate
(.venv) ~/latex-bot $ pip install -r requirements.txt
```

Then set up a .env file to set your TOKEN.
```sh
(.venv) ~/latex-bot $ echo "TOKEN=YOUR_BOT_TOKEN" > .env
```

Then just run the script.
```sh
(.venv) ~/latex-bot $ python3 .
```

## Usage

Install your bot for your user. I'm not walking through how to do that, [Google](https://google.com/search?q=how+to+make+a+discord+bot) exists for a reason.

Then use the `/latex` command with any valid LaTeX you can come up with. Have fun.
