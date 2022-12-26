# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/pilli/blob/default/sbom.json) with SHA256 checksum ([ed2590c8 ...](https://raw.githubusercontent.com/sthagen/pilli/default/sbom.json.sha256 "sha256:ed2590c87a62aa583559d4d13526f94494366c79259865bb64eb5e82675379b3")).
<!--[[[end]]] (checksum: c2cf3c1f7f16d35ec5dc2fba48c2c26e)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                               | Version                                             | License     | Author                                               | Description (from packaging data)                                  |
|:-------------------------------------------------------------------|:----------------------------------------------------|:------------|:-----------------------------------------------------|:-------------------------------------------------------------------|
| [Markdown](https://Python-Markdown.github.io/)                     | [3.3.7](https://pypi.org/project/Markdown/3.3.7/)   | BSD License | Manfred Stienstra, Yuri takhteyev and Waylan limberg | Python implementation of Markdown.                                 |
| [pandoc](https://github.com/boisgera/pandoc/blob/master/README.md) | [2.3](https://pypi.org/project/pandoc/2.3/)         | MIT License | Sébastien Boisgérault                                | Pandoc Documents for Python                                        |
| [pydantic](https://github.com/pydantic/pydantic)                   | [1.10.2](https://pypi.org/project/pydantic/1.10.2/) | MIT License | Samuel Colvin                                        | Data validation and settings management using python type hints    |
| [typer](https://github.com/tiangolo/typer)                         | [0.7.0](https://pypi.org/project/typer/0.7.0/)      | MIT License | Sebastián Ramírez                                    | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: f59afc35fde7d289fd295c97ba51eb53)-->

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
pydantic==1.10.2
  - typing-extensions [required: >=4.1.0, installed: 4.4.0]
typer==0.7.0
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: 92bd4ef5f17284a732599385f8ec2322)-->
