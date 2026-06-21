# boot.dev projects

A monorepo for my [Boot.dev](https://www.boot.dev) projects. Each project lives
in its own folder so they stay self-contained and can be run/submitted
independently.

## Layout

```
.
├── bookbot/          # first project: book text analyzer
│   ├── main.py
│   ├── stats.py
│   └── books/
└── <next-project>/   # add new projects here, one folder each
```

## Running a project

`bootdev` commands operate on the **current directory**, so always `cd` into the
project folder first:

```bash
cd bookbot
python3 main.py books/frankenstein.txt        # run locally

bootdev run <lesson-uuid>                      # run the lesson without submitting
bootdev run <lesson-uuid> -s                   # run and submit
```

Each project's own `README.md` records its lesson UUID and run instructions.

## Adding a new project

1. Create a new folder at the repo root: `mkdir my-next-project`
2. Add the project's code inside it.
3. Add a `README.md` in that folder noting its Boot.dev lesson UUID.

That's it — projects never share files, so nothing conflicts.
