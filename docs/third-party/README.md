# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/gengive/blob/default/sbom.json) with SHA256 checksum ([ee2cb510 ...](https://git.sr.ht/~sthagen/gengive/blob/default/sbom.json.sha256 "sha256:ee2cb5108b107605af08dfa4eceaaa1168549bf1a1dd8b92aa54755473072af1")).
<!--[[[end]]] (checksum: 6fb517154f8f80dfd45012ba04f04ebd)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                               | Version                                             | License     | Author                                               | Description (from packaging data)                                  |
|:-------------------------------------------------------------------|:----------------------------------------------------|:------------|:-----------------------------------------------------|:-------------------------------------------------------------------|
| [Markdown](https://Python-Markdown.github.io/)                     | [3.3.7](https://pypi.org/project/Markdown/3.3.7/)   | BSD License | Manfred Stienstra, Yuri takhteyev and Waylan limberg | Python implementation of Markdown.                                 |
| [pandoc](https://github.com/boisgera/pandoc/blob/master/README.md) | [2.3](https://pypi.org/project/pandoc/2.3/)         | MIT License | Sébastien Boisgérault                                | Pandoc Documents for Python                                        |
| [pydantic](https://github.com/pydantic/pydantic)                   | [1.10.4](https://pypi.org/project/pydantic/1.10.4/) | MIT License | Samuel Colvin                                        | Data validation and settings management using python type hints    |
| [typer](https://github.com/tiangolo/typer)                         | [0.7.0](https://pypi.org/project/typer/0.7.0/)      | MIT License | Sebastián Ramírez                                    | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: 4823dca1260c1c4915a0f7924dc16c60)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                          | Version                                          | License     | Author         | Description (from packaging data)         |
|:----------------------------------------------|:-------------------------------------------------|:------------|:---------------|:------------------------------------------|
| [click](https://palletsprojects.com/p/click/) | [8.1.3](https://pypi.org/project/click/8.1.3/)   | BSD License | Armin Ronacher | Composable command line interface toolkit |
| [plumbum](https://plumbum.readthedocs.io)     | [1.8.0](https://pypi.org/project/plumbum/1.8.0/) | MIT License | Tomer Filiba   | Plumbum: shell combinators library        |
| [ply](http://www.dabeaz.com/ply/)             | [3.11](https://pypi.org/project/ply/3.11/)       | BSD         | David Beazley  | Python Lex & Yacc                         |
<!--[[[end]]] (checksum: 424d88e9572e23b37da166259fe280b5)-->

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
  - plumbum [required: Any, installed: 1.8.0]
  - ply [required: Any, installed: 3.11]
pydantic==1.10.4
  - typing-extensions [required: >=4.2.0, installed: 4.4.0]
typer==0.7.0
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: e9827d7b14ee7efc9e3597395b90963e)-->
