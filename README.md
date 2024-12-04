# Character Sheet Web App

This web application allows users to create and manage character sheets for any RPG.

## Features

- Create new characters with default attributes and skills.
- Edit character details, attributes, skills, talents, armor, weapons, spells, and trappings.
- View character sheets in a structured format.

## Serving The Application Locally

**Windows** (development):

Using _**UV**_:

```{cmd}
cd 'path/to/character_creator_project/'
```

Serving for the hosting machine only:

```{cmd}
$j1 = uv run flask --app src/main run --debug 2>&1 > output.log &
```

Serving for hosting machine and check on mobile or tablet:

```{cmd}
$j1 = uv run flask --app src/main run -h 0.0.0.0 --debug 2>&1 > output.log &
```

to keep it running in the terminal remove the last `&`

**Windows** :

Using _**UV**_ :

```{cmd}
cd 'path/to/character_creator_project/'
```

```{cmd}
$j1 = uv run waitress-serve --host 127.0.0.1 --port 5000 src:app 2>&1 > output.log &
```
