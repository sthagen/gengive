# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/gengive/blob/default/sbom/cdx.json) with SHA256 checksum ([b94535b5 ...](https://git.sr.ht/~sthagen/gengive/blob/default/sbom/cdx.json.sha256 "sha256:b94535b5957641ae7bbbd1229578bc06e01e6629e81c0b0febae58bea68199fc")).
<!--[[[end]]] (checksum: 057c586d67b0dfc05cc5be7e843a16e8)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                               | Version                                               | License     | Author                                               | Description (from packaging data)                                  |
|:-------------------------------------------------------------------|:------------------------------------------------------|:------------|:-----------------------------------------------------|:-------------------------------------------------------------------|
| [Markdown](https://Python-Markdown.github.io/)                     | [3.3.7](https://pypi.org/project/Markdown/3.3.7/)     | BSD License | Manfred Stienstra, Yuri takhteyev and Waylan limberg | Python implementation of Markdown.                                 |
| [pandoc](https://github.com/boisgera/pandoc/blob/master/README.md) | [2.3](https://pypi.org/project/pandoc/2.3/)           | MIT License | Sébastien Boisgérault                                | Pandoc Documents for Python                                        |
| [pydantic](https://github.com/pydantic/pydantic)                   | [1.10.10](https://pypi.org/project/pydantic/1.10.10/) | MIT License | Samuel Colvin                                        | Data validation and settings management using python type hints    |
| [typer](https://github.com/tiangolo/typer)                         | [0.9.0](https://pypi.org/project/typer/0.9.0/)        | MIT License | Sebastián Ramírez                                    | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: d11268246f3d82c39f189dabac81d8c6)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                             | Version                                                    | License                            | Author                                                                                | Description (from packaging data)                      |
|:-----------------------------------------------------------------|:-----------------------------------------------------------|:-----------------------------------|:--------------------------------------------------------------------------------------|:-------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)                    | [8.1.5](https://pypi.org/project/click/8.1.5/)             | BSD License                        | UNKNOWN                                                                               | Composable command line interface toolkit              |
| [plumbum](https://github.com/tomerfiliba/plumbum)                | [1.8.2](https://pypi.org/project/plumbum/1.8.2/)           | MIT License                        | Tomer Filiba <tomerfiliba@gmail.com>                                                  | Plumbum: shell combinators library                     |
| [ply](http://www.dabeaz.com/ply/)                                | [3.11](https://pypi.org/project/ply/3.11/)                 | BSD                                | David Beazley                                                                         | Python Lex & Yacc                                      |
| [typing_extensions](https://github.com/python/typing_extensions) | [4.7.1](https://pypi.org/project/typing_extensions/4.7.1/) | Python Software Foundation License | "Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee" <levkivskyi@gmail.com> | Backported and Experimental Type Hints for Python 3.7+ |
<!--[[[end]]] (checksum: b43c2a174339e68896d5aee47e1967fd)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
Markdown==3.3.7
pandoc==2.3
├── plumbum [required: Any, installed: 1.8.2]
└── ply [required: Any, installed: 3.11]
pydantic==1.10.10
└── typing-extensions [required: >=4.2.0, installed: 4.7.1]
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.5]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: d69092266dfb2ce11240306f52356fbd)-->
