# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/pilli/blob/default/sbom.json) with SHA256 checksum ([65c68074 ...](https://raw.githubusercontent.com/sthagen/pilli/default/sbom.json.sha256 "sha256:65c68074f9709231ca044bb8c02ae5b64a3576e59ae7e270960a105cc6c67ea2")).
<!--[[[end]]] (checksum: a9b6db54f8f52ae627dd8d979caaa802)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                 | Version                                           | License     | Author                                               | Description (from packaging data)                                  |
|:-----------------------------------------------------|:--------------------------------------------------|:------------|:-----------------------------------------------------|:-------------------------------------------------------------------|
| [Markdown](https://Python-Markdown.github.io/)       | [3.4.1](https://pypi.org/project/Markdown/3.4.1/) | BSD License | Manfred Stienstra, Yuri takhteyev and Waylan limberg | Python implementation of Markdown.                                 |
| [pydantic](https://github.com/samuelcolvin/pydantic) | [1.9.2](https://pypi.org/project/pydantic/1.9.2/) | MIT License | Samuel Colvin                                        | Data validation and settings management using python type hints    |
| [typer](https://github.com/tiangolo/typer)           | [0.6.1](https://pypi.org/project/typer/0.6.1/)    | MIT License | Sebastián Ramírez                                    | Typer, build great CLIs. Easy to code. Based on Python type hints. |
| pandoc                                               | [2.2](https://pypi.org/project/pandoc/2.2/)       | MIT License | Sébastien Boisgérault                                | Pandoc Documents for Python                                        |
<!--[[[end]]] (checksum: 1d2399a05741d440337b490c60a4815a)-->

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
Markdown==3.4.1
pandoc==2.2
  - plumbum [required: Any, installed: 1.7.2]
  - ply [required: Any, installed: 3.11]
pydantic==1.9.2
  - typing-extensions [required: >=3.7.4.3, installed: 4.2.0]
typer==0.6.1
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: b34e05a1433a1153247db8c4dd3254a0)-->
