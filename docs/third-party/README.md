# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/pilli/blob/default/sbom.json) with SHA256 checksum ([c28cf7a6 ...](https://raw.githubusercontent.com/sthagen/pilli/default/sbom.json.sha256 "sha256:c28cf7a6bcfa8afbfcdb7edc97d07e55686e20fa13d20d77389ee65cf17e8c0d")).
<!--[[[end]]] (checksum: ba0caf8edee6a9e8c77c90e9d9dd4372)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                 | Version                                           | License     | Author                                               | Description (from packaging data)                                  |
|:-----------------------------------------------------|:--------------------------------------------------|:------------|:-----------------------------------------------------|:-------------------------------------------------------------------|
| [Markdown](https://Python-Markdown.github.io/)       | [3.3.7](https://pypi.org/project/Markdown/3.3.7/) | BSD License | Manfred Stienstra, Yuri takhteyev and Waylan limberg | Python implementation of Markdown.                                 |
| [pydantic](https://github.com/samuelcolvin/pydantic) | [1.9.1](https://pypi.org/project/pydantic/1.9.1/) | MIT License | Samuel Colvin                                        | Data validation and settings management using python type hints    |
| [typer](https://github.com/tiangolo/typer)           | [0.4.2](https://pypi.org/project/typer/0.4.2/)    | MIT License | Sebastián Ramírez                                    | Typer, build great CLIs. Easy to code. Based on Python type hints. |
| pandoc                                               | [2.2](https://pypi.org/project/pandoc/2.2/)       | MIT License | Sébastien Boisgérault                                | Pandoc Documents for Python                                        |
<!--[[[end]]] (checksum: 2b30ec4dc3937e358c9bcb2f7c27f501)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                          | Version                                        | License     | Author         | Description (from packaging data)         |
|:----------------------------------------------|:-----------------------------------------------|:------------|:---------------|:------------------------------------------|
| [click](https://palletsprojects.com/p/click/) | [8.1.3](https://pypi.org/project/click/8.1.3/) | BSD License | Armin Ronacher | Composable command line interface toolkit |
<!--[[[end]]] (checksum: dc3a866a7aa3332404bde3da87727cb9)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="https://raw.githubusercontent.com/sthagen/pilli/default/docs/third-party/package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
Markdown==3.3.7
pandoc==2.2
  - plumbum [required: Any, installed: 1.7.2]
  - ply [required: Any, installed: 3.11]
pydantic==1.9.1
  - typing-extensions [required: >=3.7.4.3, installed: 4.2.0]
typer==0.4.2
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: dcbd8aa007e70a9cc9dd3b9d7f48a26d)-->
