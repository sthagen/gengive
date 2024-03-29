# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/gengive/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([c25b5f0d ...](https://git.sr.ht/~sthagen/gengive/blob/default/etc/sbom/cdx.json.sha256 "sha256:c25b5f0d6be6c4ee76d256b878dc7b81439145967bef2a42a3059cfeb25ec5e3")).
<!--[[[end]]] (checksum: c7d7df357696966ef38761e59cc5f8fa)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                               | Version                                           | License     | Author                                                                                                                                                                                                                                                                                                                                                                                                                           | Description (from packaging data)                                  |
|:-------------------------------------------------------------------|:--------------------------------------------------|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------|
| [Markdown](https://Python-Markdown.github.io/)                     | [3.5.1](https://pypi.org/project/Markdown/3.5.1/) | BSD License | Manfred Stienstra, Yuri Takhteyev                                                                                                                                                                                                                                                                                                                                                                                                | Python implementation of John Gruber's Markdown.                   |
| [pandoc](https://github.com/boisgera/pandoc/blob/master/README.md) | [2.3](https://pypi.org/project/pandoc/2.3/)       | MIT License | Sébastien Boisgérault                                                                                                                                                                                                                                                                                                                                                                                                            | Pandoc Documents for Python                                        |
| [pydantic](https://github.com/pydantic/pydantic)                   | [2.5.3](https://pypi.org/project/pydantic/2.5.3/) | MIT License | Samuel Colvin <s@muelcolvin.com>, Eric Jolibois <em.jolibois@gmail.com>, Hasan Ramezani <hasan.r67@gmail.com>, Adrian Garcia Badaracco <1755071+adriangb@users.noreply.github.com>, Terrence Dorsey <terry@pydantic.dev>, David Montague <david@pydantic.dev>, Serge Matveenko <lig@countzero.co>, Marcelo Trylesinski <marcelotryle@gmail.com>, Sydney Runkle <sydneymarierunkle@gmail.com>, David Hewitt <mail@davidhewitt.io> | Data validation using Python type hints                            |
| [typer](https://github.com/tiangolo/typer)                         | [0.9.0](https://pypi.org/project/typer/0.9.0/)    | MIT License | Sebastián Ramírez                                                                                                                                                                                                                                                                                                                                                                                                                | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: 75d42749993dfdb4f9e7d3f36b2aec87)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                             | Version                                                    | License                            | Author                                                                                | Description (from packaging data)                      |
|:-----------------------------------------------------------------|:-----------------------------------------------------------|:-----------------------------------|:--------------------------------------------------------------------------------------|:-------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)                    | [8.1.5](https://pypi.org/project/click/8.1.5/)             | BSD License                        | Pallets <contact@palletsprojects.com>                                                 | Composable command line interface toolkit              |
| [plumbum](https://github.com/tomerfiliba/plumbum)                | [1.8.2](https://pypi.org/project/plumbum/1.8.2/)           | MIT License                        | Tomer Filiba <tomerfiliba@gmail.com>                                                  | Plumbum: shell combinators library                     |
| [ply](http://www.dabeaz.com/ply/)                                | [3.11](https://pypi.org/project/ply/3.11/)                 | BSD                                | David Beazley                                                                         | Python Lex & Yacc                                      |
| [typing_extensions](https://github.com/python/typing_extensions) | [4.7.1](https://pypi.org/project/typing_extensions/4.7.1/) | Python Software Foundation License | "Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee" <levkivskyi@gmail.com> | Backported and Experimental Type Hints for Python 3.7+ |
<!--[[[end]]] (checksum: 13e65160a1fbeb8cb4a0f1d885f5eb2a)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
Markdown==3.5.1
pandoc==2.3
├── plumbum [required: Any, installed: 1.8.2]
└── ply [required: Any, installed: 3.11]
pydantic==2.5.3
├── annotated-types [required: >=0.4.0, installed: 0.5.0]
├── pydantic-core [required: ==2.14.6, installed: 2.14.6]
│   └── typing-extensions [required: >=4.6.0,!=4.7.0, installed: 4.7.1]
└── typing-extensions [required: >=4.6.1, installed: 4.7.1]
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.5]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: ac19af23e0c4a350809dc06d2cbc7af7)-->
