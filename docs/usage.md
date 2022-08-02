# Usage

## Example 

Maybe not yet ... but if you insist:

## Call without arguments

```console
$ gengive
Usage: gengive [OPTIONS] COMMAND [ARGS]...

  Render text (Danish: gengive tekst).

Options:
  -V, --version  Display the gengive version and exit  [default: False]
  -h, --help     Show this message and exit.

Commands:
  render   render the manuscript for target.
  version  Display the gengive version and exit
```

## Version command

```console
$ gengive version
Render text (Danish: gengive tekst). version 2022.2.3
```

## Render command

### Help

```console
$ gengive render --help
Usage: gengive render [OPTIONS] [SOURCE]

  render the manuscript for target.

Arguments:
  [SOURCE]  [default: ]

Options:
  -m, --manuscript <manuscript>  Path to or name of input manuscript folder
                                 (no default)  [default: ]

  -t, --target target            Target facet to render manuscript as (default
                                 is default)  [default: default]

  -p, --publisher-root target    Publisher root (default is /somewhere)
                                 [default: /somewhere]

  -r, --render-root target       Render root (default is /somewhere)
                                 [default: /somewhere]

  -n, --dry-run                  Dry run (default is False)  [default: False]
  -h, --help                     Show this message and exit.

```

### Dry run

```console
$ gengive render examples/bar/ --dry-run
Note: Dry run - verification mode.
Updating publisher root from /somewhere to examples ...
Retrieving manuscript folders below publisher root examples ...
- bar
Identifying variants defined for document(bar) ...
- default
Requested rendering document(bar) for target(default) below /somewhere/render/bar/default/ ...
Binder analysis OK, all files resolve. Sequence of binding will be:
 1: examples/bar/foo.md
{
  "request_parameters": [
    "verify",
    "/somewhere",
    "examples/bar/",
    "default",
    "/somewhere"
  ],
  "processing_start": "2022-02-02 21:40:13 UTC",
  "manuscript": "bar",
  "variant": "default",
  "manuscript_path": "examples/bar",
  "config_path": "examples/bar/render-config.json",
  "config_hash_sha256": "1a7de86e951d0d9374cee0dc1152fe781f16db072cb45985c300d4477374bd6e",
  "config_data_version": "2022-01-30 15:42:38 UTC",
  "config_size_bytes": 59,
  "render_config": {
    "name": "the-name-of-the-thing"
  },
  "binder_path": "examples/bar/bind-default.txt",
  "binder_hash_sha256": "38cf0d8e52b3020eb9e750c30998e1759657ad927462621ddd0b706b79a140c5",
  "binder_data_version": "2022-01-30 15:41:15 UTC",
  "binder_size_bytes": 7,
  "binder": [
    "examples/bar/foo.md"
  ]
}
```

### Render

Another variant using environment variables to specify publisher and render root:

```console
$ GENGIVE_PUBLISHER_ROOT=./examples GENGIVE_RENDER_ROOT=. \
  gengive render --manuscript bar --target default
Retrieving manuscript folders below publisher root examples ...
- bar
Identifying variants defined for document(bar) ...
- default
Requested rendering document(bar) for target(default) below examples/render/bar/default/ ...
Binder analysis OK, all files resolve. Sequence of binding will be:
 1: examples/bar/foo.md
Binding source documents from (bar) for target(default) to examples/render/bar/default/the-name-of-the-thing.md ...
- Written 39 lines from 1 parts to examples/render/bar/default/the-name-of-the-thing.md
Writing HTML rendition from (bar) for target(default) to examples/render/bar/default/html/the-name-of-the-thing.html ...
Creating HTML rendition of document(bar) for target(default) below examples/render/bar/default/html/ ...
Determine set of media assets in use ...
Copying the per conventions 3 media asset folders from source to target ...
Done. Entrypoint is examples/render/bar/default/html/the-name-of-the-thing.html
```

```console
$ tree render/bar/default
render/bar/default
├── html
│   ├── images
│   │   └── red.png
│   └── the-name-of-the-thing.html
├── render-info.json
└── the-name-of-the-thing.md

2 directories, 4 files
```

```console
$ cat render/bar/default/render-info.json
{
  "request_parameters": [
    "render",
    ".",
    "examples/bar",
    "default",
    "."
  ],
  "processing_start": "2022-02-02 21:37:01 UTC",
  "manuscript": "bar",
  "variant": "default",
  "manuscript_path": "examples/bar",
  "config_path": "examples/bar/render-config.json",
  "config_hash_sha256": "1a7de86e951d0d9374cee0dc1152fe781f16db072cb45985c300d4477374bd6e",
  "config_data_version": "2022-01-30 15:42:38 UTC",
  "config_size_bytes": 59,
  "render_config": {
    "name": "the-name-of-the-thing"
  },
  "binder_path": "examples/bar/bind-default.txt",
  "binder_hash_sha256": "38cf0d8e52b3020eb9e750c30998e1759657ad927462621ddd0b706b79a140c5",
  "binder_data_version": "2022-01-30 15:41:15 UTC",
  "binder_size_bytes": 7,
  "binder": [
    "examples/bar/foo.md"
  ],
  "collation_folder": "render/bar/default",
  "collation_name": "the-name-of-the-thing.md",
  "collation_path": "render/bar/default/the-name-of-the-thing.md",
  "collation_hash_sha256": "fb47b878b8507bc9850f6df42a3548a10cabc03fb2c6beb94b5947f6625fad73",
  "collation_data_version": "2022-02-02 21:37:01 UTC",
  "collation_size_bytes": 410,
  "lines_written": 39,
  "html_folder": "render/bar/default/html",
  "html_name": "the-name-of-the-thing.html",
  "html_path": "render/bar/default/html/the-name-of-the-thing.html",
  "html_hash_sha256": "459ab962cf0c8942853721f786c165c50339e2f049546534156b41ba218a9b1e",
  "html_data_version": "2022-02-02 21:37:01 UTC",
  "html_size_bytes": 2193,
  "asset_descriptions": [
    {
      "asset_path_str": "images/red.png",
      "asset_hash_sha256": "1d129bcd632bb057ea18f16dff7d5942266fe6dfaf4d9e6c87aaa1bb7365559a",
      "asset_data_version": "2022-02-02 21:05:34 UTC",
      "asset_size_bytes": 277
    }
  ],
  "processing_stop": "2022-02-02 21:37:01 UTC",
  "processing_duration_seconds": 0.076157
}
```

```console
$ cat examples/bar/bind-default.txt
foo.md
```

```console
$ cat examples/bar/render-config.json
{
  "default": {
    "name": "the-name-of-the-thing"
  }
}
```

```console
$ cat examples/bar/foo.md
# Heading Wun

We talk from time to time.

- wun
- two
- three

1. again wun
1. two
1. three
1. and four

> a blockquote

!!! note
    Notes are this way

## Subesection

Yes a subsection

```python
print(42)
\```

## A Table Section

| Something | was | here |
|:--------- |:--- |:---- |
| or        | did | not  |

A missing image ![so missed](picture.jpg)

An existing image ![so red](images/red.png)

End.

```

```console
$ cat render/bar/default/the-name-of-the-thing.md
# Heading Wun

We talk from time to time.

- wun
- two
- three

1. again wun
1. two
1. three
1. and four

> a blockquote

!!! note
    Notes are this way

## Subesection

Yes a subsection

\```python
print(42)
\```

## A Table Section

| Something | was | here |
|:--------- |:--- |:---- |
| or        | did | not  |

A missing image ![so missed](picture.jpg)

An existing image ![so red](images/red.png)

End.

```

```console
$ cat render/bar/default/html/the-name-of-the-thing.html
<!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="description" content="Some Documents 'the-name-of-the-thing.md'.">
        <meta name="viewport" content="width=device-width, initial-scale=1">
          <style>
            html {font-family: "ITC Franklin Gothic Std Bk Cd", Verdana, Arial, sans-serif;}
            a {color: #0c2d82;}
            b {font-weight: 600;}
            h1 {font-weight: 300; text-transform: capitalize;}
            h2 {font-weight: 200;}
            li {line-height: 1.5;}
            table {table-layout: fixed; width: 90%; background-color: #ffffff; margin: 20px;
              border-collapse: collapse;}
            td, th {word-wrap: break-word; border: solid 1px #666666;}
            th {background-color: #0c2d82; color: #ffffff; font-size: 75%; font-weight: 300;}
            td {vertical-align: top; font-size: 67%; padding: 2px;}
            table caption {font-size: 120%; margin-bottom: 20px;}
            tbody tr:nth-child(odd) {background-color: #dddddd;}
            tbody tr:nth-child(even) {background-color: #ffffff;}
          </style>
        <title>the-name-of-the-thing.md</title>
      </head>
    <body>
    <h1 id="heading-wun">Heading Wun</h1>
<p>We talk from time to time.</p>
<ul>
<li>wun</li>
<li>two</li>
<li>
<p>three</p>
</li>
<li>
<p>again wun</p>
</li>
<li>two</li>
<li>three</li>
<li>and four</li>
</ul>
<blockquote>
<p>a blockquote</p>
</blockquote>
<p>!!! note
    Notes are this way</p>
<h2 id="subesection">Subesection</h2>
<p>Yes a subsection</p>
<div class="codehilite"><pre><span></span><code><span class="nb">print</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span>
</code></pre></div>

<h2 id="a-table-section">A Table Section</h2>
<table>
<thead>
<tr>
<th align="left">Something</th>
<th align="left">was</th>
<th align="left">here</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">or</td>
<td align="left">did</td>
<td align="left">not</td>
</tr>
</tbody>
</table>
<p>A missing image <img alt="so missed" src="picture.jpg"></p>
<p>An existing image <img alt="so red" src="images/red.png"></p>
<p>End.</p>
    </body>
    </html>

```
